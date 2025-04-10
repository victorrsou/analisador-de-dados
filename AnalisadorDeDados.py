# Carregamento de um arquivo CSV ou JSON com dados de alunos
from TratamentoDados import tratamentoDados
from LeitorCSV import leitorCSV
from LeitorJSON import leitorJSON

def iniciarApp():
    while True:
        try:
            # Solicita a entrada do usuário
            opcaoArquivo = int(input("\nInforme se deseja inserir um arquivo CSV para analisar os dados (Digite '1' para ler CSV ou '2' para JSON): "))
              
            # Verifica a opção usando match-case
            match opcaoArquivo:
                case 1:
                    print("\nVocê escolheu analisar dados no formato CSV.")
                    dados = leitorCSV()
                    if dados is not None and not dados.empty:
                        tratamentoDados(dados)
                case 2:
                    print("\nVocê escolheu analisar dados no formato JSON.")
                    dados = leitorJSON()
                    if dados is not None and not dados.empty:
                        tratamentoDados(dados)
                case _:
                    print("Opção inválida. Por favor, escolha '1' para ler CSV ou '2' para JSON.")
                    continue  
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir um número inteiro.")

        # Pergunta ao usuário se deseja executar novamente
        executar_novamente = input("\nDeseja executar o programa novamente? (S/N): ").strip().lower()
        if executar_novamente != 's':
            print("Encerrando a aplicação. Até a próxima!")
            break



# Chama a função principal para iniciar a aplicação
iniciarApp()