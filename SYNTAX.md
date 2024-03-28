# XBasic Syntax Guide

## Table of Contents

1. [Introduction to XBasic](#introduction)
2. [Variables and Data Types](#variables-and-data-types)
3. [Operators](#operators)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Lists](#lists)
7. [Strings](#strings)

<a name="introduction"></a>

## 1. Variables and Data Types

### Variable Assignment

In XBasic, you can assign values to variables using the following syntax:
```xbasic
datatype varname = value
```

Here's an example:

```xbasic
num x = 10
text name = "John"
```

### Data Types

XBasic supports the following data types:

- **num**: Integers and floating-point numbers.
- **text**: Strings of characters enclosed in double or single quotes.
- **list**: Comma separated collections of values. There must be atleast 2 values in a list

<a name="operators"></a>
## 2. Operators

### Arithmetic Operators

XBasic supports standard arithmetic operators for numeric operations:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Exponentiation (`^`)

Example:

```xbasic
num result = 10 * (5 + 3) / 2
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
num x = 5
num y = 10
num is_greater = x > y
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
num x = 10
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
    print(i)
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
num x = 1
WHILE x <= 5
    print(x)
    num x = x + 1
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
    RETURN name * 2
END
```

### Function Call

Functions are called by specifying the function name and passing arguments:

```xbasic
datatype result = functionName(arg1, arg2)
```

Example:

```xbasic
text val = greet("John")
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
- Appending elements: You can do using the append method or using the + operator
- Removing elements: you can do using the minus operator
- Concatenating lists

Example:

```xbasic
myList[0] = 10     // Accessing element at index 0
myList.append(6)   // Appending a new element
myList.remove(3)   // Removing an element
newList = myList + [7, 8, 9]  // Concatenating lists
```

---

<a name="strings"></a>
### 7. Strings

XBasic provides various string operations for manipulating textual data. Here are some commonly used string operations:

#### Concatenation
Strings can be concatenated using the `+` operator. This operation combines two or more strings into a single string.

Example:
```xbasic
text str1 = "Hello"
text str2 = "world"
text greeting = str1 + " " + str2  # Result: "Hello world"
```

#### Length
The length of a string can be obtained using the `len()` function. It returns the number of characters in the string.

Example:
```xbasic
text str = "Hello"
num length = len(str)  # Result: 5
```

### String Repetition

In XBasic, you can repeat a string multiple times by using the multiplication (`*`) operator between a string and a numeric value. This operation duplicates the string the specified number of times.

#### Syntax:
```
text * num
```

#### Example:
```xbasic
text str = "Hello "
num repetitions = 3
text repeated_str = str * repetitions  # Result: "Hello Hello Hello "
```

In the above example, the string `"Hello "` is repeated three times, resulting in `"Hello Hello Hello "`. This feature is useful when you need to generate repeated patterns or strings in your XBasic programs efficiently.