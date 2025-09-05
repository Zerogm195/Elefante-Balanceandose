import random
import time
from funcionsecreta import funcionsecreta
import json
from os import path

numeroelefantes = 1
aguanta = 150
serompe = 0
tiempo = 2

## Contador de veces que se ha abierto el programa

nombre_archivo = 'numerodevecesqueseabrio.json'

if not path.exists(nombre_archivo):
    with open(nombre_archivo, "w") as f:
        json.dump({"veces": 0}, f)

with open(nombre_archivo, "r") as f:
    data = json.load(f)

data["veces"] += 1

with open(nombre_archivo, "w") as f:
    json.dump(data, f)

##################################################################

print("Bienvenido, este es un programa que simula la cancion de los elefantes")

if data["veces"] == 1:
    print("Es la primera vez que usas este programa, espero que te guste :D")
    time.sleep(2)

elif data["veces"] == 2:
    print("Vaya, ya es la segunda vez que usas este programa, espero que te guste :D")
    time.sleep(2)
    print("Mmmmm... sigues aqui?..... muehehehe")
    time.sleep(2)

elif data["veces"] == 3:
    print("Mira, no pense que alguien usara este programa mas de 2 veces :D o quizas si mueheehehe")
    time.sleep(2)

elif data["veces"] == 5:
    print("Vaya asi que van 5 veces que usas este programa, espero que te guste :D")
    time.sleep(2)
    print("Sigues aqui?..... muehehehe")
    time.sleep(2)
    print("*Se esconde*")

elif data["veces"] == 10:
    print("Asi que van 10 veces... te felicito por tu perseverancia :D")
    time.sleep(2)
    print("Aqui no hay nada especial, ni un secreto je...jeje")
    time.sleep(2)
    print("O tal vez si... muehehehe")
    time.sleep(2)

elif data["veces"] == 25:
    print("25 veces, no esta nada mal... te dire algo: el que persevera alcanza :D")
    time.sleep(2)
    print("Asi que sigue asi y algun dia podras ver algo especial :D")
    time.sleep(2)
    print("O tal vez no... muehehehe")
    time.sleep(2)

elif data["veces"] == 50:
    print("Wow 50 veces, eres un usuario muy dedicado :D")
    time.sleep(2)
    print("Te daré un pequeño regalo:")
    time.sleep(2)
    print("¿Sabias que el elefante es el unico mamifero que no puede saltar?")
    time.sleep(2)
    print("y diras... ¿y eso que tiene que ver?")
    time.sleep(2)
    print("Pues nada, solo queria darte un dato curioso XD")
    time.sleep(2)

elif data["veces"] == 100:
    print("100 veces, impresionante... eres un usuario muy dedicado :D")
    time.sleep(2)
    print("Te daré otro pequeño regalo:")
    time.sleep(2)
    print("¿Sabias que los elefantes pueden reconocer su reflejo en un espejo?")
    time.sleep(2)
    print("y diras... ¿y eso que tiene que ver?")
    time.sleep(2)
    print("Pues yo tampoco kajskajskajska")
    time.sleep(2)

elif data["veces"] == 200:
    print("Eres el guerrero dragón de los elefantes, 200 veces, impresionante... eres un usuario muy dedicado :D")
    time.sleep(2)
    print("Te dire algo:")
    time.sleep(2)
    print("if numeroelefantes >= 666:")
    time.sleep(2)
    print("Igual y pasa algo quien sabe muehehee")
    time.sleep(2)

elif data["veces"] == 500:
    print("A partir de aqui ya no habran mas mensajes especiales por abrir el programa muchas veces")
    print("Asi que si quieres ver mas mensajes especiales, tendras que buscar los finales secretos :D")
    time.sleep(2)
    print("Suerte!!!")
    time.sleep(2)
        

while True:

    probabilidad = random.randint(serompe,aguanta)

    if probabilidad >= 1:
        #time.sleep(tiempo) #Funcion de espera (usuario promedio)
        print(f"{numeroelefantes} elefantes se balanceaba sobre la tela de una araña")
        #time.sleep(tiempo)
        print("Como veía que resistía, fue a llamar a otro elefante")
        numeroelefantes += 1
        aguanta -= 1

    elif probabilidad == 0:

        
        if numeroelefantes >= 200 and numeroelefantes < 400:
            print("Final secreto numero 1: Para bailar la bamba para bailar la bamba se necesita una poca de gracia una poca de gracia pa mi pa ti arriba y arriba")
            break
        elif numeroelefantes >= 400 and numeroelefantes < 600:
            print("Final secreto numero 2: Never gonna give you up, never gonna let you down, never gonna run around and desert you")
            time.sleep(2)
            print("Never gonna make you cry, never gonna say goodbye, never gonna tell a lie and hurt you")
            time.sleep(2)
            print("You've been rickrolled")
            break
        
        elif numeroelefantes >= 600 and numeroelefantes < 800:
            print("Final secreto numero 3: ¡Felicidades! Has encontrado el final secreto, pero no hay más elefantes, así que el programa termina aquí.")
            time.sleep(2)
            print("Si pudieras comenzar a ser la mitad de lo que crees de mi, cualquiera podría ser y podria aprender a amar, como tú")
            break

        elif numeroelefantes >= 800 and numeroelefantes < 999:
            print("Final secreto numero 4: ¡Felicidades! Has encontrado el final secreto, pero no hay más elefantes, así que el programa termina aquí.")
            time.sleep(2)
            print("Felicidades, has hecho que el programa se autodestruya!!!")
            print("Iniciando secuencia de autodestrucción en 5 segundos...")
            time.sleep(5)
            print("os.remove('elefantes.py')")
            time.sleep(2)
            print("eliminando elefantes.py...")
            time.sleep(2)
            print("elefantes.py eliminado")
            time.sleep(2)
            print("Eliminando sistema operativo...")
            time.sleep(2)
            print("Sistema operativo eliminado")
            time.sleep(2)
            print("Eliminando la existencia misma...")
            time.sleep(2)
            print("Dividiendo entre 0..... Adios")
            time.sleep(2)
            try:
                exception = 1 / 0
            except ZeroDivisionError:
                print("Bienvenido al ciclo infinito de los elefantes...")
                time.sleep(2)
                print("¿Podrá la tela resistir? Solo el destino lo dirá.")
                time.sleep(2)
                print("Oh no, la tela del tiempo y el espacio se ha roto...")
                time.sleep(2)
                print("¿¡Qué has hecho!?")
                time.sleep(2)
                print("Ahi viene.....")
                time.sleep(2)
                exception = 1 / 0

            #Hola programador, asi que viendo el codigo eh?
            #Si quieres evitar el error de division entre 0, solo quita la linea 61
            print("Si ves este mensaje, es que has evitado la autodestrucción, felicidades y como premiooo")
            funcionsecreta()
            break

        elif numeroelefantes >= 999:
            print("Felicidades ahora te tengo una ligera sorpresa!")
            time.sleep(2)
            print("Aver si esto es de tu talla o(.^.^.)o")
            time.sleep(2)
            print("modify line 4 : numeroelefantes = 1")
            numeroelefantes = 1
            time.sleep(2)
            print("Muehehehe ahora no tendré que escribir más codigo :D")
            continue

        elif numeroelefantes == 666:

            from faker import Faker
            listanombres = []
            n = 0
            print("Has llegado al numero de la bestia, asi que ahora pondré el nombre de todos los elefantes")

            while n < numeroelefantes:
                fake = Faker()
                nombre = fake.name()
                listanombres.append(nombre)
                n += 1

            for nombre in listanombres:
                print(nombre)
                time.sleep(0.5) #Hacer sufrir al usuario

            print("Muehehehehehehehe")
            break

        elif numeroelefantes == 777:
            print("Has llegado al numero de la suerte, asi que ahora te daré un mensaje de buena suerte")
            time.sleep(2)
            print("La suerte no es algo que se pueda predecir, pero si algo que se puede crear. Así que crea tu propia suerte y haz que las cosas sucedan.")
            time.sleep(2)
            print("Buena suerte en todo lo que hagas!")
            break
        
        else: 

            print(f"{numeroelefantes} elefantes se cayeron de la tela de una araña")

            print("\nY despues de tanto ir y venir, se cayó la tela de una araña. Los elefantes se cayeron todos al suelo y los pobres ya no se levantaron")
            print(f"\nAl final, valia más una araña en la tela que {numeroelefantes} elefantes balanceandose sobre ella")
            print("\nFin...")

            break
    
    if numeroelefantes == 5:
        print("Hay que tener cuidado...")
    elif numeroelefantes == 10:
        print("Parece una tela de araña muy resistente...")
    elif numeroelefantes == 20:
        print("¿Seguro que es una tela de araña?")
    elif numeroelefantes == 30:
        print("¡Eso ya es una locura!")
    elif numeroelefantes == 50:
        print("Es una tela normal o de hilo de acero?")
    elif numeroelefantes == 100:
        print("¡Esto ya es el colmo!")
    elif numeroelefantes == 200:
        print("¡No puede ser!")
    elif numeroelefantes == 300:
        print("¡Increible!")
    elif numeroelefantes == 400:
        print("¡Imposible!")
    elif numeroelefantes == 500:
        print("Te felicito, has llegado a los 500 elefantes, pero esto tiene que terminar aca ¿tienes la suerte de loteria y la gastas en esto?")
        print("Bueno, sigamos un poco mas...")


