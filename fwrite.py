#!/usr/bin/env python

import os, sys, time

old_dir = os.listdir("/Users/slmullin/Development/paemon/sample")
new_dir = os.listdir("/Users/slmullin/Development/paemon/sample")
for x in new_dir:
    print x
    
with open("/Users/slmullin/Development/paemon/files", "r") as content_file:
    lines = [line.rstrip() for line in content_file]
    for line in lines:
        print line