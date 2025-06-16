import networkx as nx
import matplotlib.pyplot as plt


class Tablero:
    def __init__(self, A, B):
        self.A = A  # Posición de la ficha A
        self.B = B  # Posición de la ficha B
        self.distancia = 0

    def __str__(self):
        return str(self.A) + " " + str(self.B)

    def evaluacion(tablero):
        if tablero.A == 4:
            return float('inf')
        elif tablero.B == 0:
            return float('-inf')
        else:
            d_max = 4 - tablero.A
            d_min = tablero.B - 0
            return d_min - d_max

    def movimientos_posibles_A(self):
        movimientos = []
        if self.A > 0 and self.A - 1 != self.B:
            movimientos.append(self.A - 1)
        if self.A < 4 and self.A + 1 != self.B:
            movimientos.append(self.A + 1)
        if self.A + 1 == self.B and self.A < 3:
            movimientos.append(self.A + 2)
        if self.A - 1 == self.B and self.A > 1:
            movimientos.append(self.A - 2)
        return movimientos

    def movimientos_posibles_B(self):
        movimientos = []
        if self.B > 0 and self.B - 1 != self.A:
            movimientos.append(self.B - 1)
        if self.B < 4 and self.B + 1 != self.A:
            movimientos.append(self.B + 1)
        if self.B + 1 == self.A and self.B < 3:
            movimientos.append(self.B + 2)
        if self.B - 1 == self.A and self.B > 1:
            movimientos.append(self.B - 2)
        return movimientos

    def mover_A(self, nueva_posicion):
        self.A = nueva_posicion

    def mover_B(self, nueva_posicion):
        self.B = nueva_posicion



def generar_arbol(tablero, nivel, G):
    if nivel == 6:
        return
    elif nivel == -1:
        G.add_node(tablero)
        generar_arbol(tablero, 0, G)
        tablero.distancia = evaluarDistancia(G, tablero, nivel, 'max')
        print("nodo: " + str(tablero) + " distancia: " + str(tablero.distancia))

    elif nivel % 2 == 0:  # Es el turno de A en niveles pares
        movimientos = tablero.movimientos_posibles_A()
        for movimiento in movimientos:
            nuevo_tablero = Tablero(movimiento, tablero.B)
            G.add_edge(tablero, nuevo_tablero)
            generar_arbol(nuevo_tablero, nivel + 1, G)
            nuevo_tablero.distancia = evaluarDistancia(G, nuevo_tablero, nivel, 'min')
            print("nodo: " + str(nuevo_tablero) + " distancia: " + str(nuevo_tablero.distancia))
    else:  # Es el turno de B en niveles impares
        movimientos = tablero.movimientos_posibles_B()
        for movimiento in movimientos:
            nuevo_tablero = Tablero(tablero.A, movimiento)
            G.add_edge(tablero, nuevo_tablero)
            generar_arbol(nuevo_tablero, nivel + 1, G)
            nuevo_tablero.distancia = evaluarDistancia(G, nuevo_tablero, nivel, 'max')
            print("nodo: " + str(nuevo_tablero) + " distancia: " + str(nuevo_tablero.distancia))

def evaluarDistancia (G, nodo, nivel, turno):
    if nivel == 5:
        return nodo.evaluacion()
    elif turno == "max":
        return max(hijo.distancia for hijo in list(G.successors(nodo)))
    else:
        return min(hijo.distancia for hijo in list(G.successors(nodo)))

# Crear el grafo
G = nx.DiGraph()
# Generar árbol de búsqueda
tablero_inicial = Tablero(0, 4)
generar_arbol(tablero_inicial, -1, G)
print("Número de nodos en el árbol:", G.number_of_nodes())
pos = nx.spring_layout(G, scale=20)  # increase scale to lengthen edges
nx.draw_networkx_nodes(G, pos, node_size=300)  # reduce node size
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=6)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')  # reduce font size
plt.axis('off')
plt.show()
