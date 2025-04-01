import pandas as pd

def tratamentoJson():
    inputAlunos = input("Informe o diretório ou nome do arquivo em JSON: ") # Caminho do arquivo
    inputAlunos = "Students_Grading_Dataset.json"
    try:
        return
        # Exibir a quantidade de dados carregados (número de linhas no DataFrame)

        # Exibir a quantidade de homens e mulheres

        # Exibir quantos registros sem dados sobre a educação dos país.

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