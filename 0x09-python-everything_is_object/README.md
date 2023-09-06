# 0x09. Python - Everything is object
Project Author: Guillaume
Project Attempted by: Thapelo M Moumakoe
Language: `Project`
Subject: `OOP`

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)

## Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```
OK. But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```
![](https://giphy.com/gifs/batman-look-whoa-wAjfQ9MLUfFjq)

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should **read all documentation first (as usual :))**, then take the time to **think and brainstorm with your peers** about what you think and why. **Try to do this without coding anything for a few hours.**

Trying examples in the Python interpreter will give you most of the answers without having to think about it. **Don’t go this route**. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, **you will most likely have to answer to these type of questions**.

All your answers should be only one line in a file. No space before or after the answer.

## Resources
**Read or watch**:
- [9.10. Objects and values](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation](https://www.composingprograms.com/pages/24-mutable-data.html) (Only this chapter)
- [9.12. Cloning lists](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:
### General
- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a newline character
- The first line of all your script files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

### `.txt` Answer Files
- Only one line
- No Shebang
- All your files should end with a new line

## Tasks
### 0. Who am I?
`mandatory`

What function would you use to get the type of an object?

Write the name of the function in the file, without `()`.

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `0-answer.txt`

### 1. Where are you?
`mandatory`

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `1-answer.txt`

### 2. Right count
`mandatory`

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 100
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `2-answer.txt`

### 3. Right count =
`mandtory`

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 89
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `3-answer.txt`

### 4. Right count =
`mandatory`

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `4-answer.txt`

### 5. Right count =+
`mandatory`

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a + 1
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `5-answer.txt`

### 6. Is equal
`mandatory`

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `6-answer.txt`

### 7. Is the same
`mandatory`

What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `7-answer.txt`

### 8. Is really equal
`mandatory`

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `8-answer.txt`

### 9. Is really the same
`mandatory`

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `9-answer.txt`

### 10. And with a list, is it equal
`mandatory`

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `10-answer.txt`

### 11. And with a list, is it the same
`mandatory`

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `11-answer.txt`

### 12. And with a list, is it really equal
`mandatory`

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `12-answer.txt`

### 13. And with a list, is it really the same
`mandatory`

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `13-answer.txt`

### 14. List append
`mandatory`

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `14-answer.txt`

### 15. List add
`mandatory`

What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `15-answer.txt`

### 16. Integer incrementation
`mandatory`

What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x09-python-everything_is_object`
- File: `16-answer.txt`

###
