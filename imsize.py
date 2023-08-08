#!/usr/bin/env python3
# imsize.py

import sys

def Usage():
    print("Usage: imdims.py <filepath>")
    sys.exit(1)

def main() -> int:
    if (len(sys.argv) != 2):
        Usage()
    filepath = sys.argv[1]
    from PIL import Image
    im=Image.open(filepath)
    (w,h) = im.size # (width, height) tuple
    
    print('{}, w={}, h={}'.format(filepath, w, h))
    return 0

if __name__ == '__main__':
    sys.exit(main())

