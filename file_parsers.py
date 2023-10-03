# This is where writing up dirtest.py was helpful.
# Two functions here: odt_parse and txt_parse.  They split up the doc into
# individual powers, which get handed to power parse.  Also tracks ID.

from odf import text, teletype
from odf.opendocument import load
from disc_parsers import disc_parse

def odt_parse(file, ID):
    doc = load(file)
    paragraphs =  doc.getElementsByType(text.P)
    holding = []
    for para in paragraphs:
        holding.append(teletype.extractText(para))
    disc = "\n".join(holding)
    # you know at this point it just is whatever I'd get out of text parse,
    # practically.  disc_parse(disc, ID), which just works on that string?
    return disc_parse(disc, ID)

def txt_parse(file, ID):
    with open(file, encoding="utf-8") as f:
        disc = f.read()
    return disc_parse(disc, ID)

