# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
# sexo y el nombre. El grupo A esta formado por las mujeres con un nombre
# anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
# resto. Escribir un programa que pregunte al usuario su nombre y sexo, y
# muestre por pantalla el grupo que le corresponde.

name = input("Ingrese su nombre: ") 
sexo = input("Ingrese su sexo: ")

def grupo1(name, sexo):
    nombre = name.lower()
    if sexo.lower() == "mujer" :
        if name < "m":
            return "Grupo A"
        else:
            return "Grupo B"
    elif sexo.lower() == "hombre":
            if name > "n":
                return "Grupo A"
            else:
                return "Grupo B"
    else:
        return "Sexo no válido"
    
grupo = grupo1(name, sexo)
print ("Usted pertenece al grupo " + grupo)           