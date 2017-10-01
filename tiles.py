# Copyright (c) 2017 Martin Sustrik  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import inspect

def __trim(arg):
    s = arg.split("\n")
    top = -1; bottom = 0; left = -1
    for i in range(len(s)):
        if len(s[i].strip()) == 0:
            continue
        bottom = i
        if top == -1:
           top = i
        first = len(s[i]) - len(s[i].lstrip())
        if left == -1 or first < left:
            left = first
    if top == -1:
        top = 0
    r = []
    for i in range(top, bottom + 1):
        r.append(s[i][left:].rstrip())
    return r

def __append(curr, val):
    w = max([len(s) for s in curr or [""]])
    for i in range(len(val)):
        if i >= len(curr):
            curr.append("")
        curr[i] = curr[i].ljust(w) + val[i]

def tile(s):
    globs = inspect.currentframe().f_back.f_globals
    locs = inspect.currentframe().f_back.f_locals
    lns = __trim(s)
    res = []
    for i in range (len(lns)):
        curr = []
        pos = 0
        while True:
            start = lns[i].find("@{", pos)
            __append(curr, [lns[i][pos : (len(lns[i]) if start == -1 else start)]])
            if start == -1:
                break
            end = lns[i].find("}", start)
            if end == -1:
                raise Exception("unifinished @{} expression")
            val = __trim(str(eval(lns[i][start + 2 : end], globs, locs)))
            __append(curr, val)
            pos = end + 1
        res += curr
    return "\n".join(res)
