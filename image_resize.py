# -*- coding: utf-8 -*-
import argparse
import os
from PIL import Image


def calc_new_image_size(img, width, height, scale):
    if scale:
        scale = abs(float(scale))
        width = round(img.width * scale)
        height = round(img.height * scale)
    else:
        if width:
            width = abs(int(width))
            height = round(width / (img.width / img.height))
        elif height:
            height = abs(int(height))
            width = round(height * (img.width / img.height))
    return width, height


def resize_image(infile, width, height, scale, outfile):
    img = Image.open(infile)
    width, height = calc_new_image_size(img, width, height, scale)
    tmp = img.resize((width, height), Image.ANTIALIAS)
    name, ext = os.path.splitext(infile)
    if not outfile:
        outfile = '{0}__{1}x{2}{3}'.format(name, tmp.width, tmp.height, ext)
    tmp.save(outfile)
    tmp.close()
    return outfile


def get_console_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', '--i', help='Input image', required=True)
    parser.add_argument('--width', '--w', help='Final image width', type=int)
    parser.add_argument('--height', '--h', help='Final image height', type=int)
    parser.add_argument('--scale', '--s', help='Final image scale', type=float)
    parser.add_argument('--outfile', '--o', help='Output image')
    args = parser.parse_args()
    if args.scale and (args.width or args.height):
        print('You can\'t specify both the scale and the width or height')
        parser.print_usage()
        exit(1)
    elif not args.width and not args.height and not args.scale:
        print('You did\'nt specify any width or height or the scale')
        parser.print_usage()
        exit(1)
    return args


def main():
    args = get_console_args()
    final_file = resize_image(args.infile, args.width, args.height,
                              args.scale, args.outfile)
    print('The file is processed and saved as %s' % final_file)

if __name__ == '__main__':
    main()
