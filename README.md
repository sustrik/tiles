# Tiles

*Tiles* is a simple Python module meant to help with **code generation**.
It provides a way to deal with **rectangular areas of text** as atomic units.
This is particularly important if proper **indentation** of generated code is
desired.

Tile is a standard Python string. However, one should keep in mind that
conceptually it's just the ractangular area of text that counts. All the
surrounding whitespace has no significance.

![](pics/tile.png)

The module provides a single function that can be used to combine smaller
tiles to create larger tiles:

```python
from tiles import tile

colors = """
         White
         Black
         Ultramarine
         Red
         Green
         Blue
         """

shapes = """
         Triangle
         Circle
         """

output = tile("""
              Colors: @{colors}     Shapes: @{shapes}

              That's all, folks!
              """)

print output
```

The output looks like this (expanded tiles marked in red):

![](pics/output.png)

### Worked example

Imagine we want to generate code that prints out some greetings.

```python
def greet(name):
    return "print 'Hello, " + name + "!'\nprint 'Welcome!'" 
```

Although there is no particular need for manipulating rectangular areas of text
here tiling can be employed to make the code more readable.

```python
def greet(name):
    return tile("""
                print 'Hello, @{name}!'
                print 'Welcome!'
                """)
```

Given that whitespace surrounding the tile is ignored anyway we can neatly
align the generated code with the generator code instead of writing an
abomination like this:

```python
def greet(name):
    return tile("""print 'Hello, @{name}!'
print 'Welcome!'""")
```

Another consequence of using tiles is that the greeting function can be used
in different contexts and the indentation will allways be right.

```python
code = tile("""
            import sys

            @{greet('Alice')}
            if len(sys.argv) > 1 and 'also-greet-bob' in sys.argv:
                @{greet('Bob')} 
            """)

print code
```

Here's the output. Note how the greeting code is properly aligned in both
cases, thus forming a valid Python program.

```python
print 'Hello, Alice!'
print 'Welcome!'
if len(sys.argv) > 1 and 'also-greet-bob' in sys.argv:
    print 'Hello, Bob!'
    print 'Welcome!
```

