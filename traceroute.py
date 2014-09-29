#!/usr/bin/python -tt
# coding: utf-8

import sys
from subprocess import Popen, PIPE

def main():

  if not sys.argv[1]:
    sys.exit(1)
  node = sys.argv[1]

  urls = ('google.com', 'akamai.com')
  for url in urls:
    f = open(node + '-' + url + '.txt', 'w')
    sp = Popen(['traceroute', url], stdout=PIPE)
    f.write(sp.communicate()[0])
    f.close()

if __name__ == '__main__':
  main()