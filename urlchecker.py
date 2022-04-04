import requests
import argparse
import sys

parser = argparse.ArgumentParser(description="Return the status code of a given URLs")
parser.add_argument("-f", type=argparse.FileType('r', encoding='UTF-8'), help="The path to the wordlist")
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
lines = parser.parse_args().f

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args=parser.parse_args()
for line in lines:

 try:

        r = requests.get(line.rstrip())
        code = r.status_code
        print(line, "STATUS =", "[",code,"]")
 except:
    print('exception')


