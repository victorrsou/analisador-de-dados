# Carregamento de um arquivo CSV ou JSON com dados de alunos
import pandas as pd
from TratamentoCsv import tratamentoCsv
from TratamentoJson import tratamentoJson

def iniciarApp():
    while True:
        try:
            # Solicita a entrada do usuário
            opcaoArquivo = int(input("Informe se deseja inserir um arquivo CSV ou JSON para analisar os dados (Digite '1' para JSON ou '2' para CSV): "))
            
            # Verifica a opção usando match-case
            match opcaoArquivo:
                case 1:
                    print("Você escolheu analisar dados no formato JSON.")
                    tratamentoJson()
                    # Insira aqui a lógica para tratar arquivos JSON
                case 2:
                    print("Você escolheu analisar dados no formato CSV.")
                    tratamentoCsv()
                    # Insira aqui a lógica para tratar arquivos CSV
                case _:
                    print("Opção inválida. Por favor, escolha '1' para JSON ou '2' para CSV.")
                    continue  # Permite ao usuário tentar novamente
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir um número inteiro.")

        # Pergunta ao usuário se deseja executar novamente
        executar_novamente = input("Deseja executar o programa novamente? (S/N): ").strip().lower()
        if executar_novamente != 's':
            print("Encerrando a aplicação. Até a próxima!")
            break



# Chama a função principal para iniciar a aplicação
iniciarApp()