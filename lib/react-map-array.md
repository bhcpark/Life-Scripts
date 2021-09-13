---
title: Element mapping
date: "2021-08-10"
tags:
- JavaScript
- HTML
- React
categories: 
- code
---

Filter data array into HTML on React

<!--more-->

```javascript
{/* filter based on selection */}
<ul>
{data.filter(data => data.variable ==  variablematch).map((el) => (
                        
                    <li key={el.id}>
                        <b>{el.topic}</b>
                        <ul>
                            <li>{el.q1}</li>
                            {el.q2 !== "" && <li>{el.q2}</li>} {/* conditional if exists element */}
                        </ul>
                    </li>
          ))}
```