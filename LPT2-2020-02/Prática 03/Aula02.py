numero_secreto = 32

palpite = int(input("Informe Um Palpite: "))

if palpite == numero_secreto:
  print ("\nAcertou\n")
elif palpite > numero_secreto:
  print ("Chute um número menor\n")
elif palpite < numero_secreto:
  print ("Chute um número maior\n")  
else:
  print ("Caso Padrão\n")
