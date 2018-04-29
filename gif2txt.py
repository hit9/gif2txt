# -*- coding: utf-8 -*-

import argparse
from PIL import Image


def gif2txt(filename, maxLen=80, output_file='out.txt', chs="MNHQ$OC?7>!:-;. "):
    try:
        maxLen = int(maxLen)
    except:
        maxLen = 80

    try:
        img = Image.open(filename)
    except IOError:
        exit("file not found: {}".format(filename))

    width, height = img.size
    ratio = float(maxLen) / max(width, height)
    width = int(ratio * width)
    height = int(ratio * height)

    palette = img.getpalette()
    strings = []

    try:
        while 1:
            img.putpalette(palette)
            im = Image.new('RGB', img.size)
            im.paste(img)
            im = im.resize((width, height))
            string = ''
            # Height progresses by 2s since characters are roughly twice as tall
            # as they are wide
            for h in range(0, height, 2):
                for w in range(width):
                    rgb = im.getpixel((w, h))
                    # Use 'luminosity' method
                    # https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
                    luminosity = 0.21 * rgb[0] + 0.72 * rgb[1] + 0.07 * rgb[2]
                    string += chs[int(luminosity / 256.0 * len(chs))]

                string += '\n'

            strings.append(string)
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    with open(output_file, 'w') as out_f:
        out_f.write("=====\n".join(strings));


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('filename',
                        help='Gif input file')
    parser.add_argument('-m', '--maxLen', type=int,
                        help='Max width of the output gif')
    parser.add_argument('-o', '--output',
                        help='Name of the output file')
    # Added option to change what characters are used such as the ones found
    # here: http://paulbourke.net/dataformats/asciiart/
    parser.add_argument('-k', '--keyset', type=str,
                        help="The characters the image will be made of",
                        default="MNHQ$OC?7>!:-;. ")
    args = parser.parse_args()

    if not args.maxLen:
        args.maxLen = 80
    if not args.output:
        args.output = 'out.txt'

    gif2txt(filename=args.filename,
            maxLen=args.maxLen,
            output_file=args.output,
            chs=args.keyset)

if __name__ == '__main__':
    main()
