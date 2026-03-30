name = "Ilya"
last_name = "Cortes Ruiz"
spaced_name = "Ilya         Cortés            Ruiz"
print(name[0])
print(name[1])
print(name[2])
print(name[3])

#Concatenación
print(name + " " + last_name)

#Replicación de un String
print(name * 5)

#Consultar Caracteres
#Los espacios también son contados
print(len(name))

#Metodos
print(name.lower())
print(name.upper())
print(spaced_name.strip())
print(last_name.swapcase())
print(last_name.split())


