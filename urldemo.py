#Kyle Kalbach
#01/30/2024
#csci395
import sys, urllib.request
from urllib.request import Request

try:
    # grabs second arg
    rfc_num = int(sys.argv[1]) 

except (IndexError, ValueError): 
    print('Please provide an RFC number as first argument e.g. in Terminal, type: python3 name_of_program.py RFC num') 
    sys.exit(2) 

    #http template string with {} as a placeholder
source = 'http://www.rfc-editor.org/rfc/rfc{}.txt' 
    #creating the url using format and supplying the user input argument
url = source.format(rfc_num) 

    #requesting the url and reading it into rfc_raw
rfc_raw = urllib.request.urlopen(Request(url,headers={'User-Agent': 'Mozilla/5.0'})).read()
    #format the data into utf-8
rfc = rfc_raw.decode('utf-8') 
    #display the data into the console
print(rfc)