def pass_check():
    inpt = int(input())
    if inpt != 2002:
        print("Senha Invalida")
        return pass_check()
    else:
        print("Acesso Permitido")


passw = pass_check()