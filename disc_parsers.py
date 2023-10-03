# Okay, here I actually do the heavy lifting.  disc_parse puts together a list
# of lists, tracking ID number as given, for a single discipline file.
# It repeatedly calls power_parse to parse the individual powers, which
# are turned into lists of strings.

def disc_parse(disc, ID):
    # disc shows up just as the raw full text of a discipline file.
    # This line cleans up some inconvenient visual formatting.
    disc = disc.replace('\n\n\n','\n\n').replace('• •','••')

    # This splits disc into a list of strings, each one being a discipline
    # power (a blank line followed by a dot).  It also removes one dot from
    # every first line, which is inconvenient.
    disc = disc.split('\n\n•')

    # This removes any empty strings from the list.
    disc = list(filter(None, disc))

    # This should restore the dot to the front of power names.
    for i in range(1,len(disc)):
        disc[i] = '•'+disc[i]

    # The name of the discipline we're talking about.
    disc_name = disc[0].split('\n')[0]
    print(disc_name)

    # Holder for the output list.
    output = []

    # Given the rework of power_parse to return a dictionary, I think I want
    # a dictionary of column numbers.
    col_num = {
        "ID": 0,
        "Name": 1,
        "Discipline": 2,
        "Rank": 3,
        "Amalgam": 4,
        "Prerequisite": 5,
        "Prereq ID": 6,
        "Requirement": 7,
        "Description": 8,
        "System": 9,
        "Animalism": 10,
        "Auspex": 11,
        "Blood Sorcery": 12,
        "Celerity": 13,
        "Dominate": 14,
        "Fortitude": 15,
        "Obfuscate": 16,
        "Oblivion": 17,
        "Potence": 18,
        "Presence": 19,
        "Protean": 20,
    }
    for i in range(1,len(disc)):
        # Parse what can be got from the power block.
        power_dict = power_parse(disc[i])

        # Prep a list.
        power = [None] * 21

        # Fill the list with known values.
        power[col_num["ID"]] = ID
        power[col_num["Discipline"]] = disc_name

        # Fill the list with values from the power block.
        for k, v in power_dict.items():
            power[col_num[k]] = v

        # Set the current discipline's required level to equal Rank (because
        # the power block can't tell what discipline the power is from).
        power[col_num[disc_name]] = power[col_num["Rank"]]

        # I'm not sure how to find the prerequisite IDs right now.
        # Will give that thought later.

        # Increment ID value.
        ID += 1

        output.append(power)

    return output, ID

def power_parse(power):
    # At this point I realize I need to rethink what's in the power_parse and
    # what's in the disc_parse.
    # What can the power_parse not know?  Discipline name.  Other power names.
    # So Discipline Name needs to be passed in, so that power_parse assigns
    # the correct ... or does it?  Maybe power_parse just splits up the lines?
    # returns what the rank, name, description, amalgam, prereq, system lines
    # are?

    # Rethinking: the information contained in a power block is the above set
    # of whatevers.  Maybe there should be a power class?
    # What am I handing back?  A name.  A rank.  Amalgam powers.  Prereq.  Req.
    # Rank allows the disc_parser to assign the correct other column, because
    # it knows name.

    # Making this output a dictionary so that I can not have to worry about
    # eleven columns.
    output = {}

    # Split the power into individual lines.
    power = power.split('\n')

    # Rank is the number of dots, or: the number of characters before the
    # first space in the first line of the power.
    output["Rank"] = len(power[0].split(' ')[0])

    # Name is the rest of the first line of the power.
    output["Name"] = power[0].split(' ', maxsplit=1)[1]

    # Dweomer Strike has all three: Amalgam, Prerequisite, and Requirement.
    # I'm just assuming they're always in alphabetical order.

    # This is a marker to get checked and moved forward.
    desc_line = 1

    # If there is an amalgam line:
    if power[desc_line].startswith("Amalgam:"):
        # Strip the amalgam prefix off the line.
        amalgam = power[desc_line].removeprefix("Amalgam: ")

        # Move the marker forward.
        desc_line += 1

        # Inward Focus requires three things!  Using a comma as a basic check.
        if "," not in amalgam:
            # Check if it's an 'or' type, split if so.
            if " or " in amalgam:
                amalgam = amalgam.split(" or ")
                output["Amalgam"] = "OR"

            # Check if 'and' type, split if so.
            if " and " in amalgam:
                amalgam = amalgam.split(" and ")
                output["Amalgam"] = "AND"
        elif "," in amalgam:
            if " and " in amalgam:
                amalgam = amalgam.split(" and ")
                output["Amalgam"] = "AND"
            if " or " in amalgam:
                amalgam = amalgam.split(" or ")
                output["Amalgam"] = "OR"
            amalgam = amalgam[0].split(", ") + [amalgam[1]]

        # Using the name of the discipline as a key, add the length of the
        # power dots as the rank.  If there are two disciplines, do both.
        if len(amalgam) == 2 or len(amalgam) == 3:
            for i in range(len(amalgam)):
                output[amalgam[i].rsplit(' ', maxsplit=1)[0]] = (
                len(amalgam[i].rsplit(' ', maxsplit=1)[1])
                )
        else:
            output[amalgam.rsplit(' ', maxsplit=1)[0]] = (
                len(amalgam.rsplit(' ', maxsplit=1)[1])
                )

    # If there is a prereq line:
    if power[desc_line].startswith("Prerequisite:"):
        # Just take in the entire prereq line; should just be a power name.
        output["Prerequisite"] = power[desc_line].removeprefix("Prerequisite: ")

        # Update marker position
        desc_line += 1

    # If there is a requirement line:
    if power[desc_line].startswith("Requirement:"):
        # Also just needs the full line.
        output["Requirement"] = power[desc_line].removeprefix("Requirement: ")

        # Update marker position
        desc_line += 1

    # I'm not sure if the description is ever more than a single line.
    # Wait, there's an example, False Death.
    # Assume the system starts one line later.
    sys_line = desc_line+1
    # Then move the marker forward.
    while not power[sys_line].startswith("System:"):
        sys_line += 1

    # Set the description, from the first line of the description to the last
    # line before the system.
    output["Description"] = '\n'.join(power[desc_line:sys_line])

    # Set the system, from the first line of the system to the end.
    output["System"] = '\n'.join(power[sys_line:])

    return output