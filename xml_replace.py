"""With a XML Snippet replace variables present in a CSV

Usage:
  xml_replace.py  (-h | --help)
  xml_replace.py  --version
  xml_replace.py  -s <snipet_file>  -v <variables>
  

Options:
  -h --help                             Show this screen.
  -s <snipet_file>                    	Text file with XML snippet (variable example: {{VAR1}})
  -v <variables>						CSV file with variables to be replaced (first row with variable names)
  --version                             Show version.

"""

import csv
from docopt import docopt

def getFile(filename):
    f = open (filename, 'r')
    archivo = f.read()
    f.close()
    return(archivo)


if __name__ == '__main__':

    arguments = docopt(__doc__, version='XML_Replace v1.0')
#    print(arguments)
    snippet_file = arguments['-s']
    variables = arguments ['-v']
    
    snippet = getFile(snippet_file)
	
    with open(variables) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tempString_out = snippet
            for vars in row:
                tempString_out = tempString_out.replace('{{'+ vars + '}}', row[vars])
            print(tempString_out)
    
