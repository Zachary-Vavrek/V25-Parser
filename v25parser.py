# I always say I finally learned how to program in Doug Hall's Microprocessors
# class, because the class projects involved writing ARM Assembly code.
# What Dr. Hall said, and what the experience hammered home, is that you need
# to know what you're doing before you actually start writing your code.
# This is true in Assembly because every line is such a small thing, an
# individual thread in a tapestry.  But even if it's not required in other
# languages, it's still incredibly helpful.

# So, an outline:
# This file, the actual v25parser, holds main().  It calls ... other things.
# main() handles file names, directories, that sort of thing?
# A function somewhere: disc_parse(), which parses the actual block of text
# and which returns probably a list of strings which will be turned into a row
# in the output spreadsheet.
# Two functions: txt_parse() and odt_parse(), which handle opening / reading
# files and which then call disc_parse().  So, call odt_parse on a single odt
# file, get back ... a list of lists of strings, which can be appended to a
# growing list-of-lists-of-strings (every discipline).  Once all files are
# read, this full grown list is turned into a data frame and written.  That
# probably happens in main()?  It might not.

# argparse for argument parsing.
import argparse

# pandas for writing a spreadsheet file.
import pandas as pd
from os import listdir
from os.path import isdir, exists, join, isfile
from file_parsers import odt_parse


def main():
    # The opening here creates two (sets of) arguments, input (1 to n) and
    # output (1; apparently it breaks if I give it 2).
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input',
        nargs='+',
        required=True
    )
    parser.add_argument(
        '-o', '--output',
        required=True
    )
    args = parser.parse_args()

    # If there are multiple inputs and they aren't all just files, stop.
    if len(args.input) > 1 and any(isdir(x) for x in args.input):
        print("Input takes either multiple files or a single directory.")
        return

    # If the output file prompt for overwrite confirmation.
    if exists(args.output):
        choice = input("Output file present.  Overwrite? (y/N): ")
        if not (choice == 'y' or choice == 'Y'):
            return

# NOTE: what happens if I give pandas' ExcelWriter a filename without an
# extension?  Test that out.  Also, note turned blue when I wrote it in caps.
# Does that always happen?
# TESTING: no.
# Note: no
# NOTE just this, in blue.

    # I don't know if I need to initialize `files` as an empty list before
    # filling it.  It feels like good practice?  It's a holdover from C.
    files = []

    # If a directory was given as input, fill the files list with the paths to
    # all the files in that directory.  Otherwise, fill the files list with the
    # input filenames given.
    if isdir(args.input[0]):
        files = [
            join(args.input[0], f) for f in listdir(args.input[0]) if (
                isfile(join(args.input[0], f)) and f[0] != "."
                )
            ]
    else:
        files = args.input
    print(files)
    files.sort()
    print(files)
# Next up I think there's something that's broadly "for each file in files,
# call file_parse on that file and append the output to a running compilation
# of all the stuff."  I think figuring that out means figuring out all the
# stuff, though, right?

# What are my column headers?  Comma separated:
# ID, Name, Discipline, Rank, Amalgam, Prerequisite, Prereq ID, Requirement,
# Description, System, Animalism, Auspex, Blood Sorcery, Celerity, Dominate,
# Fortitude, Obfuscate, Oblivion, Potence, Presence, Protean

# In order to track ID, ID needs to be handled in main(), unless I'm passing
# everything, right?  Or main() just calls another function in here.  Like,
# whateveroutput = function(files), then convert the whatever to a DataFrame
# and then to ods?  That works.  Yeah.

    # Creates a list of lists, arranged so that it can be converted to a
    # DataFrame and then written as a spreadsheet file.
    discipline_table = table_builder(files)

    discipline_df = pd.DataFrame(discipline_table)
    discipline_df.to_excel(
        excel_writer = args.output, header=False, index=False
        )

def table_builder(files):
    output_table = [
        ["ID",
         "Name",
         "Discipline",
         "Rank",
         "Amalgam",
         "Prerequisite",
         "Prereq ID",
         "Requirement",
         "Description",
         "System",
         "Animalism",
         "Auspex",
         "Blood Sorcery",
         "Celerity",
         "Dominate",
         "Fortitude",
         "Obfuscate",
         "Oblivion",
         "Potence",
         "Presence",
         "Protean"]
    ]
    # Column numbers:
    # 0   ID
    # 1   Name
    # 2   Discipline
    # 3   Rank
    # 4   Amalgam
    # 5   Prerequisite
    # 6   Prereq ID
    # 7   Requirement
    # 8   Description
    # 9   System
    # 10  Animalism
    # 11  Auspex
    # 12  Blood Sorcery
    # 13  Celerity
    # 14  Dominate
    # 15  Fortitude
    # 16  Obfuscate
    # 17  Oblivion
    # 18  Potence
    # 19  Presence
    # 20  Protean

    ID = 1
    # Then ... for file in files, call relevant file-parser and append output?
    for file in files:
        disc = []
        # if file odt, call odt parser
        # it's not like I have a txt parser
        if file[-4:] == ".odt":
            disc, ID = odt_parse(file, ID)
            output_table.extend(disc)
        elif file[-4:] == ".txt":
            # disc, ID = txt_parse(file, ID)
            # output_table.append(disc)
            print(".txt parser not implemented yet.")

    return output_table

main()