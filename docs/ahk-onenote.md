---
categories:
- code
date: "2021-08-10"
tags:
- AHK
- OneNote
title: Use AHK to Change Colors in OneNote
---

Quickly change font color and highlights

<!--more-->

### Font color
Using ctrl+shift+letter
```
#IfWinActive OneNote ; ------ only in windows with title ending with "- OneNote"

^!p::Send, !hfca!hfc{Down 7}{Right 4}{Enter}  ; purple
^!r::Send, !hfcm!r255{Tab}5{Tab}0{Enter} ; red (255, 0, 0) 
^!b::Send, !hfcm!r0{Tab}5{Tab}255{Enter} ; blue (0, 0, 255)
^!g::Send, !hfcm!r0{Tab}100{Tab}0{Enter} ; forest green (0, 100, 0) 
^!o::Send, !hfcm!r255{Tab}165{Tab}0{Enter} ; orange (255, 165, 0) 
^!a::Send, !hfca ; automatic color (i.e. reset font color to "none") 

```

### Highlight
Using alt+shift+letter
```
#IfWinActive OneNote ; ------ only in windows with title ending with "- OneNote"

!+p::Send, !hi{right 3}{down 4}{Enter}  ; lavender highlight
!+r::Send, !hi{right 3}{down 3}{Enter} ; pink 
!+b::Send, !hi{right 4}{down 3}{Enter} ; blue 
!+g::Send, !hi{right 1}{down 3}{Enter} ; light green 
!+y::Send, !hi{Enter} ; yello
!+o::Send, !hi{right 4}{up 2}{Enter} ; light orange
!+e::Send, !hi{right 3}{down 2}{Enter} ; grEy
!+a::Send, !hin ; off
```