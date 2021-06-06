numero_secreto = 32

palpite = int(input("Informe Um Palpite: "))

if palpite == numero_secreto:
  print ("\nAcertou\n")
else:
  print ("\nErrou\n")
  if palpite > numero_secreto:
    print ("Chute um número menor\n")
  else:
    print ("Chute um número maior\n")
