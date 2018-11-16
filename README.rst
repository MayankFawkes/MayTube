MayTube
===========

.. image:: https://img.shields.io/pypi/pyversions/proxybroker.svg?style=flat-square


Requirements
------------

* Python **3.5** or higher
* `requests <https://github.com/requests/requests>`_


Installation
------------

To install last stable release from pypi:

.. code-block:: bash

    $ Not Available Yet

The latest development version can be installed directly from GitHub:

.. code-block:: bash

    $ wget https://raw.githubusercontent.com/MayankFawkes/MayTube/master/MayTube.py



Usage
-----

Sample Program With Chrome Installed in Windoes 10

.. code-block:: bash

    import os
    from MayTube import *
    def main():
    	link=YouTube(link="Z9W2Xe1Xu8c",vtype="128mp3")
	    command=str("start chrome {}{}{}".format('"',link,'"'))
	    os.system(command)

    if __name__ == "__main__":
	    main()

Video Type (vtype)
----
* YouTube(link="",vtype="720mp4") **720mp4** Default

vtype Available
~~~~~~~~~~~~
.. code-block:: bash
    1080mp4
    720mp4
    360mp4
    2403gp
    1443gp
    128mp3

License
-------

Licensed under the Apache License, Version 2.0
					
And

    This is free and unencumbered software released into the public domain.    

    Anyone is free to copy, modify, publish, use, compile, sell, or
    distribute this software, either in source code form or as a compiled
    binary, for any purpose, commercial or non-commercial, and by any
    means.    

    In jurisdictions that recognize copyright laws, the author or authors
    of this software dedicate any and all copyright interest in the
    software to the public domain. We make this dedication for the benefit
    of the public at large and to the detriment of our heirs and
    successors. We intend this dedication to be an overt act of
    relinquishment in perpetuity of all present and future rights to this
    software under copyright law.    

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
    OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.    

    For more information, please refer to <http://unlicense.org>




*This product includes y2mate.com data created by Me, and Thanks to* `https://y2mate.com/ <https://y2mate.com/>`_.
