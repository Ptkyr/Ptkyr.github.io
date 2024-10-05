---
layout: post
title: "Dividing by multiplying"
categories: compilers
author: ptkyr
---

Today I was staring at some LLVM IR and AArch64 assembly that went a little like this:
```cpp
for (int i = 0; i < foo.field.size(); ++i) { ... }
```
```llvm
cleanup:                   // %preds: for.body, ...
    %sdiv.i.i = sdiv exact i64 %ptr.sub.i.i, i64 120, !...
```
```nasm
.BB34:                     ; %cleanup
    ldp x8, x9, [x20, #72]
    sub x9, x9, x8
    asr x9, x9, 3
    mul x9, x9, x23        ; !!!
```
That 120 comes from `foo.field` being a `std::vector<T>` where `sizeof(T) == 120`. The assembly loads the start and end of the vector's active capacity and does some pointer arithmetic to calculate `size()`. The only weird thing is that `mul` somehow performing division by 15. 

A little manual dataflow analysis showed that the register allocator's favourite child, `x23`, was initialized as such at the start of `%entry` and never def'd again:
```nasm
mov  x23, #-1229782938247303442  ; 0xeeeeeeeeeeeeeeee
; ... about ten instructions, for some reason
movk x23, #61167                 ; 0xeeef
```
ARM's `movk` instruction means to move in a 16-bit immediate while keeping the rest of the bits unchanged. One can optionally shift the immediate before moving, but that didn't happen here. In fact, because ARM instructions must fit in 32-bit words, it typically takes several `movk` instructions to load a 64-bit immediate, like so:
```nasm
mov     x22, #14673
movk    x22, #34235, lsl #16
movk    x22, #36191, lsl #32
movk    x22, #62601, lsl #48
```
I suppose some compression magic happens to let it load `0xeeeeeeeeeeeeeeee` in one go. Anyways, the final value of `x23` is `0xeeeeeeeeeeeeeeef`. Turns out this is the multiplicative inverse of 15 in $$\mathbb{Z}_{2^{64}}$$. Just for fun, here's that multiplication carried out by hand against 480, yielding 32 as expected (in 16-bit, for brevity):
<!-- |&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|
|mtplr&nbsp;&nbsp;|   |   |   |   |   |   |   | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
|mcand | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |
||___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
|carry | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
||___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
||   |   |   |   |   |   |   | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
||   |   |   |   |   |   | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |   |
||   |   |   |   |   | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |   |   |
||   |   |   |   | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |   |   |   |
||   |   | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |   |   |   |   |   |
||   | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |   |   |   |   |   |   |
|| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |   |   |   |   |   |   |   |
|| 1 | 1 | 0 | 0 | 0 | 0 | 0 |   |   |   |   |   |   |   |   |   |
|| 1 | 0 | 0 | 0 | 0 | 0 |   |   |   |   |   |   |   |   |   |   |
||___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
|| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | -->

|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;|
|mtplr &nbsp;&nbsp;| 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |
|mcand|   |   |   |   |   |   |   | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
||___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
|carry | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
||___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
|| 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |   |   |   |   |   |
|| 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |   |   |   |   |   |   |
|| 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |   |   |   |   |   |   |   |
|| 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |   |   |   |   |   |   |   |   |
||___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
|| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

This suggests that division by a compile-time constant actually never requires division. Say $$p$$ is some prime radix (typically 2) in a number system with $$j$$ bits, and $$n = p^k \ell$$ with $$k \leq j$$ and $$\gcd(p, \ell) = 1 \implies \gcd(p^j, \ell) = 1$$. By counting the number of zero bits of $$n$$ from the right, you can divide out all the powers of $$p$$ with bitshifts and then multiply by $$\ell^{-1} \in \mathbb{Z}_{p^j}$$, which is guaranteed to exist. [LLVM does exactly this][llvm_isel]! They [find multiplicative inverses][inverse] with [Newton's method][newton].

So yeah. If you ever want to know the inverse of $$n$$ (broken up into 16-bit chunks of hex) in $$\mathbb{Z}_{2^{k}}$$ for $$k \in \{8,16,32,64\}$$ and more, just divide by $$n$$ in some program and pass it to clang with `-S -O3`.

[rust_table]: https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=50869acce3245dcfaaa7eb62e5a590ea
[llvm_isel]: https://github.com/llvm/llvm-project/blob/llvmorg-19.1.1/llvm/lib/CodeGen/GlobalISel/CombinerHelper.cpp#L5415
[inverse]: https://github.com/llvm/llvm-project/blob/llvmorg-19.1.1/llvm/lib/Support/APInt.cpp#L1244
[newton]: https://marc-b-reynolds.github.io/math/2017/09/18/ModInverse.html
