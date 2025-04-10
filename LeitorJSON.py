import pandas as pd

def leitorJSON():
    inputAlunos = input("Informe o diretório ou nome do arquivo em CSV (ou vazio para ./Students_Grading_Dataset.json): ") # Caminho do arquivo
    if inputAlunos == "":
        inputAlunos = "Students_Grading_Dataset.json"
    try:
        dados = pd.read_json(inputAlunos)
        print("Arquivo aberto com sucesso!")
        return dados
    except FileNotFoundError:
        print(f"O arquivo '{inputAlunos}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")