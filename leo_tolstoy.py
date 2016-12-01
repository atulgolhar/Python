#!/usr/bin/env python3
#leo_tolstoy.py
import re

record = "Leo Tolstoy*1828-8-28*1910-11-20"
fields = record.split("*")
print(fields)

name = fields[0].split("-")
print(name)

born = fields[1].split("-")
print("born", born)

died = fields[2].split("-")
print("died", died)

print("lived about", (int(died[0]) - int(born[0])), "years")
