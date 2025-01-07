
import re
inputstring = ' some strings are present in between "geeks" "for" "geeks" '

match = re.search('"([^"]*)"', inputstring)
 
#print(re.search('"([^"]*)"', inputstring))

if match:
    print(match.group(0))
