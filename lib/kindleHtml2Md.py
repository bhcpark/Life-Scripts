import re
from bs4 import BeautifulSoup

save_dir = "" #destination folder
source_file = '' #html path

# refs
# https://diegosegura.me/kindle2notion

def remove_chars(s):
    """
    from https://github.com/robertmartin8/KindleClippings/blob/master/KindleClippings.py
    This is a utility function that removes special characters from the string, so that it can
    become a valid filename.
    :param s: input string
    :return: the input string, stripped of special characters
    """
    # Replace colons with a hyphen so "A: B" becomes "A - B"
    s = re.sub(" *: *", " - ", s)
    # Remove question marks or ampersands
    s = s.replace("?", "").replace("&", "and")
    # Replace ( ) with a hyphen so "this (text)" becomes "this - text"
    s = re.sub(r"\((.+?)\)", r"- \1", s)
    # Delete filename chars tht are not alphanumeric or ; , _ -
    s = re.sub(r"[^a-zA-Z\d\s;,_-]+", "", s)
    # Trim off anything that isn't a word at the start & end
    s = re.sub(r"^\W+|\W+$", "", s)
    return s


def writeNotes(notes_soup):
    fn = save_dir + "{" + remove_chars(bookTitle) + "}.md"
    notebook = open(fn,"a",encoding="utf8")
    notebook.write('- Author:[[@' + bookAuthor + ']]\n---\n')
    #set lastline 
    lastline = ''
    for item in notes_soup:
        if item['class'][0] == "sectionHeading":
            #chapter/section
            notebook.write('## ' + item.contents[0].strip() + '\n')
            print(item.contents)
        elif item['class'][0] == 'noteHeading':
            #all notes/highlights start w/ noteHeading"
            #record if it was NOTE or HIGLIGHT
            if "Highlight" in item.get_text():
                note_counter = 0
            else:
                note_counter = 1
            # get text to right of 'higlight or note - '
            line = item.get_text().partition(' - ')[2]
            #get text to left of ' > Location'
            line = line.partition(' >')[0]
            #record last line so it doesn't create duplicates
            #create sub-section
            if lastline == line:
                continue
            else:
                notebook.write('### ' + line + '\n')
                lastline = line
        elif item['class'][0] == 'noteText':
            #this should be text or higlight
            if note_counter == 1:
                #if note, make it bullet point
                notebook.write('- ' + item.string.strip() + '\n\n')    
            else:
                #assume it will be highlight
                notebook.write('> ' + item.string.strip() + '\n\n')

with open(source_file, encoding='utf8') as sf:
    soup = BeautifulSoup(sf, 'html.parser')
    # Title
    bookTitle = soup.find("div", {"class": "bookTitle"}).string.strip()
    # Author
    bookAuthor = soup.find("div", {"class": "authors"}).string.strip()
    # Notes
    notes_soup = soup.find_all(True, {'class':['sectionHeading', 'noteHeading', 'noteText']})
    writeNotes(notes_soup)
    print("done")