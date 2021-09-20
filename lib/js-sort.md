2021-08-10"
tags: 
 - JavaScript
categories: 
- code
---

JS Function to sort data alphabetically


items.sort(function (a, b) {
  return a.localeCompare(b); //using String.prototype.localCompare()
});
```
#Reference:https://dev.to/banesag/sorting-arrays-of-strings-in-javascript-2g11

```javascript
const simpleSort = Array.from(strings).sort((a, b) => a - b);
```
#Reference: https://www.w3schools.com/jsref/jsref_sort.asp
