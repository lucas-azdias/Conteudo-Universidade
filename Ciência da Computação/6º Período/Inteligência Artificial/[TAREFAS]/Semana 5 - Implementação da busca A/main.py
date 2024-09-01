from heapq import heappop, heappush

# Heuristic for the Romania problem.
# Values represent the line-straight to Bucharest (LSB)

heuristic_lsb = {'Arad': 366, 'Bucharest': 0, "Craiova": 160, "Drobeta": 242, 
                 "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
                 "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
                 "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193, "Sibiu": 253, 
                 "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind":374   
}

# Graph of Romania
romenia = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Oradea": 71, "Arad": 75},
    "Timisoara": {"Lugoj": 111, "Arad": 118},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Rimnicu Vilcea": 146, "Pitesti": 138, "Drobeta": 120,},
    "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146,},
    "Sibiu": {"Rimnicu Vilcea": 80, "Oradea": 151, "Fagaras": 99, "Arad": 140,},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Bucharest": {"Urziceni": 85, "Pitesti": 101, "Giurgiu": 90, "Fagaras": 211},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Vaslui": 142, "Hirsova": 98, "Bucharest": 85,},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}


# Função sucessora (estratégia de exploração)
def ucs(adj_list, start, goal):
    visited = [] # visitados
    fringe = [(0, start)] # fronteira (pilha com candidatos) com prioridades
    path = [(0, [start])] # path de resposta

    while fringe:
        cur_cost, cur_node = heappop(fringe) # em visitação
        cur_path = heappop(path)[1] # caminho atual até o em visitação

        # visita o nó
        if cur_node not in visited:
            visited.append(cur_node)

            # nó é final
            if cur_node == goal:
                return cur_path
            else:
                for neighbor, cost in adj_list[cur_node].items():
                    if neighbor not in visited:
                        # adiciona aos pendentes (fronteira)
                        heappush(fringe, (cur_cost + cost, neighbor))
                        # adiciona caminho
                        heappush(path, (cur_cost + cost, cur_path + [neighbor]))
    
    return None


# Função sucessora (estratégia de exploração)
def greedy_search(graph, heuristic, start, goal):
    visited = [] # visitados
    fringe = [(heuristic[start], start)] # fronteira (pilha com candidatos) com prioridades
    path = [(heuristic[start], 0, [start])] # path de resposta

    while fringe:
        _, cur_node = heappop(fringe) # em visitação
        _, cur_cost, cur_path = heappop(path) # caminho atual até o em visitação

        # visita o nó
        if cur_node not in visited:
            visited.append(cur_node)

            # nó é final
            if cur_node == goal:
                return cur_path
            else:
                for neighbor, cost in graph[cur_node].items():
                    if neighbor not in visited:
                        # adiciona aos pendentes (fronteira)
                        heappush(fringe, (heuristic[neighbor], neighbor))
                        # adiciona caminho
                        heappush(path, (heuristic[neighbor], cur_cost + cost, cur_path + [neighbor]))
    
    return None


# Função sucessora (estratégia de exploração)
def astar(graph, heuristic, start, goal):
    visited = [] # visitados
    fringe = [(heuristic[start], start)] # fronteira (pilha com candidatos) com prioridades
    path = [(heuristic[start], 0, [start])] # path de resposta

    while fringe:
        _, cur_node = heappop(fringe) # em visitação
        _, cur_cost, cur_path = heappop(path) # caminho atual até o em visitação

        # visita o nó
        if cur_node not in visited:
            visited.append(cur_node)

            # nó é final
            if cur_node == goal:
                return cur_path
            else:
                for neighbor, cost in graph[cur_node].items():
                    if neighbor not in visited:
                        # adiciona aos pendentes (fronteira)
                        heappush(fringe, (heuristic[neighbor] + cur_cost + cost, neighbor))
                        # adiciona caminho
                        heappush(path, (heuristic[neighbor] + cur_cost + cost, cur_cost + cost, cur_path + [neighbor]))
    
    return None


if __name__ == "__main__":
    print(ucs(romenia, "Arad", "Bucharest"))
    print(greedy_search(romenia, heuristic_lsb, "Arad", "Bucharest"))
    print(astar(romenia, heuristic_lsb, "Arad", "Bucharest"))
