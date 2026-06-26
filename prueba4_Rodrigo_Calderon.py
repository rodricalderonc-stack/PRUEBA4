pelicula=[]

def agregar_pelicula(lista):
  print("==AGREGAR PELICULA==")
  nombre=input("Ingrese el nombre de la pelicula: ").lower()
  if nombre.strip()=="":
    print("El nombre de la pelicula no puede estar vacio")
    return
  try:
    duracion=int(input("Ingrese la duracion de la pelicula: "))
    if duracion<=0:
      print("La pelicula debe ser mayor a 0.")
      return
  except ValueError:
    print("La duracion deben ser datos numericos")
  try:
    clasificacion=float(input("Ingrese la clasificacion del 1 al 10: "))
    if 1>=clasificacion>=10:
      print("La clasificion debe ser mayor a 0 e entre del 1-10")
      return
  except ValueError:
    print("La clasificacion deben ser datos numericos")

  nueva_P={
    "nombre":nombre,
    "duracion":duracion,
    "clasificacion":clasificacion,
    "disponible":False
    }
  lista.append(nueva_P)
  print("--PELICULA AÑADIDA CON EXITO--")

def Buscar_pelicula(lista,nombre_buscar):
    posicion=0
    for buscar in lista:
      if buscar["nombre"]==nombre_buscar:
        return posicion

      
      posicion=posicion+1
    return -1


def Eliminar_pelicula():
  print("==ELIMINA PELICULA==")
  nombre=input("Ingrese el nombre de la pelicula que desea eliminar: ")
  posicion=Buscar_pelicula(pelicula,nombre)
  if posicion != -1:
    pelicula.pop(posicion)
    print("--PELICULA ELIMINADA EXITOSAMENTE--")
  else:
    print(f"La pelicula {nombre} no se encuentra registrada")

def actualizar_estado(lista):
  for act in lista:
    if act["clasificacion"]>=7.0:
        act["disponible"]=True
    else:
      act["disponible"]=False


def mostrar_peliculas():
    print("==LISTA DE PELICULAS==")
    if len(pelicula)==0:
      print("No hay peliculas disponibles.")
      return
    actualizar_estado(pelicula)

    for peliculas in pelicula:
      if peliculas["disponible"]==True:
        estado="DISPONIBLE"
      else:
        estado="NO RECOMENDADA"
        
      print("*"*15)
      print(f"Nombre: {peliculas["nombre"]}")
      print(f"Duracion: {peliculas["duracion"]}")
      print(f"Clasificacion: {peliculas["clasificacion"]}")
      print(f"Estado: {estado}")
      print("*"*15)

while True:
  print("\n ========== MENÚ PRINCIPAL ========== ")
  print("1. Agregar pelicula")
  print("2. Buscar pelicula")
  print("3. Eliminar pelicula")
  print("4. Actualizar pelicula")
  print("5. Mostrar pelicula")
  print("6. Salir")    
  print("=====================================")
  opcion=input("Ingrese alguna opcion: ")

  if opcion=="1":
    agregar_pelicula(pelicula)
  elif opcion=="2":
    print("==BUSCAR PELICULA==")
    nombre_buscar=input("Ingrese el nombre de la pelicula: ").lower()
    posicion=Buscar_pelicula(pelicula,nombre_buscar)
    if posicion!=1:
      peliculas=pelicula[posicion]
      estado="DISPONIBLE" if peliculas["disponible"] else "NO RECOMENDADA"

      print(f"\n Pelicula encontrada en la posicion {posicion}")
      print(f"Nombre: {peliculas["nombre"]}")
      print(f"Duracion: {peliculas['duracion']}")
      print(f"Clasificacion: {peliculas['clasificacion']}")
      print(f"Estado: {estado}")
    else:
      print("La pelicula no fue encontrada")

  elif opcion=="3":
    Eliminar_pelicula()
    
  elif opcion=="4":
    actualizar_estado(pelicula)
    print("Estados actualizados exitosamentes de forma global")

  elif opcion=="5":
      mostrar_peliculas()
  elif opcion=="6":
    print("Gracias por utilizar el sistema. Vuelva Pronto")
    break
  else:
    print("Ingrese una opcion valida")
    