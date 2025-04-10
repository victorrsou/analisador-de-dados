import pandas as pd
import statistics

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

        # Exibir quantos registros sem dados sobre a educação dos país.
        qtdSemDadosParentEducationLevel = dados["Parent_Education_Level"].isna().sum()
        print(f"Quantidade de registros sem dados sobre a educação dos pais: {qtdSemDadosParentEducationLevel}")

        # Remover os registros que tem a educação do país vazios.
        dados.dropna(subset=["Parent_Education_Level"],inplace=True)
        # Alterar os dados de presença (Attendance) que estão null para a mediana.
        medianaPresenca = dados["Attendance (%)"].median()
        dados["Attendance (%)"].fillna(medianaPresenca, inplace=True)
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
        # Gráfico de barras - Idade x média das notas intermediárias (midterm_Score)
        # Gráfico de pizza para as idades (Agrupadas: até 17 ;18 a 21; 22 a 24; 25 ou mais)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")