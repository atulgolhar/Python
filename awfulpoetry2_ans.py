#!/usr/bin/env python3

#awfulpoetry2_ans.py 
import sys
import random

articles = ["the", "a", "an", "his", "her", "their"]
subjects = ["cat", "dog", "man", "woman", "boy", "girl", "animal"]
verbs = ["sang", "ran", "jumped", "flew", "ate", "saw", "carried"]
adverbs = ["loudly", "quietly", "well", "badly", "nicely",
            "intensely", "quickly", "slowly", "meanly", "rudely"]

lines = 5 #default

if len(sys.argv) > 1:
    try:
        temp = int(sys.argv[1])
        if 1 <= temp <= 10:
            lines = temp
        else:
            print("Note: number of lines must be 1-10 inclusive")
    except ValueError:
        print("ValueError usage: badpoetry.py [input lines]")

while lines:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    if random.randint(0,1) == 0:
        print(article, subject, verb)
    else:
        print(article, subject, verb, adverb)
    lines -= 1
