#! /usr/bin/env python3
import argparse
from PIL import Image
from jinja2 import Template


def gif2txt(filename, maxLen=80, output_file='out.html'):
    try:
        maxLen = int(maxLen)
    except:
        maxLen = 80

    chs = "MNHQ$OC?7>!:-;. "

    try:
        img = Image.open(filename)
    except IOError:
        exit("file not found: {}".format(filename))

    width, height = img.size
    rate = float(maxLen) / max(width, height)
    width = int(rate * width)
    height = int(rate * height)

    palette = img.getpalette()
    strings = []

    try:
        while 1:
            img.putpalette(palette)
            im = Image.new('RGB', img.size)
            im.paste(img)
            im = im.resize((width, height))
            string = ''
            for h in range(height):
                for w in range(width):
                    rgb = im.getpixel((w, h))
                    string += chs[int(sum(rgb) / 3.0 / 256.0 * 16)]
                string += '\n'
            strings.append(string)
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    with open('template.jinja') as tpl_f:
        template = Template(tpl_f.read())
        html = template.render(strings=strings)
    with open('out.html', 'w') as out_f:
        out_f.write(html)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('filename',
                        help='Gif input file')
    parser.add_argument('-m', '--maxLen', type=int,
                        help='Max width of the output gif')
    parser.add_argument('-o', '--output',
                        help='Name of the output file')
    args = parser.parse_args()

    if not args.maxLen:
        args.maxLen = 80
    if not args.output:
        args.output = 'out.html'

    gif2txt(filename=args.filename,
            maxLen=args.maxLen,
            output_file=args.output)

if __name__ == '__main__':
    main()
