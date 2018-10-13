gif2txt
=======

Gif image to to Ascii Text. (Just a toy)

See also [img2txt](https://github.com/hit9/img2txt).

DEMO
----

![](test.gif)

HTML: 

* http://hit9.github.io/gif2txt/out.html
* http://hit9.github.io/gif2txt/withcolor.html
* http://hit9.github.io/gif2txt/pacman.html

USAGE
-----

```
python gif2txt.py test.gif -m 80 -o out.html
python gif2txt.py test.gif -m 80 -o withcolor.html -c
python gif2txt.py pacman.gif -o pacman.html -c --green-screen-sensibility 128
```

Requirements
-----------

* Jinja2
* Pillow

```
pip install -r requirements.txt
```
