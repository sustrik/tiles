#!/usr/bin/env python

from tiles import tile

def greet(name):
    return tile("""
                print 'Hello, @{name}!'
                print 'Welcome!'
                """)

print greet('Alice')
