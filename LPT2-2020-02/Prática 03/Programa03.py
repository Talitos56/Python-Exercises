numero_secreto = 32
palpite = 0

while numero_secreto != palpite:
  palpite = int(input("Informe Um Palpite: "))

  if palpite == numero_secreto:
    print ("\nAcertou\n")
  elif palpite > numero_secreto:
    print ("\nChute um número menor\n")
  elif palpite < numero_secreto:
    print ("\nChute um número maior\n")  
  else:
    print ("Caso Padrão\n")
