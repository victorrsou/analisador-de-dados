import pandas as pd

def leitorCSV():
    inputAlunos = input("\nInforme o diretório ou nome do arquivo em CSV (ou vazio para ./Students_Grading_Dataset.csv): ") # Caminho do arquivo
    if inputAlunos == "":
        inputAlunos = "Students_Grading_Dataset.csv"
    try:
        dados = pd.read_csv(inputAlunos)
        print("\nArquivo aberto com sucesso!")
        return dados
    except FileNotFoundError:
        print(f"O arquivo '{inputAlunos}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")