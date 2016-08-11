Basic Installation 
=================

To install the package simply run
pip install locate-me

NB: This is a toy project that has only been tested on Mac OSX using python 3. This package depends on
pillow and you will need to manually install some external libraries for it to work
properly. 

To install the library, run:

brew install libtiff libjpeg webp little-cms2

Once the package is installed you can run it like so:

locate_me <path to the file you want to parse>
