import pandas as pd

def tratamentoCsv():
    inputAlunos = input("Informe o diretório ou nome do arquivo em CSV (ou vazio para ./Students_Grading_Dataset.csv): ") # Caminho do arquivo
    if inputAlunos == "":
        inputAlunos = "Students_Grading_Dataset.csv"
    try:
        dados = pd.read_csv(inputAlunos)
        print("Arquivo aberto com sucesso!")

        # Exibir a quantidade de dados carregados (número de linhas no DataFrame)
        print(f"Quantidade de dados carregados: {dados.shape[0]}")

        # Exibir a quantidade de homens e mulheres
        cleanDados = dados.dropna(subset=["Gender"])
        qtdHomens = cleanDados[cleanDados["Gender"] == "Male"].shape[0]
        qtdMulheres = cleanDados[cleanDados["Gender"] == "Female"].shape[0]

        print(f"Quantidade de homens: {qtdHomens}")
        print(f"Quantidade de mulheres: {qtdMulheres}")

        # Exibir quantos registros sem dados sobre a educação dos país.
        qtdSemDadosParentEducationLevel = dados["Parent_Education_Level"].isna().sum()
        print(f"Quantidade de registros sem dados sobre a educação dos pais: {qtdSemDadosParentEducationLevel}")

        # Remover os registros que tem a educação do país vazios.
        # Alterar os dados de presença (Attendance) que estão null para a mediana.
        # Apresentar o somatório de Attendance

        # O usuário pode escolher uma das colunas (Inserção de dado numérico) e o sistema deve apresentar: media, mediana, moda, desvio padrão dos dados daquela coluna.

        # O sistema deve produzir gráfico de dispersão para "horas de sono" x "nota final"
        # Gráfico de barras - Idade x média das notas intermediárias (midterm_Score)
        # Gráfico de pizza para as idades (Agrupadas: até 17 ;18 a 21; 22 a 24; 25 ou mais)

    except FileNotFoundError:
        print(f"O arquivo '{inputAlunos}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")