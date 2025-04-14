import pandas as pd
from TratamentoDados import tratamentoDados

def leitorJSON():
    inputAlunos = input("\nInforme o diretório ou nome do arquivo em CSV (ou vazio para ./Students_Grading_Dataset.json): ") # Caminho do arquivo
    if inputAlunos == "":
        inputAlunos = "Students_Grading_Dataset.json"
    try:
        dados = pd.read_json(inputAlunos)
        print("\nArquivo aberto com sucesso!")
        return dados
    except FileNotFoundError:
        print(f"\nO arquivo '{inputAlunos}' não foi encontrado.")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

        
if __name__ == "__main__":
    dados = leitorJSON()
    if dados is not None:
        tratamentoDados(dados)