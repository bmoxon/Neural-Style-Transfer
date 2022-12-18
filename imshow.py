#!/usr/bin/env python3
# imshow.py

import sys
import urllib.request
from urllib.parse import quote
from PIL import Image

def Usage():
    print("Usage: imshow.py [ <filepath> | <url> ]")
    sys.exit(1)

def main() -> int:
    if (len(sys.argv) != 2):
        Usage()
    filepath = sys.argv[1]
    if filepath.find('http') >= 0:
        url = quote(filepath, safe=':/')
        print('url = {}'.format(url))
        urllib.request.urlretrieve(url,'content.xxx')
        im=Image.open('content.xxx')
    else:
        im=Image.open(filepath)

    (w,h) = im.size # (width, height) tuple
    fmt = im.format
    
    print('{}, fmt={}, w={}, h={}'.format(filepath, fmt, w, h))
    im.show()
    return 0

if __name__ == '__main__':
    sys.exit(main())

