import socket
from BinaryTree import BinaryTree, Node

#recorrido en preorden
def pre_orden(node):
            if node is None:
                return[]
            return [node] + pre_orden(node.left) + pre_orden(node.right)
tree = BinaryTree()
def main():
    try:
        HOST='127.0.0.1'
        PORT=65432

        #creacion del socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST,PORT))
            s.listen()
            print(f"Servidor escuchando en: {HOST}:{PORT}")
            conn,addr=s.accept()
            with conn:
                print(f"Conectado {addr}")
               
                data_received=[]

                for _ in range(30):
                    data=conn.recv(1024)
                    if not data:
                        break
                    num = int(data.decode())
                    tree.insert(num)
                    data_received.append(num)
                    print(f"Numero recibido: {num}")

                    conn.sendall(b"OK")
                print("\nTodos los datos han sido recibidos")

    except Exception as e:
        print(f"Error: {e}")

if __name__=="__main__":
    main()
