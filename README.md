Proj4JsDefGenerator
===========================

This is a small python script that generates [Proj4JS](http://proj4js.org/ "Proj4JS Project Site") definition files of a 
Spatial Reference System (SRS) identified by its [EPSG](http://www.epsg.org/ "EPSG Website")-codes. 

The script uses the EPSG file of Ubuntu (/usr/share/proj/epsg) if available.
Otherwise a local copy of the EPSG file within this project is used.


Execute the script like this:

    python main.py <epsg>

    python main.py 31467
