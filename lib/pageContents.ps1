$OneNote = New-Object -ComObject OneNote.Application
[xml]$Hierarchy = ""
$OneNote.GetHierarchy("", [Microsoft.Office.InterOp.OneNote.HierarchyScope]::hsPages, [ref]$Hierarchy)

$s = $Hierarchy.Notebooks.Notebook.Section.Where({ $_.name.StartsWith("Outline")})

$res = ForEach($page in $s.Page){
        [ref]$PageXML = ''
        $OneNote.GetPageContent($page.ID, [ref]$PageXML, [Microsoft.Office.Interop.OneNote.PageInfo]::piAll)
        $PageXML.lastModifiedTime
}
Out-File -FilePath .\output.txt -InputObject $res