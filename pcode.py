#!/bin/python

from parser import parse
from sys import argv


def print_help():
    print("pCode")
    print("-" * 40)
    print("A useless codegolfing language")
    print("\nUsage:")
    print(f"{argv[0]} <file>")


if __name__ == '__main__':
    if len(argv) == 1:
        print_help()
        exit(0)

    data = "".join(open(argv[1]).readlines())
    parse(data)
