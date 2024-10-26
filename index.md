---
layout: term
title: ptkyr
cmd: cat about.md
---

# Eric Wang

## About Me

 I'm a third year CS student at uWaterloo, with an interest in compilers and graphics. Also minoring in pure math with an algebraic focus and C&O with a graph theory focus. For a while I thought I'd minor in chemistry too, but it turns out you can't do that by only taking organic courses. Oh well, got pretty close.

My hobbies are mostly about doing things fast. I used to speedrun indie games and speedsolve various puzzles; here are some of my PBs:
+ Speedcubing (3x3): 6.25 single, 8.72 ao5, 10.17 ao100 ([officially][wca], much worse; I should really go to more competitions)
+ Nonograms/picross (15x15): [1:10.71][picross]
+ Minesweeper (Hard, NG): [87.437][minesweeper]

These days my hands can't take much stress, so I study Japanese. 現在、薬屋のひとりごとの小説を読んでいるが、たまにこの選択を後悔します。最初の本として勧めるはずがない。どうして選んだのがわからない。音楽なら、強い女性声に目がなくて、菅原圭やヨルシカが好き、Eveやtoeもよく聴きます。

## Code

These are some projects I've worked/am working on. If its name links back here, you'll need an [access key](/notes/_posts/2024-09-28-granting-repo-access.md) to clone the source.

+ **[joosc](/#code): A Java(?) compiler**

  For my third co-op I did a research term at the [PLG](https://plg.uwaterloo.ca/) in Winter 2024. Woefully underqualified but eager enough to learn, nabbing both a [URF](https://cs.uwaterloo.ca/current-undergraduate-students/research-opportunities/undergraduate-research-fellowship-urf) and [USRA](https://uwaterloo.ca/student-awards-financial-aid/awards/nserc-undergraduate-research-awards) was enough to convince [Yizhou Zhang](https://cs.uwaterloo.ca/~yizhou/) to supervise me. To gain background in compilers and PL work, I took CS444 during the term and also audited CS442. `joosc` is the name of the Joos1W compiler I and two other group members built over those four months.

  Joos1W is a subset of the Java Language Specification (2nd Edition) that notably (among other things) omits:
  - Nested classes
  - Exceptions
  - Private anything
  - do-while/switch/break/continue
  - Floats

  Essentially, it contains just enough to make parsing, name disambiguation, type linking and checking, dataflow analysis, inheritance, and virtual functions/interfaces difficult to implement. It also makes you hate `Array.length`.

  Both of my team members wanted to build `joosc` in Rust. Knowing zero Rust, I agreed immediately---precisely because I knew zero Rust. Four months later it became my favourite language and easily the one I am most comfortable in. That's right, this heading was really just an excuse to talk about Rust. All my homies love Rust 🦀.

+ **[Constructor](/#code): A UW-themed Settlers of Catan clone**

  Also a three-person job, built in C++ for my CS246 final project in Spring 2022. Runs completely on the command line with a text-based board visualization. Catan, but with a lot more geese.

* * *

### Contact

+ e-mail: `e224wang (AT) uwaterloo (DOT) ca`

* * *

[picross]: https://www.puzzle-nonograms.com/hall.php?hallsize=2&nick=ptkyr
[wca]: https://www.worldcubeassociation.org/persons/2023WANG92
[minesweeper]: https://minesweeper.online/game/826309427
