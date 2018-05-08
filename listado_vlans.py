"""lista VLANs sacadas de un listado de switchport trunk allowed

Usage:
  listado_vlans.py  (-h | --help)
  listado_vlans.py  --version
  listado_vlans.py  -v <vlans>
  

Options:
  -h --help                             Show this screen.
  -v <vlans>							listado de vlans: ej( -v '1-10,16,100,101-200)
  --version                             Show version.

"""

from docopt import docopt

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

    arguments = docopt(__doc__, version='Listado de VLANs 1.0')
    vlans = arguments['-v']
    for elemento in obtener_vlans(vlans):
        print(elemento)
    
