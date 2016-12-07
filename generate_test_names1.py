#!/usr/bin/env python
#generate_test_names1.py

#ingests forenames.txt and surnames.txt
#creates test-names1.txt with random new names

import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"), (surnames, "data/surnames.txt")):
        with open(filename, encoding="utf-8") as file:
            for name in file:
                names.append(name.rstrip())
    return forenames, surnames


forenames, surnames = get_forenames_and_surnames()
with open("test-names1.txt", "w", encoding="utf-8") as file:
    for i in range(100):
        line = " {} {}\n".format(random.choice(forenames), random.choice(surnames))
        file.write(line)
        
