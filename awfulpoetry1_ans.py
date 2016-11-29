#!/usr/bin/env python3

#awfulpoetry1_ans.py
#Loop five times and on each iteration use random.choice() function 
#and random.randint() function to choose sentence structure,
#three sentence structure (article, subject, verb) or  
#four (article, subject, verb and adverb)

import random

articles = ["the", "a", "an", "his", "her", "their"]
subjects = ["cat", "dog", "man", "woman", "boy", "girl", "animal"]
verbs = ["sang", "ran", "jumped", "flew", "ate", "saw", "carried"]
adverbs = ["loudly", "quietly", "well", "badly", "nicely",
            "intensely", "quickly", "slowly", "meanly", "rudely"]

for _ in [1, 2, 3, 4, 5]:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    if random.randint(0,1) == 0:
        print(article, subject, verb)
    else:
        print(article, subject, verb, adverb)
