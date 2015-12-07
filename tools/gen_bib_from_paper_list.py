#!/usr/bin/env python

# system modules
import os
import sys


class Example(object):
        def __init__(self):
                pass

prefix="""
@article{,
title={{
"""
surfix="""
}},
journal={ndss},
year={2016},
}
"""

def main():
        if len(sys.argv) != 3:
                print "Usage: \t" + sys.argv[0] + " <paper list>  <output file>"
                sys.exit(-1)

        PAPER_LIST = sys.argv[1]
        OUTPUT_FILE = sys.argv[2]

        fd = open(OUTPUT_FILE, "w+")
        for line in open(PAPER_LIST):
                line = line.strip()
                line = prefix + line  + surfix
                print line

                fd.write(line)
        fd.close()


if __name__ == "__main__":
        main()
