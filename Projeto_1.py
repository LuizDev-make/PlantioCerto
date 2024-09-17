# App PlantioCerto
# ALuno: Luiz Eduardo Nascimento, Projetos 1
# 1° Período BSI

import sys
import io
from datetime import datetime, timedelta
from os import system
from time import sleep
#solicita nome de usuário
usuario = input(("Digite seu nome:\n"))
lista_solo = [] # Armazena o tipo de solo escolhido na função solos

# Menu inicial
def home():
    system ('cls') or None
    print(f"{'='*30}")
    print(f"{'PLANTIO CERTO':^30}")
    print(f"{'='*30}")
    print(f"Bem-vindo, {usuario}!\n")
    print("[1] Colheitas")
    print("[2] Tipos de Solo")
    print("[3] Sugestão de Sementes")
    print("[4] Vendas")
    print("[5] Feedback")
    print("[6] Sair")
    print(f"{'='*30}")

# Histórico de colheitas
historico_colheitas = []
# Data de início da colheita (simulado)
inicio_colheita = datetime.now()
dias_para_colheita = 7  # Número de dias para a colheita

# Função de Colheita
def colheitas():
    system('cls') or None   
    while True:
        print(f"{'='*30}")
        print(f"{'COLHEITA':^30}")
        print(f"{'='*30}")
        print('\n1- Atualizar Data de Início\n2- Mostrar Detalhes da Colheita\n3- Ver Histórico de Colheitas\n4- Voltar\n')
        print(f"{'='*30}" )   
        
        try:
            colheita = int(input('Escolha uma opção:\n'))
            if colheita == 1:
                atualizar_colheita()
            elif colheita == 2:
                mostrar_detalhes_colheita()
            elif colheita == 3:
                system('cls') or None 
                if historico_colheitas:
                    print("Histórico de Colheitas:")
                    for i, (inicio, dias) in enumerate(historico_colheitas, start=1):
                        print(f"{i}. Início: {inicio.strftime('%Y-%m-%d %H:%M:%S')}, Dias para colheita: {dias}")
                else:
                    print("Nenhuma colheita registrada ainda.")
                    sleep(1)
                    system('cls') or None
            elif colheita == 4:
                system('cls') or None 
                return
            else:
                system('cls') or None
                print("colheita inválida! Tente novamente:\n")
                sleep(1)
                system('cls') or None
        except ValueError:
            erro()                    
# Função de colheita
def atualizar_colheita():
    system('cls') or None
    global inicio_colheita
    inicio_colheita = datetime.now()
    print("Data de início da colheita atualizada.")
    sleep(1)
    historico_colheitas.append((inicio_colheita, dias_para_colheita))
    system('cls') or None
    
# Mostra o detalhes da colheita
def mostrar_detalhes_colheita():
    system('cls') or None
    global inicio_colheita
    dias_restantes = (inicio_colheita + timedelta(days=dias_para_colheita) - datetime.now()).days
    print(f"\nDetalhes da Colheita:")
    print(f"Data de início: {inicio_colheita.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Dias restantes para a colheita: {max(dias_restantes, 0)}")
    print(f"Tipo de solo escolhido: {', '.join(lista_solo) if lista_solo else 'Nenhum'}\n")
    


# Função de Tipos de solo   
def solos():  
    while True:
        system('cls') or None
        print(f"{'='*30}")
        print(f"{'SOLOS':^30}")
        print(f"{'='*30}")
        print("\nEscolha o tipo de solo\n1- Massapê\n2- Salmourão\n3- Sair")
        print(f"{'='*30}")
        
        try:
            solo = int(input("Escolha um número:\n"))
            if solo == 1:
                system('cls') or None # Limpa o Prompt
                print(f"\n\nUsuário: {usuario}\nTipo de solo: Massapê")
                lista_solo.append('Massapê')
                sleep(2) # Depois de 2 segundos ele limpa o terminal e retorna ao HOME
                system('cls') or None 
                break
            elif solo == 2:
                system('cls') or None 
                print(f"\n\nUsuário: {usuario}\nTipo de solo: Salmourão")
                lista_solo.append('Salmourão')
                sleep(2)
                system('cls') or None 
                break
            elif solo == 3: 
                system('cls') or None 
                return
            else:
                system('cls') or None
                print("Opção inválida! Tente novamente.")
                sleep(1)
                system('cls') or None
        except ValueError:
            erro()
        

# Função de Sugestão de sementes
def sementes():
    system('cls') or None
    print(f'{'='*30}')
    print(f'{'SEMENTES':^30}')
    print(f"{'='*30}")
    print('1 - Feijão')
    print('2 - Milho')
    print('3 - Batata-doce')
    print('4 - Macaxeira')
    print('5 - Sair')
    print(f'{'='*30}')
    
    while True:
        try:
            semente = int(input('\n\nEscolha uma Opção:\n'))
            if semente == 1:
                system ('cls') or None
                ler_feijao()
            elif semente == 2:
                system ('cls') or None
                ler_milho()
            elif semente == 3:
                system ('cls') or None
                ler_batatadoce()
            elif semente == 4:
                system ('cls') or None
                ler_macaxeira()
            elif semente == 5:
                system('cls') or None 
                return main()
            else:
                system('cls') or None
                print("Opção inválida! Tente novamente.")
                sleep(1)
                system('cls') or None
        except ValueError:
            erro()


def ler_feijao():
    with io.open ('feijao.txt','r', encoding='utf-8') as feijao:
        print(feijao.read())
        retornar()
               
               
def ler_milho():
    with io.open ('milho.txt','r', encoding='utf-8') as milho:
        print(milho.read())
        retornar()
        
        
def ler_batatadoce():
    with io.open ('batatadoce.txt','r', encoding='utf-8') as batata:
        print(batata.read())
        retornar()
        
def ler_macaxeira():
    with io.open ('macaxeira.txt','r', encoding='utf-8') as macaxeira:
        print(macaxeira.read())
        retornar()
        
        
        
# dicionário para armazenar a tabela de vendas (produto, preço)
tabela_vendas = [
    {'produto': 'Feijão', 'preço': 5.00},
    {'produto': 'Milho', 'preço': 3.50},
    {'produto': 'Batata Doce', 'preço': 4.00}
]

#função vendas
def vendas():
    while True:
        system('cls') or None
        print(f"{'='*30}")
        print(f"{'VENDAS':^30}")
        print(f"{'='*30}")
        print("\n1 - Exibir Tabela de Vendas\n2 - Adicionar Produto\n3 - Atualizar Preço de Produto\n4 - Remover Produto\n5 - Sair para o Menu Principal\n")
        print(f"{'='*30}")
        try:
            opcao_vendas = int(input("Escolha uma opção:\n"))
            
            if opcao_vendas == 1:
                system('cls') or None
                exibir_tabela_vendas()
            elif opcao_vendas == 2:
                system('cls') or None
                adicionar_produto()
            elif opcao_vendas == 3:
                system('cls') or None
                atualizar_preco()
            elif opcao_vendas == 4:
                system('cls') or None
                remover_produto()
            elif opcao_vendas == 5:
                system('cls') or None
                return
            else:
                system('cls') or None
                print("Opção inválida! Tente novamente.")
                sleep(1)
                system ('cls') or None
        except ValueError:
            erro()

# Função para exibir a tabela de vendas
def exibir_tabela_vendas(): 
    if tabela_vendas:
        print("\nTabela de Vendas:")
        for i, item in enumerate(tabela_vendas, start=1):
            print(f"{i}. Produto: {item['produto']}, Preço: R${item['preço']:.2f}")
        enter()
    else:
        print("Tabela de vendas está vazia.")
        enter()
        
# Função separada pra mostrar a tabela vendas     
def tabela_venda():
    if tabela_vendas:
        print("\nTabela de Vendas:")
        for i, item in enumerate(tabela_vendas, start=1):
            print(f"{i}. Produto: {item['produto']}, Preço: R${item['preço']:.2f}")
    else:
        print("Tabela de vendas está vazia.")
        enter()

# Função para adicionar um novo produto à tabela de vendas
def adicionar_produto():
    while True:
        produto = input("Digite o nome do produto a ser adicionado:\n").strip()

        if not produto:
            system ('cls') or None
            print("Erro: O nome do produto não pode estar vazio. Por favor, digite um nome válido.")
            sleep(1)
            system ('cls') or None
            continue

        if not produto.replace(' ', '').isalpha():
            system ('cls') or None
            print("Erro: O nome do produto deve conter apenas letras. Por favor, digite um nome válido.\n")
            sleep(1)
            system ('cls') or None
            continue

        while True:
            try:
                preco = float(input(f"Digite o preço para '{produto.capitalize()}':\n"))
                if preco < 0:
                    system ('cls') or None
                    print("Erro: O preço não pode ser negativo. Por favor, digite um valor válido.\n")
                    sleep(1)
                    system ('cls') or None
                    continue
                tabela_vendas.append({"produto": produto.capitalize(), "preço": preco})
                system ('cls') or None
                print(f"Produto '{produto.capitalize()}' adicionado com sucesso!\n")
                sleep(1)
                system ('cls') or None
                return
            except ValueError:
                system ('cls') or None
                print("Erro: O preço deve ser um número. Tente novamente.\n")
                sleep(1)
                system ('cls') or None

# Função para atualizar o preço de um produto existente
def atualizar_preco():
    if not tabela_vendas:
        print("A tabela de vendas está vazia.")
        enter()
        return

    tabela_venda()
    try:
        opcao_produto = int(input("\nDigite o número do produto que deseja atualizar (ou digite 0 para voltar):\n"))
        if 1 <= opcao_produto <= len(tabela_vendas):
            while True:
                try:
                    novo_preco = float(input(f"Digite o novo preço para {tabela_vendas[opcao_produto - 1]['produto']}:\n"))
                    if novo_preco < 0:
                        system ('cls') or None
                        print("Erro: O preço não pode ser negativo. Tente novamente.")
                        sleep(1)
                        system ('cls') or None
                        continue
                    tabela_vendas[opcao_produto - 1]["preço"] = novo_preco
                    system ('cls') or None
                    print("Preço atualizado com sucesso!")
                    sleep(1)
                    system ('cls') or None
                    break
                except ValueError:
                    system ('cls') or None
                    print("Erro: O preço deve ser um número. Tente novamente.")
                    sleep(1)
                    system('cls') or None
        elif opcao_produto == 0:
            return
        else:
            system('cls') or None
            print("Opção inválida! Tente novamente.")
            sleep(1)
            system('cls') or None
    except ValueError:
        erro()
        return atualizar_preco()

# Função para remover um produto da tabela de vendas
def remover_produto():
    if not tabela_vendas:
        print("A tabela de vendas está vazia.")
        enter()
        return

    tabela_venda()
    try:
        opcao_produto = int(input("Digite o número do produto que deseja remover (ou digite 0 para voltar):\n"))
        if 1 <= opcao_produto <= len(tabela_vendas):
            produto_removido = tabela_vendas.pop(opcao_produto - 1)
            system ('cls') or None
            print(f"Produto '{produto_removido['produto']}' removido com sucesso!")
            sleep(2)
        elif opcao_produto == 0:
            return
        else:
            system('cls') or None
            print("Opção inválida! Tente novamente.")
            sleep(1)
            system('cls') or None
    except ValueError:
        erro()
        return remover_produto()

# Função de Feedback
def sugestao():
 while True:
    system('cls') or None
    print(f"{'='*30}")
    print(f"{'FEEDBACK':^30}")
    print(f"{'='*30}")
    print("1 - Escrever Feedback")
    print("2 - Ver Feedbacks")
    print("3 - Sair")
    print(f"{'='*30}")
        
    try:
         colheita = int(input('Digite o número da opção:\n'))
         if colheita == 1:
                escrever_feedback()
         elif colheita == 2:
                ver_feedbacks()
         elif colheita == 3:
                system('cls') or None
                return
         else:
            system('cls') or None
            print("Opção inválida! Tente novamente.")
            sleep(1)
            system('cls') or None
    except ValueError:
            erro()


# Lista para armazenar feedbacks
feedbacks = []

# Funções destinadas a função feedback 
def escrever_feedback():
    system('cls') or None
    feedback = input("Digite seu feedback:\n")
    if feedback.strip() != "": 
        feedbacks.append(feedback) # Adiciona o feedback a lista
        system('cls') or None
        print("Feedback recebido com sucesso!")
        sleep(2)
    else:
        system('cls') or None
        print("Feedback não pode ser vazio!")
        sleep(1)
        system('cls') or None
        
def ver_feedbacks():
    system('cls') or None
    if feedbacks:
        print("Feedbacks recebidos:\n")
        for i, feedback in enumerate(feedbacks, start=1):
            print(f"{i}. {feedback}") # mostra o feedback sepradaos em sequência numérica
        while True:
            try:
                colheita = int(input("\nDigite o número do feedback que deseja visualizar mais detalhadamente (ou 0 para voltar):\n"))
                if colheita == 0:
                    return  # Retorna ao menu anterior
                elif 1 <= colheita <= len(feedbacks):
                    print(f"\nFeedback {colheita}: {feedbacks[colheita - 1]}") # Permite visualizar feedbacks específicos em detalhe.
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                system('cls') or None
                print("Entrada inválida! Digite um número.") #tratamento de erro caso escollha um valor que não existe em feedbacks
                sleep(1)
                system('cls') or None
                for i, feedback in enumerate(feedbacks, start=1):
                    print(f"{i}. {feedback}")
    else:
        system('cls') or None
        print("Nenhum feedback recebido ainda.")    
        sleep(1)
        system('cls') or None
        
# Função de Saída
def saida():
    system('cls') or None
    print("SAINDO...")
    sleep(0.5)
    print("     SAINDO...")
    sleep(0.5)
    print("         SAINDO...")
    sleep(0.5)
    print("             SAINDO...")
    sleep(0.5)
    print("                 SAINDO...")
    sleep(1)
    system('cls') or None
    sys.exit()
  
# Função de erro do sistema, caso digite valores incorret  
def erro():
    while True:
        system('cls') or None
        entrada = input('ERRO! Digite um valor numérico para voltar:\n')
        if entrada.isdigit():
            system('cls') or None
            return int(entrada)

# Função de tratamento de erro pra algumas funções que usam a tecla enter
def enter():
    while True:
        escollha = input("Pressione Enter para voltar:\n")

        # Verifica se a entrada é uma string vazia (ou seja, Enter foi pressionado)
        if escollha == "":
            break  # Sai do loop se a tecla Enter for pressionada corretamente
        else:
            system ('cls') or None
            print('Erro! Digite apenas Enter para voltar.\n')  # Exibe mensagem de erro
            sleep(1)
            system ('cls') or None
    
def retornar():
    while True:
        try:
            voltar = int(input('\nDigite 1 para voltar:\n'))
            if voltar == 1:
                return sementes()
            else:
                system('cls') or None
                print("Opção inválida! Tente novamente.")
                sleep(1)
                system('cls') or None
        except ValueError:
            erro()
            
# Função pra chamar as outras funções mais o tratamento de erros do sistema.
def main():
    while True:
        home()
        
        try:
            opcao = int(input('Escolha uma opção:\n'))
            system('cls') or None
            if opcao == 1:
                colheitas()
            elif opcao == 2:
                solos()
            elif opcao == 3:
                sementes()
            elif opcao == 4:
                vendas()
            elif opcao == 5:
                sugestao()
            elif opcao == 6:
                saida()
            else:
                print("Opção inválida. Tente novamente.")
                sleep(1)
                system('cls') or None
        except ValueError:
            erro()

system('cls') or None
if __name__ == '__main__':
    main()
            

