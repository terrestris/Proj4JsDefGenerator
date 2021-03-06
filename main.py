#!/usr/bin/env python
"""
This script generates a Proj4JS definition for a given EPSG code.
Definition is printed to command line and to a file folder ./defs

Version: 0.1
Date: 2011-12-12
Author: Christian Mayer
License: MIT License (see ./license.txt)
"""
__author__ = 'Christian Mayer'
__version__= '0.1'
__date__= '2011-12-12'
__license__= 'MIT License (see ./license.txt)'

import sys

def print_logo_screen( ):
    """Prints a software logo to the standard out"""

    print ""
    print " _____           _ _  _       _     _____        __          "
    print "|  __ \         (_) || |     | |   |  __ \      / _|         "
    print "| |__) | __ ___  _| || |_    | |___| |  | | ___| |_   ______ "
    print "|  ___/ '__/ _ \| |__   _|   | / __| |  | |/ _ \  _| |______|"
    print "| |   | | | (_) | |  | || |__| \__ \ |__| |  __/ |           "
    print "|_|   |_|  \___/| |  |_| \____/|___/_____/ \___|_|           "
    print "               _/ |                                          "
    print "              |__/                                           "

    print "  _____                           _             "
    print " / ____|                         | |            "
    print "| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ "
    print "| | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|"
    print "| |__| |  __/ | | |  __/ | | (_| | || (_) | |   "
    print " \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   "
    print ""


try:

    print_logo_screen()
    
    # check if an argument has been passed
    if len(sys.argv) == 2:
        
        # read out epsg code from argument
        epsg = sys.argv[1]
        found = False

        try:
            # cast to int which implicitly checks
            # if passed value is an integer number
            iEpsg = int(epsg)
            
            # use current epsg file of Ubuntu if available
            # otherwise use the local copy
            try:
               f = open("/usr/share/proj/epsg", "r")
            except IOError as e:
               f = open("./epsg", "r")

            projTag = "<" + epsg + ">"
            jsDef = ""

            # search for correct epsg definition and
            # transform it to Proj4Js structure
            for line in f:
                if line.startswith(projTag) == True:
                    cleanedLine = line.replace(projTag, "");
                    cleanedLine = cleanedLine.replace("<>", "");
                    cleanedLine = cleanedLine.replace("\n", "");
                    jsDef = "Proj4js.defs[\"EPSG:" + epsg + "\"] = \"" + cleanedLine + "\";"

                    # print out epsg definition
                    print "Copy this ..."
                    print " " 
                    print jsDef

                    # create a Proj4Js definition file with the epsg definition
                    w = open("./defs/EPSG" + epsg + ".js", "w+")
                    w.write(jsDef)
                    w.close()
                    
                    # print out path to Proj4Js definition file
                    print " " 
                    print "... or look at ./defs/EPSG" + epsg + ".js"
                    print " "
                    found = True

            # print info if no matching epsg code has been found
            if found == False:
                print "Provided EPSG code was not found in the list ..."

        # info if no integer number has been passed as epsg argument
        except ValueError:
           print "Please provide a valid EPSG with only the numeric part, e.g. 4326 in order to get the Proj4JS definition of EPSG:4326 ..."
   
    # info in case of missing epsg argument
    else:
        print "Please provide a valid EPSG code as argument..."

except:
    print "Undefined error occured..."

print ""
print "FINISH"
