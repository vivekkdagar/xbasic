# XBasic Syntax Guide

## Table of Contents

1. [Introduction to XBasic](#introduction)
2. [Variables and Data Types](#variables-and-data-types)
3. [Operators](#operators)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Lists](#lists)

<a name="introduction"></a>

## 2. Variables and Data Types

### Variable Assignment

Variables in XBasic are dynamically typed, meaning their data type is inferred from the assigned value. You can assign a value to a variable using the following syntax:

```xbasic
VAR_NAME = value
```

Here's an example:

```xbasic
x = 10
name = "John"
```

### Data Types

XBasic supports the following data types:

- **Numeric**: Integers and floating-point numbers.
- **Text**: Strings of characters enclosed in double or single quotes.
- **List**: Ordered collections of values.

<a name="operators"></a>
## 3. Operators

### Arithmetic Operators

XBasic supports standard arithmetic operators for numeric operations:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Exponentiation (`^`)

Example:

```xbasic
result = 10 * (5 + 3) / 2
```

### Comparison Operators

XBasic provides comparison operators for comparing values:

- Equal to (`==`)
- Not equal to (`!=`)
- Less than (`<`)
- Greater than (`>`)
- Less than or equal to (`<=`)
- Greater than or equal to (`>=`)

Example:

```xbasic
x = 5
y = 10
is_greater = x > y
```

<a name="control-flow"></a>
## 4. Control Flow

### If-Else Statements

The `IF` statement allows conditional execution of code:

```xbasic
IF condition THEN
    // Code block executed if condition is true
ELSE
    // Code block executed if condition is false
END
```

Example:

```xbasic
x = 10
IF x > 5 THEN
    PRINT "x is greater than 5"
ELSE
    PRINT "x is not greater than 5"
END
```

### For Loops

The `FOR` loop allows iterating over a range of values:

```xbasic
FOR variable = start_value TO end_value
    // Code block executed for each iteration
NEXT
```

Example:

```xbasic
FOR i = 1 TO 5
    PRINT i
NEXT
```

### While Loops

The `WHILE` loop repeats a block of code while a condition is true:

```xbasic
WHILE condition
    // Code block executed while condition is true
END
```

Example:

```xbasic
x = 1
WHILE x <= 5
    PRINT x
    x = x + 1
END
```

<a name="functions"></a>
## 5. Functions

### Function Definition

Functions in XBasic are defined using the `FN` keyword:

```xbasic
FN functionName(param1, param2)
    // Function body
    RETURN result
END
```

Example:

```xbasic
FN greet(name)
    PRINT "Hello, " + name
END
```

### Function Call

Functions are called by specifying the function name and passing arguments:

```xbasic
result = functionName(arg1, arg2)
```

Example:

```xbasic
greet("John")
```

<a name="lists"></a>
## 6. Lists

### List Creation

Lists in XBasic are created using square brackets:

```xbasic
myList = [1, 2, 3, 4, 5]
```

### List Operations

XBasic provides various operations for manipulating lists, such as:

- Accessing elements by index
- Appending elements
- Removing elements
- Concatenating lists

Example:

```xbasic
myList[0] = 10     // Accessing element at index 0
myList.append(6)   // Appending a new element
myList.remove(3)   // Removing an element
newList = myList + [7, 8, 9]  // Concatenating lists
```

---

This guide covers the fundamental aspects of XBasic syntax and usage, including variables, data types, operators, control flow, functions, and lists. With this knowledge, you can start writing XBasic programs and explore its capabilities further.
