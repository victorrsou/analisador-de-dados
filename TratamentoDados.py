import pandas as pd
import statistics
from matplotlib import pyplot as plt

def tratamentoDados(dados: pd.DataFrame):
    try:
        # Exibir a quantidade de dados carregados (número de linhas no DataFrame)
        print(f"Quantidade de dados carregados: {len(dados)}")

        # Exibir a quantidade de homens e mulheres
        cleanDados = dados.dropna(subset=["Gender"])
        qtdHomens = len(cleanDados[cleanDados["Gender"] == "Male"])
        qtdMulheres = len(cleanDados[cleanDados["Gender"] == "Female"])
        print(f"Quantidade de homens: {qtdHomens}")
        print(f"Quantidade de mulheres: {qtdMulheres}")

        # Exibir quantos registros sem dados sobre a educação dos pais.
        qtdSemDadosParentEducationLevel = dados["Parent_Education_Level"].isna().sum()
        print(f"Quantidade de registros sem dados sobre a educação dos pais: {qtdSemDadosParentEducationLevel}")

        # Remover os registros que tem a educação do pais vazios.
        dados.dropna(subset=["Parent_Education_Level"], inplace=True)

        # Alterar os dados de presença (Attendance) que estão null para a mediana.
        medianaPresenca = dados["Attendance (%)"].median()
        dados.fillna(medianaPresenca, inplace=True)

        # Apresentar o somatório de Attendance
        somatorioPresenca = dados["Attendance (%)"].sum()
        print(f"O somatório de presença é: {somatorioPresenca}")

        # O usuário pode escolher uma das colunas (Inserção de dado numérico) e o sistema deve apresentar: media, mediana, moda, desvio padrão dos dados daquela coluna.
        print("\nSelecione a coluna para detalhar: ")
        colunas = dados.select_dtypes(include=['number']).columns
        for i, col in enumerate(colunas, 1):
            print(f"{i}: {col}")

        while True:
            escolha = input("\nDigite o número da coluna desejada, ou X para continuar: ")
            if escolha.lower() == "x":
                break
            try:
                escolha = int(escolha)
                if 1 <= escolha <= len(colunas):
                    coluna = colunas[escolha - 1]
                    media = dados[coluna].mean()
                    mediana = dados[coluna].median()
                    moda = statistics.mode(dados[coluna])
                    desvio_padrao = dados[coluna].std()

                    print(f"\nEstatísticas da coluna '{coluna}':")
                    print(f"Média: {media}")
                    print(f"Mediana: {mediana}")
                    print(f"Moda: {moda}")
                    print(f"Desvio Padrão: {desvio_padrao}")
                else:
                    print("Erro: Número inválido. Escolha um número da lista.")
            except ValueError:
                print("Erro: Entrada inválida. Digite um número.")

        input("\nAperte ENTER para apresentar os gráficos Horas de Sono x Nota Final, Idade x Média das Notas Intermediárias, Distribuição por Faixas Etárias: ")

        # Gráfico 1: Horas de Sono x Nota Final
        dadosGraficox = dados['Sleep_Hours_per_Night']
        dadosGraficoy = dados["Final_Score"]

        # Gráfico 2: Idade x Média das Notas Intermediárias
        idades = dados['Age']
        notas = dados['Midterm_Score']
        somaNotas = {}
        contagem = {}

        for idade, nota in zip(idades, notas):
            if idade in somaNotas:
                somaNotas[idade] += nota
                contagem[idade] += 1
            else:
                somaNotas[idade] = nota
                contagem[idade] = 1

        medias = {idade: somaNotas[idade] / contagem[idade] for idade in somaNotas}
        idades_ordenadas = sorted(medias.keys())
        medias_ordenadas = [medias[idade] for idade in idades_ordenadas]

        # Gráfico 3: Distribuição por Faixas Etárias
        faixa1 = sum(1 for idade in dados['Age'] if idade <= 17)
        faixa2 = sum(1 for idade in dados['Age'] if 18 <= idade <= 21)
        faixa3 = sum(1 for idade in dados['Age'] if 22 <= idade <= 24)
        faixa4 = sum(1 for idade in dados['Age'] if idade >= 25)
        valores = [faixa1, faixa2, faixa3, faixa4]
        rotulos = ['Até 17', '18 a 21', '22 a 24', '25 ou mais']

        # Configurar subplots
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        # Configurar o primeiro gráfico
        axes[0].scatter(dadosGraficox, dadosGraficoy)
        axes[0].set_title("Horas de Sono x Nota Final")
        axes[0].set_xlabel("Horas de Sono")
        axes[0].set_ylabel("Nota Final")

        # Configurar o segundo gráfico
        axes[1].bar(idades_ordenadas, medias_ordenadas)
        axes[1].set_title("Idade x Média das Notas Intermediárias")
        axes[1].set_xlabel("Idade")
        axes[1].set_ylabel("Média da Nota Intermediária")
        axes[1].grid(axis='y')
        axes[1].set_ylim(min(medias_ordenadas) - 3,max(medias_ordenadas) + 3)

        # Configurar o terceiro gráfico
        axes[2].pie(valores, labels=rotulos, autopct='%1.1f%%', startangle=90)
        axes[2].set_title("Distribuição por Faixa Etária")

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
