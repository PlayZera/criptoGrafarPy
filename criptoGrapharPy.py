from cryptography.fernet import Fernet
import os

def menu():
    print("digite o numero correspondente a opcao que voce deseja")
    print("1- Encriptar")
    print("2- Desincriptar")

    op = int(input())

    if(op == 1):
        encriptar()

    if(op == 2):
        decode()

def encriptar():

    try:
        print("Antes de iniciar por favor anote a key descriptografar a sua senha em um futuro...")
        keyGerada = Fernet.generate_key()
        print(keyGerada.decode())

        print("Digite a palavra que você deseja encriptar")
        password = str(input())

        instanciaFernet = Fernet(keyGerada)
    
        passwordEncrypt = instanciaFernet.encrypt(password.encode())

        print("A sua palavra encriptada: " ,passwordEncrypt.decode())
        menu()

    except:
        print("Falha ao tentar encriptar a sua palavra")
        #os.system('cls') or None
        menu()

def decode():

    try:
        print("Para que seja desincriptada a sua palavra por favor informe a sua key...")
        keyPass = input()
        print("Informe a sua palavra encriptada:")
        encryptPass = input()

        decodeInstanceFernet = Fernet(keyPass)
        result = decodeInstanceFernet.decrypt(encryptPass)

        print("Desincriptada a sua palavra: " ,result.decode())
        menu()
        
    except:
        print("Falha ao tentar desincriptar a sua palavra")
        #os.system('cls') or None
        menu()

menu()
    

