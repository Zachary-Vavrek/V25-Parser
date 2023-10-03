# I forgot to do one of my basic intermediate steps.
# I forgot it because it's not that important and is mostly a sideshow.

import re
from os import listdir, makedirs
from os.path import join, isfile
from odf import text, teletype
from odf.opendocument import load

def main():
    indir = "./test files/disc"
    outdir = "./test files/disc/out"
    files = [join(indir, f) for f in listdir(indir) if isfile(join(indir, f))]
    for f in files:
        write_text_files(f, outdir)

def write_text_files(disc_file, outdir):
    doc = load(disc_file)
    paragraphs = doc.getElementsByType(text.P)
    holding = []
    for para in paragraphs:
        holding.append(teletype.extractText(para))
    full_disc = "\n".join(holding).replace('\n\n\n','\n\n').replace('• •','••')
    split_disc = full_disc.split('\n\n')
    split_disc = list(filter(None, split_disc))
    disc_name = split_disc[0].split('\n')[0]
    disc_folder = outdir + "/" + disc_name
    makedirs(disc_folder, exist_ok=True)
    file_name = disc_folder+"/"+disc_name+".txt"
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(split_disc[0])
    for item in range(1,len(split_disc)):
        power = split_disc[item].split('\n')[0].split(' ', maxsplit=1)
        folder = disc_folder+"/"+"Rank " + str(len(power[0]))
        makedirs(folder, exist_ok=True)
        powername = re.sub(r'[^\w_. -]', '_', power[1].strip())
        filepath = folder+"/"+ powername + ".txt"
        with open(filepath, 'w', encoding="utf-8") as f:
            f.write(split_disc[item])
    # print("does any of this work?")
    # print("I mean really.")
    # print("I should ever call main.")

main()

# A sideshow, but one that was helpful to do!
# idea: split on two newlines then a dot, but then, every time I do something
# with a split_disc item, make the string-being-worked-on dot+item.