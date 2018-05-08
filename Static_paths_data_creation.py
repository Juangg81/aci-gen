"""With a CSV with interfaces, description, trunk status and VLANS list, create one line per vlan for Static path creation

Usage:
  Static_paths_data_creation.py  (-h | --help)
  Static_paths_data_creation.py  --version
  Static_paths_data_creation.py  -v <variables>
  

Options:
  -h --help                             Show this screen.
  -v <variables>						CSV file with info (column header "vlans")
  --version                             Show version.

"""

import csv
from docopt import docopt

def getFile(filename):
    f = open (filename, 'r')
    archivo = f.read()
    f.close()
    return(archivo)

def	obtener_vlans(listado_vlans):
    resultado = []
    arreglo = listado_vlans.split(',')
    for elemento in arreglo:
        rango = elemento.split('-')
        if len(rango) == 1:
            resultado.append(int(rango[0]))
        else:
            for numero in range(int(rango[0]),int(rango[1])+1):
                resultado.append(numero)
    return resultado

if __name__ == '__main__':

    arguments = docopt(__doc__, version='Data_Replicator_StaticPaths v1.0')
#    print(arguments)
    variables = arguments ['-v']
    print("interface,description,trunk,vlans")
    
    with open(variables) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for single_vlan in obtener_vlans(row["vlans"]):
                print row["interface"] + "," + row["description"] + "," + row["trunk"] + "," + str(single_vlan)

    
