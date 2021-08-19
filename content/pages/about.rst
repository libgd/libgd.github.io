About
#####

:date: 2013-04-09
:slug: about
:title: About
:author: Ondřej Surý

What is the GD library?
-----------------------

GD is an open source code library for the dynamic creation of images
by programmers. GD is written in C, and "wrappers" are available for
Perl, PHP, ruby and many other bindings.

## Supported Image Formats

GD has builtin support for:

- `BMP`_ (builtin)
- `GIF`_ with animation support (builtin)
- `TGA`_ (builtin)
- `WBMP`_ (builtin)
- `WebP`_ via `libwebp`
- `PNG`_ via `libpng`
- `JPEG`_ using external library:

  - `libjpeg-turbo`_ (recommended)
  - `libJpeg`-
  - Does not include `JPEG2000`_

- `AVIF`_ via `libavif`_
- `HEIF`_ via `libheif`_
  - This includes `AVIF` read support if your system's `libheif`_ has AV1 decoding.
- `TIFF`_ via `libtiff`_
- `XPM`_ via `libXpm`_

GD is commonly used to generate charts,  graphics, thumbnails, and most anything else, on the fly. It is lite weight
and fits usages like web development, embemdedded, or any other usages you may need.

It supports transparency, blending, images transformations and various filters. Its design allows the additions of custom 
features in a very friendly manner.

The library was originally developed by `Thomas Boutell`_ and is now
maintained by `Pierre Joye`_ and many `valuable contributors`_, under the umbrella of `PHP.net`_.

Support
-------

Support, discussions or feedback can be done using:

- `github issues`_
- `github discussions`_
- `Gitter chat`_
- `Mailing list`_

Contribute
----------

See `Contribute to LibGD`_.


.. _Thomas Boutell: http://www.boutell.com/
.. _Pierre Joye: https://github.com/pierrejoye
.. _valuable contributors: https://github.com/libgd/libgd/graphs/contributors
.. _PHP.net: http://php.net/
.. _BMP: https://en.wikipedia.org/wiki/BMP_file_format (builtin)
.. _GIF: https://en.wikipedia.org/wiki/GIF
.. _TGA: https://en.wikipedia.org/wiki/Truevision_TGA
.. _WBMP: https://en.wikipedia.org/wiki/Wireless_Application_Protocol_Bitmap_Format
.. _JPEG: https://en.wikipedia.org/wiki/JPEG
.. _libjpeg-turbo: http://libjpeg-turbo.virtualgl.org/
.. _libjpeg-turbo: http://libjpeg-turbo.virtualgl.org/
.. _libJpeg: http://www.ijg.org/
.. _JPEG2000: https://en.wikipedia.org/wiki/JPEG_2000
.. _AVIF: https://en.wikipedia.org/wiki/AV1#AV1_Image_File_Format_(AVIF)
.. _libavif: https://github.com/AOMediaCodec/libavif
.. _HEIF: https://en.wikipedia.org/wiki/High_Efficiency_Image_File_Format
.. _PNG: https://en.wikipedia.org/wiki/Portable_Network_Graphics
.. _WebP: https://en.wikipedia.org/wiki/WebP
.. _libwebp: https://developers.google.com/speed/webp/
.. _XPM: https://en.wikipedia.org/wiki/X_PixMap
.. _libheif: https://github.com/strukturag/libheif/
.. _libpng: http://www.libpng.org/
.. _TIFF: https://en.wikipedia.org/wiki/Tagged_Image_File_Format
.. _libtiff: http://www.libtiff.org/
.. _XPM: https://en.wikipedia.org/wiki/X_PixMap
.. _libXpm: http://xorg.freedesktop.org/
.. _Github Issues: https://github.com/libgd/libgd/issues
.. _Github Discussions: https://github.com/libgd/libgd/discussions
.. _Gitter Chat: https://gitter.im/libgd/libgd
.. _Mailing list: http://news.php.net/php.gd.devel/
.. _Contribute to LibGD: https://github.com/libgd/libgd/blob/master/CONTRIBUTING.md