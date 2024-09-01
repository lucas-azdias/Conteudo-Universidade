import numpy as np
import matplotlib.pyplot as plt

class erdos_renyi_gnp:
    def __init__(self, n_vertices, prob):
        self.ordem = n_vertices
        self.tamanho = 0
        self.matriz_adj = np.zeros([n_vertices, n_vertices])

        for i in range(n_vertices - 1):
            for j in range(i + 1, n_vertices):
                rand = np.random.random()
                if rand < prob:
                    self.matriz_adj[i, j] = 1
                    self.matriz_adj[j, i] = 1
                    self.tamanho += 1
    
    def __str__(self):
        return f"GRAFO COM {self.ordem} NÓS E {self.tamanho} ARRESTAS."

    def get_graus(self):
        graus = []
        for i in range(self.ordem):
            graus.append(np.sum(self.matriz_adj[i]))
        return graus

g = erdos_renyi_gnp(5000, 0.3)
print(g)

graus = g.get_graus()
media = np.mean(graus)
plt.figure(figsize=(5, 2))
plt.title("Distribuição de graus do modelo Erdos-Renyi")
plt.hist(graus, bins=30, color='skyblue', edgecolor='black')
plt.axvline(x=media, color='red', linestyle='dashed', label=f'Média {media}')
plt.xlabel('Grau')
plt.ylabel('Frequência')
plt.show()

# ---------------------------------------------------------------------------------


class erdos_renyi_gnm:
    def __init__(self, n_vertices, n_arrestas):
        self.ordem = n_vertices
        self.tamanho = 0
        self.matriz_adj = np.zeros([n_vertices, n_vertices])

        while n_arrestas > 0:
            i = np.random.randint(0, n_vertices)
            j = np.random.randint(0, n_vertices)
            while j == i:
                j = np.random.randint(0, n_vertices)
            self.matriz_adj[i, j] = 1
            self.matriz_adj[j, i] = 1
            self.tamanho += 1
            n_arrestas -= 1
    
    def __str__(self):
        return f"GRAFO COM {self.ordem} NÓS E {self.tamanho} ARRESTAS."

    def get_graus(self):
        graus = []
        for i in range(self.ordem):
            graus.append(np.sum(self.matriz_adj[i]))
        return graus


g = erdos_renyi_gnm(5000, 3000000)
print(g)

graus = g.get_graus()
media = np.mean(graus)
plt.figure(figsize=(5, 2))
plt.title("Distribuição de graus do modelo Erdos-Renyi")
plt.hist(graus, bins=30, color='skyblue', edgecolor='black')
plt.axvline(x=media, color='red', linestyle='dashed', label=f'Média {media}')
plt.xlabel('Grau')
plt.ylabel('Frequência')
plt.show()
