# Life Scripts


## Excel
9/2021
* Input search term and retrieve all matching rows from spreadsheet

## OneNote
### Using PowerShell
9/2021<br />
* Windows 10, OneNote 2016 (desktop). Make sure to have powershell and onenote open as administrator
Get OneNote Page contents from specified...
* [Section](/lib/pageContents.ps1) in code
* [search term under specified Section Group](/lib/search.ps1) in code

## [Rename Onenote Markdown Files](/lib/renameONoutput.py)
9/16/2021<br />
**Step 1**. [Convert Onenote to Markdown(https://github.com/SjoerdV/ConvertOneNote2MarkDown). I used the original
version due to issues with pandoc during the conversion. <br />

**Step 2** My garbage in titles led to garbage out file names.<br />
<div align=center>
    <img src="/media/garbage-in.png" style="width: 50%; height: 20%;">
</div>

**Step 3** Run script<br />

**Output**: Renamed markdown files!<br />

<table align=center>
    <tr>
        <td>
            <h3>Before</h3>
        </td>
        <td>
            <h3>After</h3>
        </td>
    </tr>
    <tr>
        <td><img src="/media/filenames-before.png" style="width: 50%; height: 50%;"></td>
        <td><img src="/media/filenames-after.png" style="width: 50%; height: 50%;"></td>
    </tr>
</table>

## [Kindle Highlights to Markdown](/lib/kindleHtml2Md.py)
9/13/2021<br />
**Input**: Kindle app highlights/notes → email to self as Html → save to computer → run script → <br />
**Output**: formatted markdown file

<div align=center>
    <h3>Rendered HTML file:</h3><br />
    <img src="/media/highlight-html1.png" style="width: 50%; height: 150;">

    <h3>Raw HTML file:</h3><br />
    <img src="/media/highlight-html2.png" style="width: 50%; height: 100;">

    <h3>Rendered Md file viewed in Preview mode of Obsidian:</h3><br />
    <img src="/media/highlight-md.png" style="width: 50%; height: auto;">
</div>