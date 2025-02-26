# Importando bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.ticker as ticker

def formato_brasileiro_float(x: np.ndarray, pos) -> np.ndarray:
    """
    Função que ajusta a exbição dos números.

    Parameters
    ----------
    x : numpy.ndarray
        Contém a lista de valores a serem formatado como brasileiro.

    Returns
    -------
    TYPE
        Array do tipo ndarray

    """
    return f'{x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


#
# 01. Variáveis
#
tituloGrafico = "Energia Potencial"
subTituloGrafico = "minimização"
labelEixoX = "Tempo (passos)"
labelEixoY = r"$kJ \cdot mol^{-1}$"

#
# 02. Dados
#
dados = np.loadtxt("em_energia_potencial.xvg", comments=("@", "#"))
valoresX, valoresY = dados[:, 0], dados[:, 1]

#
# 03. Tema do gráfico
#
sns.set_theme(style="white", palette="rocket")

#
# 04. Gráfico
#
fig, ax = plt.subplots(1, 1, figsize=(13, 7))
sns.lineplot(x=valoresX,
             y=valoresY,
             color="#f6b48f",
             linewidth=2,
             label="Energia")

#
# 05. Limites para os valores dos eixos
#
x_min = -45
x_max = np.max(valoresX)
y_min = np.floor(np.min(valoresY))  
y_max = np.ceil(np.max(valoresY)+50000) 
ax.set_xlim(x_min, x_max)
#ax.set_ylim(y_min, y_max)

#
# Imprimindo valores de mínimo e máximo dos eixos
#
print(f"Eixo X: {x_min:0.5f} - {x_max:0.5f}")
print(f"Eixo Y: {y_min:0.5f} - {y_max:0.5f}")

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
ax.set_title(f'{tituloGrafico}',
             fontweight='bold',
             pad=25,
             fontsize=24)
ax.text(0.5, 1.02,
        f'{subTituloGrafico}',
        transform=ax.transAxes,
        fontsize=14,
        ha='center')

#
# 07. Spines -> as linhas dos eixos (as bordas do gráfico)
#
for axis in ['bottom', 'left', 'top', 'right']:
    ax.spines[axis].set_linewidth(1.5)
    ax.spines[axis].set_color('0.2')
#ax.spines['left'].set_bounds(y_min, y_max)
#ax.spines['left'].set_position(('data', x_min))
#ax.spines['top'].set_position(('data', y_max))

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
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5000))
plt.yticks(size=10, weight='bold', color='0.2')     # Texto

# Aplicar a formatação brasileira ao eixo y
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formato_brasileiro_float))


#
# 09. Posiciona legenda
#
sns.move_legend(ax, "upper left",
                bbox_to_anchor=(0.75, 1),                
                fancybox=True,
                shadow=True,
                fontsize=10,
                title="Eixos",
                title_fontsize=10,
                title_fontweight='bold',
                labelspacing=1)

# Imprimindo menor valor de energia
plt.text(14000, -198500, r'$(-199.426,67\,kJ \cdot mol^{-1}) $', fontsize=12, ha='center', color="#35193e")

# 
# 10. Gerando imagem
#
plt.savefig("em_energia_potencial.png", bbox_inches='tight', dpi=300, facecolor=ax.get_facecolor())

#
# 12. Exibindo gráfico
#
plt.show()
