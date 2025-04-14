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
            escolha = input("\nDigite o número da coluna desejada, ou X para sair: ")
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

        # O sistema deve produzir gráfico de dispersão para "horas de sono" x "nota final"
        while True:
            try:
                # Solicita entrada ao usuário
                opcaoGraficoDispersao = int(input("\nInforme se deseja exibir o gráfico de dispersão para 'horas de sono' x 'nota final' (Digite '1' para SIM ou '2' para NÃO): "))

                # Verifica opção
                match opcaoGraficoDispersao:
                    case 1:
                        dadosGraficox = dados['Sleep_Hours_per_Night']
                        dadosGraficoy = dados["Final_Score"]
                        plt.scatter(dadosGraficox, dadosGraficoy)
                        plt.title("Horas de Sono x Nota Final")
                        plt.xlabel("Horas de Sono")
                        plt.ylabel("Nota Final")
                        plt.show()
                        break

                    case 2:
                        # Realizar operação exibir gráfico de barras e gráfico de pizza
                        print("\nGerando gráfico de barras: Idade x Média das Notas Intermediárias...")

                        ## Gráfico de barras - Idade x média das notas intermediárias (Midterm_Score)
                        idades = dados['Age']
                        notas = dados['Midterm_Score']

                        ## Dicionário para somar e contar
                        somaNotas = {}
                        contagem = {}

                        for idade, nota in zip(idades, notas):
                            if idade in somaNotas:
                                somaNotas[idade] += nota
                                contagem[idade] += 1
                            else:
                                somaNotas[idade] = nota
                                contagem[idade] = 1

                        ## Calcular médias por idade
                        medias = {}
                        for idade in somaNotas:
                            medias[idade] = somaNotas[idade] / contagem[idade]

                        ## Organizar para o gráfico
                        idades_ordenadas = sorted(medias.keys())
                        medias_ordenadas = [medias[idade] for idade in idades_ordenadas]

                        ## Exibir gráfico de barras
                        plt.figure(figsize=(8, 5))
                        plt.bar(idades_ordenadas, medias_ordenadas)
                        plt.title("Idade x Média das Notas Intermediárias (Midterm_Score)")
                        plt.xlabel("Idade")
                        plt.ylabel("Média da Nota Intermediária")
                        plt.grid(axis='y')
                        plt.tight_layout()
                        plt.show()

                        ## Gráfico de pizza por faixa etária
                        print("\nGerando gráfico de pizza com a distribuição por faixas etárias...")

                        faixa1 = 0  # até 17
                        faixa2 = 0  # 18 a 21
                        faixa3 = 0  # 22 a 24
                        faixa4 = 0  # 25 ou mais

                        for idade in dados['Age']:
                            if idade <= 17:
                                faixa1 += 1
                            elif idade <= 21:
                                faixa2 += 1
                            elif idade <= 24:
                                faixa3 += 1
                            else:
                                faixa4 += 1

                        valores = [faixa1, faixa2, faixa3, faixa4]
                        rotulos = ['Até 17', '18 a 21', '22 a 24', '25 ou mais']

                        ## Geração do gráfico
                        plt.figure(figsize=(6, 6))
                        plt.pie(valores, labels=rotulos, autopct='%1.1f%%', startangle=90)
                        plt.title("Distribuição de Estudantes por Faixa Etária")
                        plt.axis('equal')
                        plt.show()

                        break  # ← Sai do while após mostrar os gráficos

                    case _:
                        print("Opção inválida. Por favor, escolha '1' para exibir o gráfico de dispersão ou '2' para não.")
                        continue

            except ValueError:
                print("Entrada inválida! Certifique-se de inserir um número inteiro.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
