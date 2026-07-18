"""
============================================================
Module 1 - Python Professional
Session 01 - Python Comprehensions
============================================================

Topics
------
• List Comprehension
• Set Comprehension
• Dictionary Comprehension

Objectives
----------
✓ Understand Python comprehensions
✓ Write cleaner and more Pythonic code
✓ Replace simple loops with comprehensions
✓ Practice solving real examples

Difficulty
----------
⭐⭐☆☆☆ (Beginner)

Estimated Time
--------------
30-40 Minutes

Author
------
febz

Date
----
2026-07-16
"""

# ============================================================
# THEORY
# ============================================================

"""
List Comprehension

Syntax:
    [expression for item in iterable if condition]

Set Comprehension

Syntax:
    {expression for item in iterable if condition}

Dictionary Comprehension

Syntax:
    {key: value for item in iterable if condition}

Why use comprehensions?
- Cleaner code
- More readable
- More Pythonic
- Often faster than traditional loops
"""

# ============================================================
# EXAMPLES
# ============================================================

# Example 1
# Create a list containing numbers divisible by 3.

numbers = [x for x in range(1, 31) if x % 3 == 0]
print(numbers)

# ------------------------------------------------------------

# Example 2
# Square all even numbers between 1 and 10.

squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares)

# ------------------------------------------------------------

# Example 3
# Create a set of unique numbers.

unique_numbers = {x for x in range(1, 6)}
print(unique_numbers)

# ------------------------------------------------------------

# Example 4
# Create a dictionary:
# Key = number
# Value = cube of the number

cubes = {x: x**3 for x in range(1, 11)}
print(cubes)

# ============================================================
# EXERCISES
# ============================================================

"""
Exercise 1
Create a list containing numbers divisible by 5
between 1 and 50.

Exercise 2
Convert all words to lowercase.

Exercise 3
Create a dictionary where:
Key = number
Value = square of the number.
"""

# ============================================================
# SOLUTIONS
# ============================================================

# Exercise 1

exercise1 = [x for x in range(1, 51) if x % 5 == 0]
print(exercise1)

# ------------------------------------------------------------

# Exercise 2

words = ["Python", "AI", "Machine Learning", "Git"]

exercise2 = [word.lower() for word in words]
print(exercise2)

# ------------------------------------------------------------

# Exercise 3

exercise3 = {x: x**2 for x in range(1, 6)}
print(exercise3)

# ============================================================
# CHALLENGE
# ============================================================

"""
Challenge

Create a dictionary where:

Key = number
Value =

- square of the number if it is even
- cube of the number if it is odd

Range:
1 → 10

Try solving it without searching online.
"""

# ============================================================
# END OF SESSION 01
# ============================================================