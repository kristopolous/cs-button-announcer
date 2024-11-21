#!/usr/bin/env python3
import sys
import textwrap
import re
import html

def process_stream(wrap_width):
    paragraph = []
    
    for line in sys.stdin:
        line = re.sub('\t','  ', line.rstrip())
        
        if '  --' in line or not line:  # Blank or non-word-starting line
            if paragraph:  # Process the previous paragraph
                print(html.escape(textwrap.fill(' '.join(paragraph), width=wrap_width)))
                paragraph = []
            print(html.escape(line))
        else:
            paragraph.append(line)  # Collect lines for wrapping

    # Process any remaining paragraph
    if paragraph:
        print(textwrap.fill(' '.join(paragraph), width=wrap_width))

# Example usage
if __name__ == "__main__":
    wrap_width = int(sys.argv[1] if len(sys.argv) > 1 else 100)
    process_stream(wrap_width)

