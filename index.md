---
layout: term
title: ptkyr
cmd: cat about.md
---

# Eric Wang

## About

CS grad from uWaterloo with an interest in compilers and graphics, minored in pure math with an algebraic focus and C&O with a graph theory focus. For a while I thought I'd minor in chemistry too, but you apparently can't do that by only taking organic courses. Oh well, got pretty close.

My hobbies are mostly about doing things fast. I used to speedrun indie games and speedsolve various puzzles; here are some of my PBs:
+ Speedcubing (3x3): [5.57][pbsingle] single, 8.72 ao5, 10.17 ao100 ([officially][wca], much worse; I should really go to more competitions)
+ Nonograms/picross (15x15): [1:10.71][picross]
+ Minesweeper (Hard, NG): [87.437][minesweeper]

These days I take better care of my hands, so I mostly read a lot ~~in order to~~ and study Japanese. 

読み終わった作品：
- 同士少女よ、敵を撃て
- ブラフマンの埋葬
- もものかんづめ
- 魔法少女ノ魔女裁判
- 殺されて当然と少女は言った
- けものティータイム
- ここで唐揚げ弁当を食べないでください
- 狼と香辛料1～6巻
- 薬屋のひとりごと1～16巻
- 雨夜の月1～10巻
- この恋を星には願わない1～5巻
- 安達としまむら11～12巻、SS、SS2（1～10巻は英語で）
- 拝啓、在りし日に咲く花たちへ1～2巻
- 小春と湊1～3巻
- 無力聖女と無能王女1～2巻
- 週に一度クラスメイトを買う話1～3巻

音楽なら、強い女性系声やマスロックに目がなくて、ヨルシカの過激派です。

## Projects

Some stuff I've worked/am working on. If its name links back here, you'll need an [access key](/posts/_posts/2024-09-28-granting-repo-access.md) to clone the source.

+ **[joosc](/#code): A Java(?) compiler**

  For my third co-op I joined the [PLG](https://plg.uwaterloo.ca/) in Winter 2024. Woefully underqualified but eager to learn, nabbing both a [URF](https://cs.uwaterloo.ca/current-undergraduate-students/research-opportunities/undergraduate-research-fellowship-urf) and [USRA](https://uwaterloo.ca/student-awards-financial-aid/awards/nserc-undergraduate-research-awards) was enough to convince [Yizhou Zhang](https://cs.uwaterloo.ca/~yizhou/) to supervise me. To gain background in compilers/PL, I concurrently took CS444 (Compiler Construction) and audited CS442 (Principles of Programming Languages). `joosc` is the name of the Joos1W compiler two classmates and I built over four months as the main coursework of CS444.

  Joos1W is a subset of the Java Language Specification (2nd Edition) that notably (among other things) omits:
  - Nested classes
  - Exceptions
  - Private anything
  - do-while/switch/break/continue
  - Floats

  Essentially, it contains just enough to make parsing, name disambiguation, type linking and checking, dataflow analysis, inheritance, and virtual functions/interfaces interesting to implement. It also makes you hate `Array.length`, because final fields aren't supported in general, but `length` acts like one.

  Both of my team members wanted to write `joosc` in Rust. Knowing zero Rust, I agreed immediately---precisely because I knew zero Rust. Four months later, it wound up as my favourite language. That's right, this heading was really just an excuse to talk about Rust. All my homies love Rust 🦀.

  A little more on this [here](/posts/_posts/2025-01-06-lea.md).

+ **[Constructor](/#code): A UW-themed Settlers of Catan clone**

  Also a three-person job, built in C++ for my CS246 final project in Spring 2022. Runs completely on the command line with a text-based board visualization. Catan, but with a lot more geese.

* * *

## Contact

+ e-mail: `e224wang (AT) uwaterloo (DOT) ca`

* * *

[picross]: https://www.puzzle-nonograms.com/hall.php?hallsize=2&nick=ptkyr
[wca]: https://www.worldcubeassociation.org/persons/2023WANG92
[minesweeper]: https://minesweeper.online/game/826309427
[pbsingle]: https://cubedb.net/?puzzle=3x3&title=pb&scramble=B-_F2_U2_R2_D2_R2_F_D2_B2_U2_L2_D2_U-_B2_L-_F_L_D_L2_F_R&time=5.57&alg=z2_y_%2F%2F_inspection%0AD2_U2_R-__%2F%2F_cross%0Ay-_U_L_U_L-_%2F%2F_1st_pair%0AU-_R_U2_R-_U_R_U-_R-_%2F%2F_2nd_pair%0AL-_U-_L_U_y-_L_U_L-_%2F%2F_3rd_pair%0AU2_R_U_R-_%2F%2F_4th_pair%0AR_U_R-_U_R_U2_R-_U_%2F%2F_OLL(CP)
