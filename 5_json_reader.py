import json

file = open("ejemplo_json","r")
file=json.loads(file.read())

print(f"Son {len(file)} colores")

for dato in file:
    print("Color: ", dato["nombreColor"], dato["valorHexadec"])
    print("-"*10)
    


#print(file)
