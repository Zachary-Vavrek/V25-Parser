# V25-Parser
Text parser for VtM Homebrew with dreams of becoming more.

## Description
This is originally written as Personal Project 1 for
[Boot.dev](https://www.boot.dev/)'s Backend Development Track.  Hopefully, it
grows to be something more.

The intent is to be a digital assistant for building and updating character
sheets in my friend's homebrew Vampire: the Masquerade campaign.  As the rules
are some combination of VtM 20th Anniversary Edition and V5, I've taken to
calling it V25.

The initial goal is a text parser which converts the large quantity of
information currently stored as a collection of .odt files into something
more usable.  (Take each Discipline power description, parse the block of
text, and write a single row in a spreadsheet based on that.)  The longterm
goal is to make a World of Darkness equivalent to
[Chummer](https://github.com/chummer5a/chummer5a/).

## Roadmap
As I update the project, I'll note down which milestones have been hit.

### Foundational Steps
* ~~Open and read literally any file.  I haven't done this in Python yet.  Do
something on the basis of the contents of that file.~~ DONE
* ~~Write a new file.  Make a program that has any kind of output other than
to the screen.~~ DONE
* ~~Investigate opening / reading / writing OpenDocument format files, namely
.odt and .ods files.  Determine if there is an option to ignore text formatting
when reading from .odt.  Run some test cases.  Write some .ods files.~~ DONE
* ~~For the files in question, find out if the newline characters are \cr\lf or
what.  Separately, make a few trial runs to make sure various newline
options work fine.  This seems like a small detail which might be a headache.
Become familiar with this small detail.~~ DONE (There aren't newline
characters, I think, in these files.  Each line is enclosed in `<text:p\>`
tags.)
* ~~NEW: Do basic handling of arguments, specify input file or files, output
file.  Prompt for overwrite confirmation if output file already exists.~~ DONE

### Intermediate Goals
* Read in a single Discipline file and split it to multiple .txt files based
on content, as a proof of concept.  For example, Auspex.odt would produce
Auspex\Rank 1\Heightened Senses.txt (along with all the rest).
* Read in a sample Discipline file (perhaps a truncated version of a full file)
and write each power to a row in a .ods file.  Only as I write this goal does
the notion of appending rows to the bottom of a spreadsheet come to me, versus
rewriting the whole thing each time or ... I just hadn't given it much thought
yet.  (It's all in the 'Investigate' goal up in Foundational Stesp.)
* Read in multiple Discipline files (either given as a list or simply
'everything in this directory'?) and compile information to a single output
file.

### Here Be Dragons
* Some kind of representation of a character, so that the cost of any given
Discipline power can be calculated, as well as a simple list of what powers
are available for purchase (given clan, bloodline, instruction).
* A full character sheet, with both construction and campaign phases.
* Modular rules support: let there be a rules module for building a character
under this V25 system, a standard V20 or V5 or VtM: Revised module, modules for
other character types, etc.
* Experience point cost is probably too-often tweaked to go into the relatively
static module, and instead should be something in a settings page somewhere.
* If I or someone else wants to do a lot of data entry work, Merits, Flaws,
Backgrounds, etc. could all be incorporated.

## Intermediate Goal In Detail
At the moment, all Discipline powers are available to me in .odt files, each
written with a very regular formatting:

\[dots\] Name of Power  
(Optional) **Amalgam:** Other disciplines required.  (For combo disciplines.)  
(Optional) **Prerequisite:** Specific earlier powers required.  
(Optional) **Requirement:** Clan or Bloodline requirement for rare powers.  
\[Fluff description of the power.\]  
**System:** \[System description of the power.\]  

And then a blank line.  The goal is to convert each of these entries into a row
on a spreadsheet, with something like the following as columns:

* ID (an integer used for reference)
* Name (of the power, for example Malleable Visage)
* Discipline (which Discipline the power is from)
* Rank (what level the power is; possibly a redundant column, unsure)
* Amalgam (values: AND, OR, and Null or blank; some powers require this AND
that, while some require this OR that)
* Prerequisite (name of the prerequisite power, if any)
* Prereq ID (ID number of the prereq power; maybe 0 if none?)
* Requirement (the string of text following 'Requirement: ' if that line is
present)
* Description (the string of text between the name and the system)
* System (the string of text following 'System: ' and before the blank line)
* Then eleven columns representing what levels of which disciplines are
required, in order to support amalgam powers.  For example, Arcane Sight is a
rank 2 Auspex power which requires Blood Sorcerery 1, and so it would have a
2 in the Auspex column and a 1 in the Blood Sorcery column.  This is why 'Rank'
is probably redundant, but harmlessly so.

I designed a spreadsheet with approximately that layout a year ago and the
problem with playing a caitiff when your friend-for-twenty-years Storyteller
decides to take every power, including the Kuei-jin powers, and put them into
a single coherent framework, is that there's about three hundred powers just
when looking at levels 1 through 3.  (About a hundred of them have Requirement
lines.  Still!  That's so many.)  The regularity of the power blocks motivated
me to learn how to parse text, because I can *describe* the rules needed with
exact detail.  But, when I looked a year ago, there were no good introductory
explanations of how to build the sort of text parser into which I could put
those rules.

And so, I come to this.