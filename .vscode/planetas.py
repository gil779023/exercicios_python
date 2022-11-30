
import json    # java script order


planetas = [
    {
        'Ordem': 1,    
        'Nome': "Mercurio",    
        'Distancia': 57910000,    
        'Diametro': 4879,    
        'Rochoso': "Sim"
    }
    ,
    {
        'Ordem': 2,    
        'Nome': "Venus",    
        'Distancia': 108200000,    
        'Diametro': 12104,    
        'Rochoso': "Sim"
    }
    ,
    {
        'Ordem': 3,    
        'Nome': "Terra",    
        'Distancia': 149600000,    
        'Diametro': 12742,    
        'Rochoso': "Sim"
    }
]

print(json.dumps(planetas , indent=4))





json_file = open('planetas.json', mode='r')
data = json.load(json_file)
json_file.close()
print(data)