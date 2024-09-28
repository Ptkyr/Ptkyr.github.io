---
layout: term
title: ptkyr
cmd: cat about.md
---

# Eric Wang

## About Me

素直に紹介したくありません。

## Code

+ **[joosc](): A Java(?) compiler**

  For my third co-op I did a research term at the [PLG](https://plg.uwaterloo.ca/) in Winter 2024. Woefully underqualified but eager enough to learn, nabbing both a [URF](https://cs.uwaterloo.ca/current-undergraduate-students/research-opportunities/undergraduate-research-fellowship-urf) and [USRA](https://uwaterloo.ca/student-awards-financial-aid/awards/nserc-undergraduate-research-awards) was enough to convince [Yizhou Zhang](https://cs.uwaterloo.ca/~yizhou/) to supervise me. To gain background in compilers and PL work, I took CS444 during the term and also audited CS442. `joosc` is the name of the Joos1W compiler I and two other group members built over those four months.

  Joos1W is a subset of the Java Language Specification (2nd Edition) that notably (among other things) omits:
  - Nested classes
  - Exceptions
  - Private anything
  - do-while/switch/break/continue
  - Floats

  Essentially, it contains just enough to make parsing, name disambiguation, type linking and checking, dataflow analysis, inheritance, and virtual functions difficult to implement. It also makes you hate array `length`.

  Both of my team members wanted to build `joosc` in Rust. I, knowing zero Rust, agreed immediately, precisely because I knew zero Rust. Four months later it became my favourite language and easily the one I am most comfortable in. That's right, this heading was really just an excuse to talk about Rust.

+ **[Constructor](): A UW-themed Settlers of Catan clone**

  Also a three-person job, built in C++ for my CS246 final project in Spring 2022. Runs completely on the command line with a text-based GUI. Catan, but with a lot more geese.

* * *

### Contact

+ e-mail: `e224wang (AT) uwaterloo (DOT) ca`

* * *
