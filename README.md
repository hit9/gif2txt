gif2txt
=======

Gif image to to Ascii Text. (Just a toy)

See also [img2txt](https://github.com/hit9/img2txt).

DEMO
----

![](test.gif)

HTML: 

* http://hit9.github.io/gif2txt/examples/out.html
* http://hit9.github.io/gif2txt/examples/withcolor.html
* http://hit9.github.io/gif2txt/examples/greenscreen.html
* http://hit9.github.io/gif2txt/examples/reversegreenscreen.html
* http://hit9.github.io/gif2txt/examples/pacman.html

USAGE
-----

```
python gif2txt.py test.gif -m 80 -o out.html
python gif2txt.py test.gif -m 80 -o withcolor.html -c
python gif2txt.py pacman.gif -o pacman.html -c --green-screen-sensibility 128
python gif2txt.py test.gif -r -o reversegreenscreen.html
```

Requirements
-----------

* Jinja2
* Pillow

```
pip install -r requirements.txt
```
