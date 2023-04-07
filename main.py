import pandas as pd
import requests,json

year = "2023"
countryCode = "BR"

feriados = requests.get("https://date.nager.at/api/v3/publicholidays/" + year + "/" + countryCode)
personagens = requests.get("https://rickandmortyapi.com/api/character?page=19")


def saveToFile(data, filename, subjson=False):
    if(subjson):
        y = json.loads(data)
        dado = y["results"]
        final = json.dumps(dado)
        data=final
        
    df = pd.read_json(data)
    df.to_excel('{}.xlsx'.format(filename))


saveToFile(feriados.text, "feriados")

saveToFile(personagens.text, "personagens", True)

