#!/usr/bin/env python3
# SlicingExample.py - prompt user for a URL and then extract
# the domain name for that input
# input should be in the form --> http://www.somethinghere.com

url = input('Please enter the compete URL (http://www.xyz.com): ')
domain = url[11:-4]
print(domain)
