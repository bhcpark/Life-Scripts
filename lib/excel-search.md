---
categories:
- code
date: "2017-11-08"
tags:
- excel
- python
title: Search strings in Excel
---

Using XLRD module, search strings in excel file

<!--more-->

```python
from xlrd import open_workbook
book = open_workbook(workbookName)
for sheet in book.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
            if cell.value == "particularString" :
                print sheet.name
                print colidx
                print rowidx
```