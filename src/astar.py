import copy
import matplotlib.pyplot as plt
import igraph as ig
import networkx as nx

import plotly.graph_objects as go

class Stack:
    def __init__(self):
        self.stacks = [['A', 'C', 'B'], [], []]
        self.oldstate = []
        self.f = -1

    def isMetaState(self):
        boole = False
        i = 0
        while not boole and i < 3:
            if self.stacks[i] == ['C', 'A', 'B']:
                boole = True
            i += 1
        return boole

    def getH(self):
        h = 0
        for stack in self.stacks:
            if stack:
                for i in range(0, len(stack)):
                    if i == 0:
                        if stack[i] != 'C':
                            h += 1
                    else:
                        if ord(stack[i-1]) - ord(stack[i]) != 1:
                            h += 1
        return h

    def __str__(self):
        pila_str = "\n".join(map(str, self.stacks))
	pila_str += "Valor de F: "
	pila_str += str(self.f)
        return pila_str

    def __eq__(self, s):
        return sorted(self.stacks) == sorted(s.stacks) and self.f == s.f

    def addnewstate(self, state):
        self.oldstate.append(sorted(state))


    def is_valid_state(self):
        return sorted(self.stacks) not in self.oldstate
    def setf (self, f):
        self.f = f

    def generate_states(self):
        states = []
        for i in range(3):  # Iterar sobre las stacks
            if self.stacks[i]:
                for j in range(3):  # Iterar sobre las stacks destino
                    if j != i:  # Evitar mover a la misma Stack
                        if not self.stacks[j] or len(self.stacks[j]) < 3:
                            oldstate = copy.deepcopy(self.stacks)
                            letter = self.stacks[i].pop()  # Sacar la letra de la Stack origen
                            self.stacks[j].append(letter)  # Agregar la letra a la Stack destino
                            newstate = copy.copy(self)
                            newstate.addnewstate(oldstate)
                            if newstate.is_valid_state() and newstate not in states:
                                states.append(newstate)
                            # Revertir el movimiento (volver a colocar la letra en la Stack origen)
                            self.stacks[j].pop()
                            self.stacks[i].append(letter)
        return states

    def __copy__(self):
        new_instance = Stack()
        new_instance.stacks = [stack[:] for stack in self.stacks]
        new_instance.oldstate = copy.deepcopy(self.oldstate)
        return new_instance

    def __hash__(self):
        # Convertir el estado de la Stack en una tupla y obtener su hash
        return hash(tuple(map(tuple, self.stacks)))

    def a_star_search(self):
        G = nx.DiGraph()
        open_list = [(self, 0)]  # Lista abierta: (estado, costo total)
        closed_list = set()  # Lista cerrada

        while open_list:
            current_state, g = min(open_list, key=lambda x: x[1] + x[0].getH())  # Extrae el estado con el menor f
            open_list.remove((current_state, g))
            print("Estado actual:")
            print(current_state)
            h = current_state.getH()  # Obtiene la heurística h
            f = g + h  # Calcula el costo total f
            print("Costo total (f):", f)
            print("Heurística (h*):", h)
            print()
            current_state.setf(f)
            if G.number_of_nodes() == 0:
                G.add_node(str(current_state))
            if current_state.isMetaState():
                return G

            closed_list.add(current_state)
            # Mostrar lista de estados expandidos
            print("Estados expandidos:")
            for state, _ in open_list:
                print(state)
            print()

            # Mostrar lista de estados visitados
            print("Estados visitados:")
            for state in closed_list:
                print(state)
            print()
            for successor_state in current_state.generate_states():
                g_successor = g + 1  # Incrementa g en 1 para cada sucesor
                h = successor_state.getH()
                f_successor = g_successor + h  # Costo total: g(n) + h(n)
                successor_state.setf(f_successor)
                if str(successor_state) not in G:
                    G.add_node(str(successor_state))
                    G.add_edge(str(current_state), str(successor_state))
                print("Sucesor:")
                print(successor_state)
                print("Costo total (f*):", f_successor)
                print("Heurística (h*):", h)
                print()
                found_state, found_f = next(((s, f) for s, f in open_list if s == successor_state), (None, None))
                if found_state is None or f_successor < found_f:
                    open_list.append((successor_state, g_successor))

        return None  # No se encontró solución



def draw_graph(G):
    pos = nx.spring_layout(G, scale=5)  # increase scale to lengthen edges

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=300)  # reduce node size

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=6)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')  # reduce font size

    plt.axis('off')
    plt.show()

G = Stack().a_star_search()
draw_graph(G)
