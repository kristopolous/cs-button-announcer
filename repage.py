#!/usr/bin/env python3
import sys
import textwrap
import re
import html

process = lambda text: html.escape('\n'.join(map(lambda x: '│ ' + x + ' ' * (wrap_width - len(x)) + ' │', text.split('\n'))))

def process_stream(wrap_width):
    paragraph = []
    
    for line in sys.stdin:
        line = re.sub('\t','  ', line.rstrip())
        
        if '  --' in line or not line: 
            if paragraph:  # Process the previous paragraph
                text = textwrap.fill(' '.join(paragraph), width=wrap_width)
                print(process(text))
                paragraph = []
            line = textwrap.fill(line, width=wrap_width)
            print(process(line))
        else:
            paragraph.append(line.lstrip())  

    if paragraph:
        print(process(textwrap.fill(' '.join(paragraph), width=wrap_width)))

wrap_width = int(sys.argv[1] if len(sys.argv) > 1 else 80)
process_stream(wrap_width)

