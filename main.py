"""There's such a thing as a docstring and I'm not sure when to make one."""


# This is the initial testing grounds for the foundational steps laid out
# in the roadmap included in the readme.  Code which accomplishes its
# initial goals may be preserved for a bit by being cleaned up and
# commented out.  Relevant study notes will be written as I learn what I'm
# doing, and will be condensed to explain the commented-out code.

# Per Python documentation (7.2, Input and Output, Reading and Writing Files),
# open() takes as arguments filename, mode (read, write, both, append; defaults
# to read), and encoding.

# Ah, good: "In text mode, the default when reading is to convert
# platform-specific line endings (\n on Unix, \r\n on Windows) to just \n."

# Strong recommendation here to use the `with` keyword.


# Condensed version of reading:
# Use a with to handle the initial reading step, as in:
# def main():
#     with open('test.txt', encoding="utf-8") as f:
#         test_read = f.read()
#     print(test_read)
#
# Perhaps include an error check after this to see if the file was closed.
# string.replace('\n\n\n','\n\n') will change all double blank lines to
# singles, appending .split('\n\n') at the end will split a string on all
# double or single blank lines.

# Now to write something.

# from os.path import exists

# def main():
#     # I am immediately concerned about "how do I make a new file but stop
#     # if the file already exists?" because the documentation I was looking at
#     # didn't detail that situation.  The open() documentation does, though!
#     # with open('write_test.txt', 'x', encoding="utf-8") as f:
#     #     f.write("Test: Write?")
#     # This should work the first time and fail somehow the second time.
#     # Learn by doing.
#     # Alright, that does what it says on the tin.  Commenting out.

#     # There should be a better way of handling it when there's already a file.
#     # Print a complain to the screen, but not in a 'oh no the program failed'
#     # way.  I want some way of checking if the output is there already.
#     # This would allow for prompting "overwrite? y/n" for instance.
#     with open('test.txt', 'r', encoding="utf-8") as f:
#         test_read = f.read()
#     if exists('write_test.txt'):
#         print("Output file already present, stopping.")
#         returns
#     test_split = test_read.replace('\n\n\n','\n\n').split('\n\n')
#     with open('write_test.txt', 'a', encoding="utf-8") as f:
#         f.write(test_split[1])

# What happens if I just use regular open() on an odt file?
# Learn by doing.
# Answer: utf-8 encoding chokes.

# I find the status of dealing with ODF files enraging.
# I generally find it enraging any time there are details left unexplained.

# Using odfpy.  Some headache about learning what's going on with venv stuff.
# This pulls out each paragraph and reconstructs structure, though.

# from odf import text, teletype
# from odf.opendocument import load

# # Why the .opendocument?

# def main():
#     doc = load("Test doc.odt")
#     print("holding")
#     paras = doc.getElementsByType(text.P)
#     print(paras)
#     print("holding")
#     holding = []
#     for para in paras:
#         holding.append(teletype.extractText(para))
#     print("holding")
#     print(holding)
#     thing = "\n".join(holding)
#     print(thing)
#     print("holding")
# main()

# Next step: writing a spreadsheet.  Looking at the following example:
# https://github.com/eea/odfpy/blob/master/examples/passwd-as-ods.py
# ... so much of this is about styling the information, which is uninteresting.

# from odf.opendocument import OpenDocumentSpreadsheet
# While attempting to figure out what else to do here, and how to do it, I
# have instead found out about Python-UNO, and am going down a different
# rabbit hole of "trying to find the official API" ...

# Alternately, Pandas?  Whatever Pandas is?  Pandas seems to support reading
# .ods files but not writing them.  Awkward.  Making some kind of csv file
# with an unusual delimiter seems like it might be the most convenient,
# certainly.

# Pandas seems like the best tool (certainly the best documented tool), but so
# much of its documentation is talking about situations other than mine.
# At least it's not enraging.

# DataFrames seem like I can treat them as somewhat equivalent to a sheet in a
# spreadsheet workbook, which means they're vastly more complicated than what
# I need right now.

# From Wikipedia, the Sator Square:

# S A T O R
# A R E P O
# T E N E T
# O P E R A
# R O T A S

# import pandas as pd

# def main():
#     test_array = [
#         ['S', 'A', 'T', 'O', 'R'],
#         ['A', 'R', 'E', 'P', 'O'],
#         ['T', 'E', 'N', 'E', 'T'],
#         ['O', 'P', 'E', 'R', 'A'],
#         ['X', 'O', 'T', 'A', 'S'],
#     ]
#     print("holding")
#     print("array:")
#     print(test_array)
#     test_df = pd.DataFrame(test_array)
#     print("data frame:")
#     print(test_df)
#     output_file = "test.ods"
#     test_df.to_excel(excel_writer = output_file, header=False, index=False)
#     # Excellent, this does just give me an ods file, formatted like I want.
#     # Ish.  Like I want-ish.  Setting header and index to false removes those,
#     # giving me just a 25-element set of single-char strings in the sheet.

#     # Can I append things to the bottom?  Aha, there's the example.
#     test_array = [
#         ['S', 'A', 'T', 'O', 'R'],
#         ['A', 'R', 'E', 'P', 'O'],
#         ['T', 'E', 'Y', 'E', 'T'],
#         ['O', 'P', 'E', 'R', 'A'],
#         ['X', 'O', 'T', 'A', 'S'],
#     ]
#     test_df = pd.DataFrame(test_array)
#     # with pd.ExcelWriter(output_file, mode='a') as writer:
#     #     test_df.to_excel(writer, header=False, index=False)
#     # Update: Cannot append to an odf.  Alas.
# main()

# Recap: If nothing else, I can build an array, a list of lists, according to
# a columnar framework I set out ahead of time, convert that to a DataFrame,
# and then export that to a .ods file.
# I keep smelling some kind of cleaning fluid and it's irritating my eyes.
# If I can use Pandas (pandas?  Unsure standard for capitalization) to open
# the .odt files, then the bulk of the work is just in specifying and
# implementing all the step-by-step text processing rules.

# Didn't I plan on developing some kind of habit of manual hyphenation when I
# wrote comments?  I keep just starting a new line when I think my current word
# will be too long.

# Pandas is all about well-structured data.  But I can read stuff in with odfpy
# and write it out with pandas.  Transformation happens within Python.

import pandas as pd
from odf import text, teletype
from odf.opendocument import load

def main():
    doc = load("Test doc.odt")
    paras = doc.getElementsByType(text.P)
    holding = []
    for para in paras:
        holding.append(teletype.extractText(para))
    thing = "\n".join(holding)
    split_thing = thing.replace('\n\n\n','\n\n').split('\n\n')
    test_df = pd.DataFrame(split_thing)
    output_file = "test.ods"
    test_df.to_excel(excel_writer = output_file, header=False, index=False)
    # Once I realized I already had test.ods open in another window, and needed
    # to close and reopen it in LibreOffice Calc, this worked perfectly.
    # That took me a good minute or three, though.
main()