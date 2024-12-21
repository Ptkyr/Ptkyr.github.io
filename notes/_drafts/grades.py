#!/usr/bin/env python3

import csv
import json
import textwrap
from statistics import mean

SPACE = " "

csv_file = "./grades.csv"

TERMS = ["1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B"]


def xValue(course):
    if not course["Term"]:
        return course
    ret = TERMS.index(course["Term"])
    if course["Coop"] == "Y":
        ret += 0.5
    course["x"] = ret
    return course


def fullCode(course):
    return course["Subject"] + course["Code"]


def indent(string, level=12):
    return textwrap.indent(string, SPACE * level)


with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)

    by_subject = {
        "CS": [],
        "(P)MATH": [],
        "CO": [],
        "CHEM": [],
        "ENGL": [],
        "STAT": [],
        "ECON": [],
    }

    courses = [xValue(row) for row in csv_reader]
    for term in TERMS:
        by_grade = {}
        for course in courses:
            if course["Term"] == term and course["Coop"] == "N":
                if course["Grade"] in by_grade:
                    by_grade[course["Grade"]]["x"] -= 0.1
                    course["x"] += 0.1
                by_grade[course["Grade"]] = course

    for row in courses:
        if row["Subject"] in ["MATH", "PMATH"]:
            by_subject["(P)MATH"].append(row)
        else:
            by_subject[row["Subject"]].append(row)

    for subj, arr in by_subject.items():
        print(indent(f"{{\n    name: '{subj}',\n    data: ["))
        for course in arr:
            if course["Term"]:
                print(
                    indent(
                        f"        {{x: {course['x']}, "
                        f"y: {course['Grade']}, "
                        f"name: '{fullCode(course)}', "
                        f"desc: '{course['Name']}'}},",
                    )
                )
        print(indent("    ]\n},"))

    averages = [
        mean(
            int(x["Grade"]) for v in by_subject.values() for x in v if x["Term"] == term
        )
        for term in TERMS
    ]

    drop_worst = [
        mean(
            sorted(
                [
                    int(x["Grade"])
                    for v in by_subject.values()
                    for x in v
                    if x["Term"] == term
                ]
            )[1:]
        )
        for term in TERMS
    ]

    print(indent(f"{{\n    name: 'Avg',\n    data: ["))
    for i, avg in enumerate(averages):
        print(indent(f"        {{x: {i}, y: {avg:.2f}}},"))
    print(indent("    ]\n},"))

    print(indent(f"{{\n    name: 'Meme',\n    data: ["))
    for i, avg in enumerate(drop_worst):
        print(indent(f"        {{x: {i}, y: {avg:.2f}}},"))
    print(indent("    ]\n},"))
    print(mean(averages))
    print(mean(drop_worst))
