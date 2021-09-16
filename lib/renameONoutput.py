import re, os, os.path
from datetime import datetime
from os import path

# OneNote Headings:
# title of document (not always correct date)
#
# Weekday, Month Day, Year
regex = re.compile(',\s(?P<month>[a-zA-Z]+)\s(?P<day>\d{1,2})\W+(?P<year>\d{4})') 

#directory with markdown files
dir_path = r""  #add here!

def convert(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for a_file in files:
            p = os.path.join(root,a_file)
            #pesky encoding errors.
            with open(p,"r", encoding="utf-8", errors='ignore') as f:
                lines = f.readlines()
                a = "".join(lines)
                f.close()
            r = re.search(regex,a)
            m = datetime.strptime(r.group('month'),"%B")
            m = m.strftime("%m") 
            d = datetime.strptime(r.group('day'),"%d")
            d = d.strftime('%d')
            y = r.group('year')
            fname = y + "-" + m + "-" + d + ".md"
            #rr = "\\".join(root.split("\\")[:-1])
            print(fname)
            # some cleanup
            z = re.sub(' {2,}', ' ',a)
            z = re.sub('\n{3,}','',z)
            zz = z.encode("ascii","ignore")
            text = zz.decode()
            # append if file exists
            if path.exists(dir_path + "\\" + fname):
                with open(dir_path + "\\" + fname,"a") as f:   
                    f.write(text)
                    f.close()
            # otherwise create new
            else:
                with open(dir_path + "\\" + fname,"w+") as f:
                    f.write(text)
                    f.close()