import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler o arquivo CSV
estoque = pd.read_csv("estoque.csv")

# 2. Exibir os dados
print("Estoque atual de livros de terror:\n")
print(estoque)

# 3. Filtrar livros com estoque baixo (menor ou igual a 3 unidades)
estoque_baixo = estoque[estoque["Quantidade"] <= 3]

# 4. Gerar gráfico de barras dos livros com estoque baixo
plt.figure(figsize=(10, 6))
plt.bar(estoque_baixo["Título"], estoque_baixo["Quantidade"], color="darkred")
plt.xlabel("Título do Livro")
plt.ylabel("Quantidade em Estoque")
plt.title("Livros com Estoque Baixo na Biblioteca")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# 5. Salvar gráfico como imagem
plt.savefig("estoque_baixo.png")
plt.show()
