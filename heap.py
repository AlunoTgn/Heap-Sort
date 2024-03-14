import time
import random
import heapq
import math

def sqrtsort_quadratico(A):
  """
  Ordena o vetor A usando o método de ordenação por seleção de raiz quadrada com ordenação quadrática nas partições.

  Args:
      A (list): Vetor a ser ordenado.

  Returns:
      None.
  """
  n = len(A)
  k = n // math.floor(math.sqrt(n))

  for i in range(k):
    inicio = i * math.floor(math.sqrt(n))
    fim = min(inicio + math.floor(math.sqrt(n)), n)
    maior = A[inicio]

    for j in range(inicio + 1, fim):
      if A[j] > maior:
        maior = A[j]

    A[inicio] = maior

  for i in range(k):
    inicio = i * math.floor(math.sqrt(n))
    fim = min(inicio + math.floor(math.sqrt(n)), n)

    for j in range(inicio + 1, fim):
      for k in range(j + 1, fim):
        if A[j] > A[k]:
          A[j], A[k] = A[k], A[j]

def sqrtsort_heap(A):
  """
  Ordena o vetor A usando o método de ordenação por seleção de raiz quadrada com Heap.

  Args:
      A (list): Vetor a ser ordenado.

  Returns:
      None.
  """
  n = len(A)
  H = A.copy()

  for i in range(n):
    if i < math.floor(math.sqrt(n)):
      heapq.heappush(H, A[i])
    else:
      if A[i] > heapq.heappop(H):
        A[i] = heapq.heappop(H)
        heapq.heappush(H, A[i])

def main():
  """
  Função principal do programa.
  """
  n = 10000  # Tamanho do vetor
  A = random.sample(range(n), n)

  # Medição do tempo de ordenação com método quadrático
  inicio_quadratico = time.time()
  sqrtsort_quadratico(A.copy())
  fim_quadratico = time.time()
  tempo_quadratico = fim_quadratico - inicio_quadratico

  # Medição do tempo de ordenação com Heap
  inicio_heap = time.time()
  sqrtsort_heap(A.copy())
  fim_heap = time.time()
  tempo_heap = fim_heap - inicio_heap

  # Impressão dos resultados
  print("Tamanho do vetor:", n)
  print("Tempo de ordenação (Método Quadrático):", tempo_quadratico)
  print("Tempo de ordenação (Heap):", tempo_heap)

if __name__ == "__main__":
  main()