import sys
import argparse
import json
import subprocess
import os


def curl_command_func():
    curlcommand = str("curl -X POST -H "+
                      "\"Content-Type: application/x-www-form-urlencoded\""
                      + " -d \"grant_type=client_credentials\""
                      + " -d \"client_id=5e15e933\""
                      + " -d \"client_secret=a09256c925adc9e2279435038df9d55e\" "
                      + "\"https://api.ambiverse.com/oauth/token\"")

    print curlcommand
    try:
        outputdata = subprocess.check_output(str(curlcommand), shell=True)
    except subprocess.CalledProcessError:
        print 'CalledProcessError'

    print (outputdata)

curl_command_func()