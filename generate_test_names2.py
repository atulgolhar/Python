#!/usr/bin/env python
#generate_test_names2.py

#ingests forenames.txt and surnames.txt
#creates test-names2.txt with random new names and related year

import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"), (surnames, "data/surnames.txt")):
        with open(filename, encoding="utf8") as file:
            for name in file:
               names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
with open("test-names2.txt", "w", encoding="utf8") as file:
    limit = 30
    years = list(range(1970, 2013)) * 3
    for year, forename, surname in zip(random.sample(years, limit), random.sample(forenames, limit), random.sample(surnames, limit)):
        name = "{0} {1}".format(forename, surname)
        file.write("{0:.<25}.{1}\n".format(name, year))
