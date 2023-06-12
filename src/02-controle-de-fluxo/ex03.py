""" Ex 03 """

identificador = input("Entre com o identificador de funcionário: ")

if len(identificador) == 7:
    if 'BR' in identificador:
        if 'X' in identificador:
            numero = int(identificador[2:6])
            if 1 <= numero <= 9999:
                print("Identificador válido")
            else:
                print("Identificador inválido")
        else:
            print("Identificador inválido")
    else:
        print("Identificador inválido")
else:
    print("Identificador inválido")
