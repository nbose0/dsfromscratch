# Data Science from Scratch Notes

## Overview
This document contains notes for Data Science from Scratch 2nd Edition by Joel Grus.

## Motivation
Learn more about DS to use personally and professionally.

## Notes
### Chapter 1: Introduction

### Chapter 2: A Crash Course in Python
#### Set Up
To edit $PATH : `sudo vim /etc/paths`
To add env variable:
`vim ~/.bash_profile`
<in bash profile>
`export <variable_name>=<value>`
<exit vim>
`source ~/.bash_profile`
Restart terminal

#### Strings
`r'\t'` : `r` represents "raw string". `(r'\t' == '\\t') != '\t'`
`f"{first_name} {last_name}"` : formatted string.

#### Truthiness
`and` returns its second value when the first is “truthy,” and the first value when it’s not.
`first_char = s and s[0]` : Empty string or first char of `s`.
`or` 
`safe_x = x or 0` :  0 if `x` is None. `x` otherwise.

#### Object-Oriented Programming
`__init__` : constructor
`__repr__` : toString

### Chapter 3: Visualizing Data
Bar chart: 
1. Show how quantities vary between discrete items
2. Histogram buckets to show distribution

`plt.bar()`

Tip
```
# x-axis is 2017, 2018
# if you don't do the following, matplotlib will label the x-axis 0, 1
# and then add a +2.013e3 off in the corner (bad matplotlib!)
plt.ticklabel_format(useOffset=False)
```

Line chart: show trends
`plt.plot()`

Scatterplot: visualizing relationships between two sets of data

Tip
If two sets are comparable (e.g. grade on test 1 and grade on test 2), matplotlib may choose bad axes creating a misleading chart. Use `plt.axis("equal")` to prevent this.

Consider using seaborn or Altair (newer Python libraries) instead of matplotlib.

### Chapter 4: Linear Algebra
Vector: "Points in some finite-dimensional space"
Scalar: number


## Open Questions
### Chapter 1: Introduction

### Chapter 2: A Crash Course in Python
2.0. Is it necessary to restart terminal if you added something to ~/.bash_profile and ran `source ~/.bash_profile`?

2.1. Is list comprehension lazy evaluation?
Ans: No.

2.2. When should you use `yield` in a program? What is the output of `yield`? 
Ans:

### Chapter 3: Visualization

### Chapter 4: Linear Algebra

4.1. What is a dot product conceptually?

4.2. How do you visualize a vector on a graph? Isn't it a point on an x dimensional plane?

4.3. Why is the magnitude of a vector the sqrt of the sums of its components?

4.4. What does it mean to say that two vectors are x distance apart?




