# -*- coding: utf-8 -*-
import json
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open("chinese6_midterm.html", "r", encoding="utf-8") as f:
    c = f.read()

idx = c.find('"quiz"')
if idx != -1:
    print("chinese6_midterm.html quiz sample:")
    print(c[idx:idx+800])
