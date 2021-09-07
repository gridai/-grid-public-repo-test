#!/usr/bin/env python

print("Hello world")

with open("artifacts.txt", "w") as f:
    print("Hello world", file=f)