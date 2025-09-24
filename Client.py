import socket
import time

def main():    
    HOST='127.0.0.1'
    PORT=65432

    #creacion del socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST,PORT))
            print(f"Conectado al servidor: {HOST}:{PORT}")
            print("\n---Ingreso de los numeros---")
            print("\nPor favor, ingresa 30 numeros enteros de 2 cifras")

            for i in range(30):
                while True:
                    try:
                        #ingreso de los numeros
                        num=int(input(f"Ingrese el numero {i + 1}/30: "))

                        #validar si tiene dos cifras
                        if 10<= num <=99:
                            s.sendall(str(num).encode())

                            #esperar respuesta del servidor
                            respuesta=s.recv(1024)
                            if respuesta.decode=="OK":
                                print(f"Dato '{num}' enviado y confirmado")
                            break
                        else:
                            print("El numero debe tener dos cifras. Intenta de nuevo")                        

                    except ValueError:
                        print(f"Por favor ingresa un numero entero")
                    except ConnectionRefusedError:
                        print(f"Error: El servidor no esta en ejecucion")
                        return

        except ConnectionRefusedError:
            print(f"Error: El servidor no esta en ejecucion")

if __name__=="__main__":
    main()