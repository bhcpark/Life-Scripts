import pandas as pd
import difflib

file_path = r"D:\Users\Brian\Desktop\temp\kw.xlsx"
index_path = r"D:\Dropbox\indices.xlsx"
df1 = pd.read_excel(file_path, sheet_name='Sheet1')
df2 = pd.read_excel(index_path, sheet_name='Sheet1')
# colm 'kw'


def kwsearch():
    # prompt search
    term = input("Type in search term: ")
    # show col kw where kw contains search term
    res = df1.loc[df1["kw"].str.lower().str.contains(term.lower())]
    if res.empty == True:
        print("no match")
    else:
        print(res)
        print(str(len(res)) + " matches")
        # working on this
        # print(sorted(res, key=lambda x: difflib.SequenceMatcher(None, x, term).ratio()))
    while True:
        print(kwsearch())


def indexsearch():
    # prompt search
    term = input("Type in search term: ")
    # show col kw where kw contains search term
    res = df2[df2["Topic"].str.lower().str.contains(
        term.lower(), na=False)]  # ignore NANs
    if res.empty == True:
        print("no match")
    else:
        print(res.iloc[:, 0:4])
        print(str(len(res)) + " matches")
        # working on this
        # print(sorted(res, key=lambda x: difflib.SequenceMatcher(None, x, term).ratio()))
    while True:
        print(indexsearch())


# add word if not there
def add_kw(term):
    # make sure it's to the end
    row_num = len(df1['kw'])+1
    # add to col 'kw', last row
    df1.set_value('kw', row_num, term)


# to do
#
#

# most common words in results
#Counter(" ".join(res).split()).most_common(4)
# get value at y/x
# df1['kw'][2478]

# search fuzzy
# https://www.datacamp.com/community/tutorials/fuzzy-string-python

# search indices
# index path
# set as df = pd
#structure: references | edition | Topic | Page | ch|p|q

# show if any ACE questions match
# can use powershell..
