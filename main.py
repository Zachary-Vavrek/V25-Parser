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

# def main():
#     with open('test.txt', encoding="utf-8") as f:
#         test_read = f.read()
#     print(test_read)
#     # I'm not fond of the string.method.method thing going on here.
#     # It's just a lot of function composition happening on one line.
#     # (Which is fine.)
#     # First step is a find-replace to convert double blank lines to singles.
#     # Second splits based on double blank lines.
#     test_split = test_read.replace('\n\n\n','\n\n').split('\n\n')
#     # Looking at documentation, the method splitlines is interesting.
#     print(len(test_split))
#     for x in test_split:
#         print("---")
#         print(x)
#         print("---")

# main()

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

from os.path import exists

def main():
    # I am immediately concerned about "how do I make a new file but stop
    # if the file already exists?" because the documentation I was looking at
    # didn't detail that situation.  The open() documentation does, though!
    # with open('write_test.txt', 'x', encoding="utf-8") as f:
    #     f.write("Test: Write?")
    # This should work the first time and fail somehow the second time.
    # Learn by doing.
    # Alright, that does what it says on the tin.  Commenting out.

    # There should be a better way of handling it when there's already a file.
    # Print a complain to the screen, but not in a 'oh no the program failed'
    # way.  I want some way of checking if the output is there already.
    # This would allow for prompting "overwrite? y/n" for instance.
    with open('test.txt', 'r', encoding="utf-8") as f:
        test_read = f.read()
    if exists('write_test.txt'):
        print("Output file already present, stopping.")
        return
    test_split = test_read.replace('\n\n\n','\n\n').split('\n\n')
    with open('write_test.txt', 'a', encoding="utf-8") as f:
        f.write(test_split[1])

main()