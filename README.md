# Tiles

*Tiles* is a simple Python module meant to help with *code generation*.
It provides a way to deal with *rectangular areas of text* as atomic units.
This is particularly important if proper *indentation* of generated code is
desired.

Tile is a standard Python string. However, one should keep in mind that
conceptually it's just the ractangular area of non-whitespace characters
that counts.

```
s = """

         Hello,
           world!

    """
```


