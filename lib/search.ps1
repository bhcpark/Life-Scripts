$OneNote = New-Object -ComObject OneNote.Application
[xml]$Hierarchy = ""
$OneNote.GetHierarchy("", [Microsoft.Office.InterOp.OneNote.HierarchyScope]::hsPages, [ref]$Hierarchy)

$s = $Hierarchy.Notebooks.Notebook.SectionGroup.Where({ $_.name.StartsWith("_Exams")})
    ForEach($section in $s.Section){
    ForEach($page in $section.Page){
		        [ref]$PageXML = ''
		        $OneNote.GetPageContent($page.ID, [ref]$PageXML, 		[Microsoft.Office.Interop.OneNote.PageInfo]::piAll)


if($PageXML.value -like '*awake*'){
Write-Output "Found on page: " $PageXML.name;
Write-Output 'onenote:'$section.path'&section-id='$section.id'&page-id='$page.id
Write-Output "----------";
}
						}
				}

