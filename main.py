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

def main():
    with open('test.txt', encoding="utf-8") as f:
        test_read = f.read()
    print(test_read)
    # I'm not fond of the string.method.method thing going on here.
    # It's just a lot of function composition happening on one line.
    # (Which is fine.)
    # First step is a find-replace to convert double blank lines to singles.
    # Second splits based on double blank lines.
    test_split = test_read.replace('\n\n\n','\n\n').split('\n\n')
    # Looking at documentation, the method splitlines is interesting.
    print(len(test_split))
    for x in test_split:
        print("---")
        print(x)
        print("---")

main()