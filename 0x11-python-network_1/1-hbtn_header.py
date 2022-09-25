#!/usr/bin/python3
"""
    A python script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable
    found in the header of the response
"""

from sys import argv
from urllib import (request)

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        header = response.info()

    print(header.get("X-Request-Id"))
