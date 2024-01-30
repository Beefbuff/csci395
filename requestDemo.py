#Kyle Kalbach
#01/30/2024
#csci395
import sys,requests

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

    #requesting the url and reafing it into rfc_raw
rfc_response = requests.get(url) 

    #display the data into the console
print(rfc_response.text)