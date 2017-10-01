#!/usr/bin/env python

from tiles import tile

def greet(name):
    return tile("""
                print 'Hello, @{name}!'
                print 'Welcome!'
                """)

code = tile("""
            import sys

            @{greet('Alice')}
            if len(sys.argv) > 1 and 'all' in sys.argv:
                @{greet('Bob')} 
            """)

print code
