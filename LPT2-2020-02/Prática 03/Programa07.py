#Nossa Calculadora

from math import sin,cos, radians


#Cria uma função
def mostrar_menu(): 
  print("0 - Sair")
  print("+ - Somar")
  print("- - Subtrair")
  print("* - Multiplicar")
  print("/ - Dividir")
  print("sen - Seno")
  print("cos - Cosseno")
  print("elevado - Potência")
  print("raiz - Calcular a raiz")

def somar():
  numero1 = float(input("\nNúmero 1: "))
  numero2 = float(input("Número 2: "))
  resultado = numero1 + numero2
  print("\nResultado da soma: ", resultado)

def subtrair():
  numero1 = float(input("\nNúmero 1: "))
  numero2 = float(input("Número 2: "))
  resultado = numero1 - numero2
  print("\nResultado da subtração: ", resultado)

def seno():
  angulo = float(input("\nÂngulo: "))
  print("\nSeno do ângulo: ", sin(radians(angulo)))


ligado = True

while ligado == True:
  mostrar_menu()
  opcao = input("\nOpção: ")
  if opcao == "0":
    ligado = False
  elif opcao == "+":
    somar()
  elif opcao == "-":
    subtrair()
  elif opcao == "sen":
    seno()

print("\nAté logo\n")
