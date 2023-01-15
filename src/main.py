import parseXml
import json

parser = parseXml.Parser()
argin = {
    # 'person' : 'sergiu',
    'supermarket' : 'dsas'
}

# e = parser.get_predicat('ceaMaiLungaCoada', argin)
# e = parser.get_predicat('ceaMaiScurtaCoada', argin)
# e = parser.get_predicat('clienti', argin)
e = parser.get_predicat('ceaMaiLungaCoada', argin)
print(e)

