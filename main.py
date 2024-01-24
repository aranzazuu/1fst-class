meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LMAO": "una respuesta a algo que nos da mucha risa",
            "ROFL": "una respuesta a una broma",
            "creepy": "algo que nos da miedo",
            "aggro": "ponerse agresivo",
            "diff": "termino de juegos que dice que algo es mejor que otro",
            "nerfeo": "termino de juegos al volver alguna cosa peor de como era antes",
            "buffeo": "termino de juegos al volver algo mejor a como era antes"
            }
print("desea buscar una palabra?")
repetir = input("diga si o no")
            

while repetir == "si":
    print("no entiende alguna de estas palabras?")
    print(meme_dict.keys())
    
    palabra = input("en caso de ser asi escriba la palabra que no entiende: ")
    
    if palabra in meme_dict.keys():
        print(meme_dict[palabra])
        print("desea buscar otra palabra?")
        repetir = input("diga si o no")
        
    else:
        print("revisa tu ortografia por favor")
