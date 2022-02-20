from helpers import Helper
from pilas import Stack
from colas import Cola
from listas import Lista

import os

helper = Helper()
lista = ["1) Listas ","2) Pilas ","3) Colas ","4) Salir"]
opcion = ""
while opcion !="4":
  os.system("cls")
  opcion =helper.menu(lista, "Menú")
  os.system("cls")
  if opcion == '1':
    opc1=""
    while opc1 != "7":
      os.system("cls")
      print("*"*10,"LISTAS","*"*10)
      opc1 = helper.menu(["1) Push","2) Pop", "3) Show", "4) Eliminar", "5) Insertar", "6) Buscar", "7) Salir"], "Sub-menú Listas")
      os.system("cls") 
      if opc1 == "1":
        lista1 = Lista()
        print("*"*10,"PUSH","*"*10)
        lista1.push()
        input("\n"
              "Presiona una tecla para continuar =>")
      elif opc1 == '2':
        print("*"*10,"POP","*"*10)
        lista1.pop()
        input("\n"
              "Presiona una tecla para continuar =>")
      elif opc1 == '3':
        print("*"*10,"SHOW","*"*10)
        lista1.show()
        input("\n"
              "Presiona una tecla para continuar =>")
      elif opc1 == '4':
        print("*"*10,"ELIMINAR","*"*10)
        lista1.eliminarElemento()
        input("\n"
              "Presiona una tecla para continuar =>")
      elif opc1 == '5':
        print("*"*10,"INSERTAR","*"*10)
        lista1.insertarElemento()
        input("\n"
              "Presiona una tecla para continuar =>")
      elif opc1 == '6':
        print("*"*10,"BUSCAR","*"*10)
        lista1.buscar()
        input("\n"
              "Presiona una tecla para continuar =>")
      elif opc1 == "7":
        input("Saliendo..." 
              "\n" "Presione una tecla para continuar...")
        break
  
  elif opcion == '2':
    opc1=""
    while opc1 != "6":
      os.system("cls")
      print("*"*10,"PILAS","*"*10)
      opc1 = helper.menu(["1) Push","2) Pop", "3) Show", "4) Buscar","5) Longitud" ,"6) Salir"], "Sub-menú Pilas")
      os.system("cls") 
      if opc1 == "1":
        print("*"*10,"PUSH","*"*10)
        tamaño = int(input('\nIngrese el tamaño de la pila: '))
        pila = Stack(tamaño)
        pila.push(tamaño)
        input("\n"
            "Presiona una tecla para continuar=>")
      elif opc1 == '2':
        print("*"*10,"POP","*"*10)
        pila.pop()
        input("\n"
        "Presiona una tecla para continuar=>")
      elif opc1 == '3':
        print("*"*10,"SHOW","*"*10)
        pila.show()
        input("\n"
        "Presiona una tecla para continuar=>")
      elif opc1 == '4':
        print("*"*10,"BUSCAR","*"*10)
        pila.buscar()
        input("\n"
        "Presiona una tecla para continuar=>")
      elif opc1 == '5':
        print("*"*10,"LONGITUD","*"*10)
        pila.longitud()
        input("\n"
        "Presiona una tecla para continuar=>")
      elif opc1 == "6":
        input("Saliendo..." 
        "\n" "Presione una tecla para continuar...")
        break
  
  elif opcion == '3':
    opc1=""
    while opc1 != "6":
      os.system("cls")
      print("*"*10,"COLAS","*"*10)
      opc1 = helper.menu(["1) Push","2) Pop", "3) Show", "4) Buscar","5) Longitud" , "6) Salir"], "Sub-menú Colas")
      os.system("cls") 
      if opc1 == "1":
        print("*"*10,"PUSH","*"*10)
        tamaño = int(input('\nIngrese el tamaño de la cola: '))
        cola = Cola(tamaño)
        cola.push(tamaño)
        input("\n"
          "Presiona una tecla para continuar=>")
      elif opc1 == '2':
        print("*"*10,"POP","*"*10)
        cola.pop()
        input("\n"
        "Presiona una tecla para continuar=>")
      elif opc1 == '3':
        print("*"*10,"SHOW","*"*10)
        cola.show()
        input("\n"
        "Presiona una tecla para continuar=>")
      elif opc1 == '4':
        print("*"*10,"BUSCAR","*"*10)
        cola.buscar()
        input("\n"
        "Presiona una tecla para continuar=>")
      elif opc1 == '5':
        print("*"*10,"LONGITUD","*"*10)
        cola.longitud()
        input("\n"
        "Presiona una tecla para continuar=>")
      elif opc1 == "6":
        input("Saliendo..." 
        "\n" "Presione una tecla para continuar...")
        break
  elif opcion == "4":
    print("¡Gracias por visitarnos!")