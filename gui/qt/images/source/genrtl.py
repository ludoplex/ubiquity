#!/usr/bin/env python

"""
Generates rtl versions of images by mirroring them
"""
import glob

from PyQt5.QtGui import QImage

def main():
    for src in glob.glob("*_ltr.png"):
        dst = src.replace("ltr", "rtl")
        print(f"{src} => {dst}")
        img = QImage(src)
        img.mirrored(True, False).save(dst)

if __name__ == "__main__":
    main()
