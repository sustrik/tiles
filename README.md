# Tiles

*Tiles* is a simple Python module meant to help with *code generation*.
It provides a way to deal with *rectangular areas of text* as atomic units.
This is particularly important if proper *indentation* of generated code is desired.

The module contains a single function:

```python
from tiles import tile
```

The function takes a string and expands any `@{}` expressions within it.

More importantly though, all `@{}` expressions are treated not as strings but rather as tiles, i.e. rectangular areas of text.

Note that any whitespace around the rectangular are of text is ignored.

