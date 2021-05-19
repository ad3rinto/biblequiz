#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:26:12 2020

@author: aaderinto
"""
import csv
import random
import sys

no_of_tries = 5
attempts = 0
score = 0

name = input("Please enter your name: ")

infile = sys.argv[1]
data = open(infile)
question_prompts = list(csv.reader(data))
random.shuffle(question_prompts)
for questions in question_prompts:
    if attempts < no_of_tries:
        print()
        print(questions[0])
        print("a", questions[2])
        print("b", questions[3])
        print("c", questions[4])
        print("")
        answer = input("Please enter your answer here: ").upper()
        print("")
        attempts = attempts + 1
        if answer == " ":
            break
        elif answer == questions[5]:
            score = score + 1
print(name, "you scored a total of ", score, "out of 5")
print("Thank you for playing")
data.close()
