import re

def range_parser(string):
    # Separamos el string con un delimitador 
    splited = re.split(',', string)
    result = []
    
    for item in splited:  
        # Verificamos si el 'item' tiene el delimitador '-'
        if '-' in item:
            # Verificamos si el 'item' tiene el delimitador ':'
            if ':' in item:
                split = re.split('-|:', item)
                result += [n for n in range(int(split[0]),int(split[1]) + 1,int(split[2]))]
            else:
                split = re.split('-', item)
                result += list(range(int(split[0]), int(split[1]) + 1))     
        else:
            # No tiene delimitador
            result += [int(item)]

    return result