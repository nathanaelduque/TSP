import numpy as np

class AlgoritmoGenetico:
    def __init__(self, matriz_distancias, n_individuos, taxa_mutacao, n_geracoes):
        self.matriz_distancias = matriz_distancias
        self.n_cidades = len(matriz_distancias)
        self.n_individuos = n_individuos
        self.taxa_mutacao = taxa_mutacao
        self.n_geracoes = n_geracoes
        self.populacao = np.zeros((n_individuos, self.n_cidades), dtype=int)
        for i in range(n_individuos):
            self.populacao[i] = np.random.permutation(self.n_cidades)

    def calcular_distancia(self, rota):
        distancia = 0
        for i in range(self.n_cidades - 1):
            cidade_atual = rota[i]
            proxima_cidade = rota[i + 1]
            distancia += self.matriz_distancias[cidade_atual][proxima_cidade]
        distancia += self.matriz_distancias[rota[-1]][rota[0]]
        return distancia

    def crossover(self, pai1, pai2):
        ponto_corte = np.random.randint(1, self.n_cidades)
        filho = np.zeros(self.n_cidades, dtype=int)
        filho[:ponto_corte] = pai1[:ponto_corte]
        for cidade in pai2:
            if cidade not in filho:
                filho[ponto_corte] = cidade
                ponto_corte += 1
                if ponto_corte == self.n_cidades:
                    ponto_corte = 0
        return filho

    def mutacao(self, individuo):
        if np.random.rand() < self.taxa_mutacao:
            idx1, idx2 = np.random.choice(self.n_cidades, 2, replace=False)
            individuo[idx1], individuo[idx2] = individuo[idx2], individuo[idx1]

    def evoluir(self):
        for geracao in range(self.n_geracoes):
            novos_individuos = []
            fitness = np.array([self.calcular_distancia(individuo) for individuo in self.populacao])
            melhor_individuo_idx = np.argmin(fitness)
            melhor_individuo = self.populacao[melhor_individuo_idx]
            novos_individuos.append(melhor_individuo)
            while len(novos_individuos) < self.n_individuos:
                pais_indices = np.random.choice(len(self.populacao), size=2, replace=False)
                pai1 = self.populacao[pais_indices[0]]
                pai2 = self.populacao[pais_indices[1]]
                filho = self.crossover(pai1, pai2)
                self.mutacao(filho)
                novos_individuos.append(filho)
            self.populacao = np.array(novos_individuos)
            melhor_distancia = self.calcular_distancia(melhor_individuo)
            print(f"Geração {geracao + 1}: Melhor Distância = {melhor_distancia:.2f}")
  
    def encontrar_melhor_solucao(self):
        fitness = np.array([self.calcular_distancia(individuo) for individuo in self.populacao])
        melhor_individuo_idx = np.argmin(fitness)
        melhor_individuo = self.populacao[melhor_individuo_idx]
        melhor_distancia = self.calcular_distancia(melhor_individuo)
        print("Melhor Solução Encontrada:")
        print("Rota:", melhor_individuo)
        print("Distância:", melhor_distancia)

if __name__ == "__main__":
    
    
    
    filename = "Tsp58_2.txt"
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    
    # Criar Metade da Matriz de Custos dada
    m58 = np.zeros([58,58])
    for i in range(0,len(m58)-1):
      for j in range(0,len(matrix[i])): 
          m58[i][i+j+1]=matrix[i][j]
    
    # Espelhar a Matriz de Custos
    for i in range(0,len(m58)):
      for j in range(0,len(m58)): 
        if i==j:
          m58[i][j]=0
        elif i < j:
          m58[j][i]=m58[i][j]
    print(m58)
    matriz_distancias=m58

    np.random.seed(42)
    algoritmo = AlgoritmoGenetico(matriz_distancias=matriz_distancias, n_individuos=800, taxa_mutacao=0.1, n_geracoes=10000)
    algoritmo.evoluir()
    algoritmo.encontrar_melhor_solucao()
