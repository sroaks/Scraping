import urllib.request

web = open("web.html","wb")
consulta = urllib.request.urlopen("https://lorem2.com")
consulta = consulta.read()
web.write(consulta)
web.close()

