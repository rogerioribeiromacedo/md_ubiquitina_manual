# Importando bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd

#
# 01. Variáveis
#
tituloGrafico = "Pressão"
subTituloGrafico = "Equilíbrio NPT"
labelEixoX = "Tempo (passos)"
labelEixoY = "bar"

#
# 02. Dados
#
dados = np.loadtxt("npt_pressao.xvg", comments=("@", "#"))
valoresX, valoresY = dados[:, 0], dados[:, 1]
df = pd.DataFrame({"Tempo": valoresX, "Pressao": valoresY})
df["media_movel"] = df["Pressao"].rolling(window=10, min_periods=1).mean()

#
# 03. Tema do gráfico
#
sns.set_theme(style="white", palette="rocket")

#
# 04. Gráfico
#
fig, ax = plt.subplots(1, 1, figsize=(13, 7))

# Dados Originais
sns.lineplot(x=valoresX,
             y=valoresY,
             linewidth=1,
             color="#f6b48f",
             label="Pressão")

# Média móvel
sns.lineplot(x=valoresX,
             y=df["media_movel"],
             linewidth=1,             
             label="Média Móvel")

#
# 05. Limites para os valores dos eixos
#
x_min = -45
x_max = np.max(valoresX)
y_min = np.floor(np.min(valoresY)-50)  
y_max = np.ceil(np.max(valoresY)+50) 
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

#
# 06. Rótulo dos eixos e título do gráfico
#

# Eixo Y
ax.set_ylabel(labelEixoY,
              fontsize=18,
              weight="bold",
              labelpad=20)
# Eixo X
ax.set_xlabel(labelEixoX,
              fontsize=18,
              weight="bold",
              labelpad=20)

# Título/Subtitulo do gráfico
fig.suptitle(tituloGrafico,
             fontweight='bold',
             fontsize=22)
ax.set_title(subTituloGrafico,
             fontweight='bold',
             fontsize=14,
             pad=15)

#
# 07. Spines -> as linhas dos eixos (as bordas do gráfico)
#
for axis in ['bottom', 'left', 'top', 'right']:
    ax.spines[axis].set_linewidth(1.5)
    ax.spines[axis].set_color('0.2')
ax.spines['left'].set_bounds(y_min, y_max)
ax.spines['left'].set_position(('data', 0))
ax.spines['top'].set_position(('data', y_max))

#
# 08. Ticks
#  - length: comprimento; width: largura
#

# Traços
ax.tick_params(which='major',
               length=5.5,
               grid_alpha=0.5,
               width=1.5)
ax.tick_params(which='minor',
               length=3.5,
               grid_alpha=0.5,
               width=0.75)

# Eixo X
ax.xaxis.set_ticks_position('bottom')
ax.xaxis.set_minor_locator(ticker.MultipleLocator(500))
plt.xticks(size=10, weight='bold', color='0.2')     # Texto

# Eixo Y
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_minor_locator(ticker.MultipleLocator(50))
plt.yticks(size=10, weight='bold', color='0.2')     # Texto

# 
# 09. Gerando imagem
#
plt.savefig("em_energia_potencial.png", bbox_inches='tight', dpi=300, facecolor=ax.get_facecolor())

#
# 10. Exibindo gráfico
#
plt.show()
