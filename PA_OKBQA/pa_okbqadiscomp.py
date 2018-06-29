#!/usr/bin/env python
"""This program execute curl command on webserive url for given input data.
   Parameters: file or data, webserivice url
   Example:
   $ python pa_okbqadiscomp.py -f=inputdata.json -w=http://121.254.173.77:2357/agdistis/run

"""
import sys
import argparse
import json
import subprocess
import os

class OKBQADisambiguator(object):
    """The Disambiguator component Class
    """
    def __init__(self, inputdata, webserviceurl):
        """Constructor object initialisation
        :param inputdata:
        :param webserviceurl:
        """
        self.inputdata = inputdata
        self.webserviceurl = webserviceurl
        self.outputdata = ""

    def curl_command_func(self):
        """Execution of Curl Command on Webserivce
        :return:
        """
        tmpdata = "'data=" + self.inputdata + "'"
        curlcommand = str("curl -G --data-urlencode" + " " + tmpdata + " " + self.webserviceurl)
        try:
            self.outputdata = subprocess.check_output(str(curlcommand), shell=True)
        except subprocess.CalledProcessError:
            print 'CalledProcessError'

    def print_outputdata(self):
        """Display result of command output
        :return:
        """
        print self.outputdata


def urlvalidator():
    """For validating wrong url or invalid url
    :return:
    """
    return None


def inputdatafileparsing(inputfilepath):
    """Parsing file to collect json code for input data
    :param inputfilepath:
    :return:
    """
    if os.path.exists(inputfilepath):
        with open(inputfilepath, 'r') as inputfile:
            try:
                tmpinputdata = json.JSONEncoder().encode(json.load(inputfile))
                inputfile.close()
                return tmpinputdata
            except IOError:
                print "Error :Input file read or open error "
                sys.exit()
            except TypeError:
                print "Error :Input file json error "
                sys.exit()
    else:
        print "Error :File path does not exist"
        sys.exit()


def main():
    """Argumnent parser for program parameters and define OKBQADisambiguator class object
    :return:
    """
    webserviceurl = None
    inputdata = None

    parser = argparse.ArgumentParser \
        (description='-----------Pass Input Data and Webserviceurl as Parameters.----------')

    parser.add_argument('-d', '--dataInput', dest='inputdata', type=str,
                        help='Sample input for command', required=False, default=None)
    parser.add_argument('-f', '--dataFile', dest='inputdata_File', type=str,
                        help='Sample input from file for command', required=False, default=None)
    parser.add_argument('-w', '--wsUrl', dest='webserviceurl', type=str,
                        help='Web Service Url', required=True, default=None)
    args = parser.parse_args()


    if args.webserviceurl != None:
        webserviceurl = args.webserviceurl
    else:
        parser.print_help()
        sys.exit()

    if args.inputdata != None:
        inputdata = args.inputdata
    elif args.inputdata_File != None:
        inputdata = inputdatafileparsing(args.inputdata_File)
    else:
        print "Error :Input Data is Missing: " \
              "Please provide data either by file or through command console"
        parser.print_help()
        sys.exit()

    #OKBQADisambiguator class object
    okbqqdisambiguatorobject = OKBQADisambiguator(inputdata, webserviceurl)
    okbqqdisambiguatorobject.curl_command_func()
    okbqqdisambiguatorobject.print_outputdata()


if __name__ == "__main__":
    main()
