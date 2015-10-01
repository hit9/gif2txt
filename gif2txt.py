# coding=utf8

from PIL import Image
from jinja2 import Template

maxlen = 80
filename = "test.gif"

chs = "MNHQ$OC?7>!:-;. "

try:
    img = Image.open(filename)
except IOError:
    exit("file not found: {}".format(filename))

width, height = img.size
rate = float(maxlen) / max(width, height)
width = int(rate * width)
height = int(rate * height)

i = 0
palette = img.getpalette()
strings = []

try:
    while 1:
        img.putpalette(palette)
        im = Image.new('RGB', img.size)
        im.paste(img)
        im = im.resize((width, height))
        string = ''
        for h in xrange(height):
            for w in xrange(width):
                rgb = im.getpixel((w, h))
                string += chs[int(sum(rgb) / 3.0 / 256.0 * 16)]
            string += '\n'
        i += 1
        img.seek(img.tell() + 1)
        strings.append(string)
except EOFError:
    pass

with open('template.jinja') as tpl_f:
    template = Template(tpl_f.read())
    html = template.render(strings=strings)
    with open('out.html', 'w') as out_f:
        out_f.write(html)
