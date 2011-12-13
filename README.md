Proj4JsDefGenerator
===========================

This is a small python script that helps to generate definition files of EPSG
codes, which can be used in [Proj4JS](http://proj4js.org/ "Proj4JS Project Site")

The script uses the EPSG file of Ubuntu (/usr/share/proj/epsg) if available.
Otherwise a local copy of the EPSG file within this project is used.

To execute the script like this:

python main.py <epsg>

python main.py 31467
