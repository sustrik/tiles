#!/usr/bin/env python

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

print tile("""
           Colors: @{colors}     Shapes: @{shapes}

           That's all, folks!
           """)
