import socket
from BinaryTree import BinaryTree, Node
import graphviz

# Función para generar la visualización del árbol con Graphviz
def generate_tree_graph(root_node):
    # Crea un nuevo gráfico dirigido
    dot = graphviz.Digraph(comment='Arbol Binario de Busqueda', format='png')
    
    # Función recursiva para añadir nodos y aristas
    def add_nodes_edges(node):
        if node is not None:
            # Añade el nodo al gráfico
            dot.node(str(node.value))
            if node.left:
                # Añade una arista del padre al hijo izquierdo
                dot.edge(str(node.value), str(node.left.value))
                add_nodes_edges(node.left)
            if node.right:
                # Añade una arista del padre al hijo derecho
                dot.edge(str(node.value), str(node.right.value))
                add_nodes_edges(node.right)
    
    add_nodes_edges(root_node)
    
    return dot

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

                tree = BinaryTree()
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

                   
                #visualización del árbol con graphviz
                if tree.root:
                    try:
                        #generar el gráfico y guardarlo como un archivo .png
                        dot = generate_tree_graph(tree.root)
                        dot.render('arbol_binario', view=True, cleanup=True)
                        print("\n--- Visualización del árbol generada y abierta ---")
                        print("El archivo 'arbol_binario.png' ha sido creado en este directorio.")
                    except Exception as e:
                        print(f"Error al generar la visualización con Graphviz: {e}")
                        print("Asegúrate de que Graphviz esté instalado y en tu PATH.")
                else:
                    print("\nNo hay datos para construir el arbol.")

    except Exception as e:
        print(f"Error: {e}")

if __name__=="__main__":
    main()
