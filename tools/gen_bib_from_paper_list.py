#!/usr/bin/env python

# system modules
import os
import sys
import re


class Example(object):
        def __init__(self):
                pass

FORMAT_STR = '@ARTICLE{,\n' + \
             'author = "%s",\n' + \
             'title = "%s",\n' + \
             'journal = "NDSS",\n' + \
             'year = "2016"\n}\n'

def main():
        if len(sys.argv) != 3:
                print "Usage: \t" + sys.argv[0] + " <paper list>  <output file>"
                sys.exit(-1)

        PAPER_LIST = sys.argv[1]
        OUTPUT_FILE = sys.argv[2]

        input_fd = open(PAPER_LIST)
        output_fd = open(OUTPUT_FILE, "w+")

        all_lines = input_fd.readlines()
        i = 0
        while i < len(all_lines):
                title = all_lines[i].strip()
                title = title.replace('"', '\'')
                authors = all_lines[i + 1].strip()

                # authors = filter(None, authors.split(","))
                authors = [x.strip() for x in authors.split(",") if x.strip()]
                new_authors_list = []

                for each_author in authors:
                        each_author_list = each_author.split()
                        each_author_list = [x.strip() for x in each_author_list if x.strip()]
                        if len(each_author_list) <= 1:
                                raise Exception("each_author_list length is less than 1 : " + str(each_author_list))
                        each_author_str = each_author_list[-1] + ", " + " ".join(each_author_list[:-1])
                        new_authors_list.append(each_author_str)

                print new_authors_list

                output_fd.write(FORMAT_STR % (" and\n".join(new_authors_list), title))

                i += 2

        input_fd.close()
        output_fd.close()


if __name__ == "__main__":
        main()
