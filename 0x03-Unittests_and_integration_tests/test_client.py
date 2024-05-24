#!/usr/bin/env python3

"""
This module demonstrates a simple function with docstring and type annotations.
"""

def greet(name: str) -> str:
  """
  Greets the provided name. 

  Args:
    name: The name of the person to greet (str).

  Returns:
    A greeting message including the name (str).
  """
  return f"Hello, {name}!"

# Sample usage
print(greet("Alice"))
