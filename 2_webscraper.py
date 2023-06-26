def main():
    web = open("web.html","rb")
    inicio = "<li>"
    fin = "</li>"
    for linea in web.readlines():
        linea = str(linea) #cambiar a linea de texto
        if inicio in linea:
            x = linea.find(inicio) #definir variable de inicio
            x = x + len(inicio)
            y = linea.find(fin) #definir variable de fin
            print(linea[x:y])
    """ Transforma cada linea en texto para luego ir linea por línea y buscar si está la variable inicio, en caso de estar, en qué posición
    y cuando lo tiene, me trae todo hasta la variable de fin
    """
        
if __name__ == "__main__":
    main()