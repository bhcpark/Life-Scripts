---
categories:
- code
date: "2018-01-18"
tags:
- parse
- python
- rank list
title: Parse NRMP from ERAS for rank list
---

Pull NRMP codes for ERAS rank list
<!--more-->

As of 2018,  residency application process is complicated by fractionated interview scheduling process, it makes the rank list even more tedious. Currently, we can either search programs manually or enter in the program code. Why hasn't NRMP created a way to communicate directly from ERAS and pull the data?

Enter a 4th year, bright-eyed medical student (*that's me!*) eager to learn programming and saw this as a brilliant opportunity to practice daily coding. The following is a simple code to pull NRMP program code from all applied list on ERAS. I considered parsing the webpage, but opted for using a clipboard method to preserve confidentiality. 

###Instructions
1. Navigate to ERAS 'Programs applied to' page and copy whole page to clipboard.
2. Run code!

```python
#Created on 1/28/18 by Brian Park.
import re, pyperclip
#copying text from 'Programs Applied to' on ERAS. 
text = pyperclip.paste()
#find 9 digit code, with 8th character being a letter (usually 'A','C', or 'P')
s = re.findall('\d{7}[A-Za-z]\d', text)
#print each code as separate line
for code in s:
    print(p)
```

###Future features
Have the parser grab the program details and prompt if you interviewed at this place. Then the program will only print out list of programs you are eligible to rank! (Although you can technically rank any program)