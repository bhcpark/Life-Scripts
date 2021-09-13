---
categories:
- code
date: "2018-02-02"
tags:
- OneNote
- Anki
- Python
title: OneNote to Anki
---

Use Python to create flashcards in Anki from OneNote.

<!--more-->

Used Anki so much but was always siloed from Onenote which I use a lot for writing and textbooks. I finally got comfortable enough with Python to go into one of the add-ons (import from onenote) and tweak it so my notes could be parsed into flashcards! the key was changing the following code


```python
 # Build the format that the Anki importer can parse.
        output = ''
        table = self.soup.find('table')
        for row in table.findAll('tr', recursive=False):
            tds = [td for td in row.findAll(recursive=False, limit=3)]
            question = self._strip_newlines(tds[0].renderContents())
            answer = self._strip_newlines(tds[1].renderContents())
            note = self._strip_newlines(tds[2].renderContents())
            output += '%s\t%s\t%s\n' % (question, answer, note)
        return output
```

into

```python
# Build the format that the Anki importer can parse.
        output = ''
        table = self.soup.find('table')
        for row in table.findAll('tr', recursive=False):
            tds = [td for td in row.findAll(recursive=False, limit=14)]
            Answer = self._strip_newlines(tds[0].renderContents())
            Topic = self._strip_newlines(tds[1].renderContents())
            Q1 = self._strip_newlines(tds[2].renderContents())
            Q2 = self._strip_newlines(tds[3].renderContents())
            Q3 = self._strip_newlines(tds[4].renderContents())
            Q4 = self._strip_newlines(tds[5].renderContents())
            Q5 = self._strip_newlines(tds[6].renderContents())
            Q6 = self._strip_newlines(tds[7].renderContents())
            Q7 = self._strip_newlines(tds[8].renderContents())
            Q8 = self._strip_newlines(tds[9].renderContents())
            Q9 = self._strip_newlines(tds[10].renderContents())
            Q10 = self._strip_newlines(tds[11].renderContents())
            Link = self._strip_newlines(tds[12].renderContents())
            NoteID = self._strip_newlines(tds[13].renderContents())
            output += '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (Answer, Topic, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Link, NoteID)
        return output
```

This was really thanks to getting an idea of beautifulsoup/regex from my boltbus and MAC hour project. Mac hour I sort of got used to pandas dataframe. AHK also getting an idea for regex.