# App PlantioCerto
# ALuno: Luiz Eduardo Nascimento, Projetos 1
# 1° Período BSI

import sys
from random import shuffle
from datetime import datetime, timedelta
import os
from time import sleep
#solicita nome de usuário
usuario = input(("Digite seu nome:\n"))
lista_solo = [] # Armazena o tipo de solo escolhido na função solos

# Menu inicial
def home():
    print('\n------------PLANTIO CERTO-----------------')
    print(f"Bem vindo, {usuario}!\n\n[1] COLHEITA\n[2] TIPOS DE SOLO\n[3] SUGESTÃO DE SEMENTES\n[4] VENDAS\n[5] FEEDBACK\n[6] SAIR")
    print('-----------------------------\n')
    

# Histórico de colheitas
historico_colheitas = []
# Data de início da colheita (simulado)
inicio_colheita = datetime.now()
dias_para_colheita = 7  # Número de dias para a colheita

# Função de Colheita
def colheitas():
    os.system('cls') or None   
    while True:
        try:
            colheita = int(input('\nCOLHEITA:\n\n1- Atualizar Data de Início\n2- Mostrar Detalhes da Colheita\n3- Ver Histórico de Colheitas\n4- Voltar\n\nEscolha uma opção:\n'))
            if colheita == 1:
                
                atualizar_colheita()
            elif colheita == 2:
                mostrar_detalhes_colheita()
            elif colheita == 3:
                os.system('cls') or None 
                if historico_colheitas:
                    print("Histórico de Colheitas:")
                    for i, (inicio, dias) in enumerate(historico_colheitas, start=1):
                        print(f"{i}. Início: {inicio.strftime('%Y-%m-%d %H:%M:%S')}, Dias para colheita: {dias}")
                else:
                    print("Nenhuma colheita registrada ainda.")
                    sleep(1)
                    os.system('cls') or None
            elif colheita == 4:
                os.system('cls') or None 
                return
            else:
                os.system('cls') or None
                print("colheita inválida! Tente novamente:\n")
                sleep(1)
                os.system('cls') or None
        except ValueError:
            erro()                    
# Função de colheita
def atualizar_colheita():
    os.system('cls') or None
    global inicio_colheita
    inicio_colheita = datetime.now()
    print("Data de início da colheita atualizada.")
    sleep(1)
    historico_colheitas.append((inicio_colheita, dias_para_colheita))
    os.system('cls') or None
    
# Mostra o detalhes da colheita
def mostrar_detalhes_colheita():
    os.system('cls') or None
    global inicio_colheita
    dias_restantes = (inicio_colheita + timedelta(days=dias_para_colheita) - datetime.now()).days
    print(f"\nDetalhes da Colheita:")
    print(f"Data de início: {inicio_colheita.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Dias restantes para a colheita: {max(dias_restantes, 0)}")
    print(f"Tipo de solo escolhido: {', '.join(lista_solo) if lista_solo else 'Nenhum'}\n")
    


# Função de Tipos de solo   
def solos():  
    while True:
        os.system('cls') or None
        try:
            solo = int(input("\n\nEscolha o tipo de solo:\n1- Massapê\n2- Salmourão\n3- Sair\n\nDigite um número:\n"))
            if solo == 1:
                os.system('cls') or None # Limpa o Prompt
                print(f"\n\nUsuário: {usuario}\nTipo de solo: Massapê")
                lista_solo.append('Massapê')
                sleep(2) # Depois de 2 segundos ele limpa o terminal e retorna ao HOME
                os.system('cls') or None 
                break
            elif solo == 2:
                os.system('cls') or None 
                print(f"\n\nUsuário: {usuario}\nTipo de solo: Salmourão")
                lista_solo.append('Salmourão')
                sleep(2)
                os.system('cls') or None 
                break
            elif solo == 3: 
                os.system('cls') or None 
                return
            else:
                os.system('cls') or None
                print("Opção inválida! Tente novamente.")
                sleep(1)
                os.system('cls') or None
        except ValueError:
            erro()
        

# Função de Sugestão de sementes
def sementes():
    os.system('cls') or None
    lista_sementes = ['feijão', 'batata doce', 'milho', 'cana-de-açúcar', 'macaxeira','manga','côco','abacaxi','algodão']
    shuffle(lista_sementes) # mistura a lista 
    print(f"SUGESTÃO DE SEMENTES:\n\nUsuário: {usuario}\nTipo de solo: {lista_solo}\n\n")
    sugestao = lista_sementes[:2] # mostra apenas 2 itens da lista por vez
    print(sugestao)
    while True:
        try:
            voltar = int(input('\n\nPara voltar digite 1.\n'))
            if voltar == 1:
                os.system('cls') or None 
                return
        except ValueError:
            erro()
 
# dicionário para armazenar a tabela de vendas (produto, preço)
tabela_vendas = [
    {'produto': 'Feijão', 'preço': 5.00},
    {'produto': "Milho", 'preço': 3.50},
    {'produto': 'Batata Doce', 'preço': 4.00}
]

#função vendas
def vendas():
    while True:
        os.system('cls') or None
        print("-----------------VENDAS-----------------\n")
        print("1 - Exibir Tabela de Vendas")
        print("2 - Adicionar Produto")
        print("3 - Atualizar Preço de Produto")
        print("4 - Remover Produto")
        print("5 - Sair para o Menu Principal\n")
        print('----------------------------------------\n')
        try:
            opcao_vendas = int(input("Escolha uma opção:\n"))
            
            if opcao_vendas == 1:
                os.system('cls') or None
                exibir_tabela_vendas()
            elif opcao_vendas == 2:
                os.system('cls') or None
                adicionar_produto()
            elif opcao_vendas == 3:
                os.system('cls') or None
                atualizar_preco()
            elif opcao_vendas == 4:
                os.system('cls') or None
                remover_produto()
            elif opcao_vendas == 5:
                os.system('cls') or None
                return
            else:
                os.system('cls') or None
                print("Opção inválida! Tente novamente.")
                sleep(1)
                os.system ('cls') or None
        except ValueError:
            erro()

# Função para exibir a tabela de vendas
def exibir_tabela_vendas():
    if tabela_vendas:
        print("\nTabela de Vendas:")
        for i, item in enumerate(tabela_vendas, start=1):
            print(f"{i}. Produto: {item['produto']}, Preço: R${item['preço']:.2f}")
        input("\nPressione Enter para voltar.\n")
    else:
        print("Tabela de vendas está vazia.")
        input("\nPressione Enter para voltar.")
        
# Função separada pra mostrar a tabela vendas     
def tabela_venda():
    if tabela_vendas:
        print("\nTabela de Vendas:")
        for i, item in enumerate(tabela_vendas, start=1):
            print(f"{i}. Produto: {item['produto']}, Preço: R${item['preço']:.2f}")
    else:
        print("Tabela de vendas está vazia.")
        input("\nPressione Enter para voltar.")

# Função para adicionar um novo produto à tabela de vendas
def adicionar_produto():
    while True:
        produto = input("Digite o nome do produto a ser adicionado:\n").strip()

        if not produto:
            os.system ('cls') or None
            print("Erro: O nome do produto não pode estar vazio. Por favor, digite um nome válido.")
            sleep(1)
            os.system ('cls') or None
            continue

        if not produto.replace(' ', '').isalpha():
            os.system ('cls') or None
            print("Erro: O nome do produto deve conter apenas letras. Por favor, digite um nome válido.\n")
            sleep(1)
            os.system ('cls') or None
            continue

        while True:
            try:
                preco = float(input(f"Digite o preço para '{produto.capitalize()}':\n"))
                if preco < 0:
                    os.system ('cls') or None
                    print("Erro: O preço não pode ser negativo. Por favor, digite um valor válido.\n")
                    sleep(1)
                    os.system ('cls') or None
                    continue
                tabela_vendas.append({"produto": produto.capitalize(), "preço": preco})
                os.system ('cls') or None
                print(f"Produto '{produto.capitalize()}' adicionado com sucesso!\n")
                sleep(1)
                os.system ('cls') or None
                return
            except ValueError:
                os.system ('cls') or None
                print("Erro: O preço deve ser um número. Tente novamente.\n")
                sleep(1)
                os.system ('cls') or None

# Função para atualizar o preço de um produto existente
def atualizar_preco():
    if not tabela_vendas:
        print("A tabela de vendas está vazia.")
        input("\nPressione Enter para voltar.\n")
        return

    tabela_venda()
    try:
        opcao_produto = int(input("\nDigite o número do produto que deseja atualizar (ou digite 0 para voltar):\n"))
        if 1 <= opcao_produto <= len(tabela_vendas):
            while True:
                try:
                    novo_preco = float(input(f"Digite o novo preço para {tabela_vendas[opcao_produto - 1]['produto']}:\n"))
                    if novo_preco < 0:
                        os.system ('cls') or None
                        print("Erro: O preço não pode ser negativo. Tente novamente.")
                        sleep(1)
                        os.system ('cls') or None
                        continue
                    tabela_vendas[opcao_produto - 1]["preço"] = novo_preco
                    os.system ('cls') or None
                    print("Preço atualizado com sucesso!")
                    sleep(1)
                    os.system ('cls') or None
                    break
                except ValueError:
                    os.system ('cls') or None
                    print("Erro: O preço deve ser um número. Tente novamente.")
                    sleep(1)
                    os.system('cls') or None
        elif opcao_produto == 0:
            return
        else:
            os.system('cls') or None
            print("Opção inválida! Tente novamente.")
            sleep(1)
            os.system('cls') or None
    except ValueError:
        erro()
        return atualizar_preco()

# Função para remover um produto da tabela de vendas
def remover_produto():
    if not tabela_vendas:
        print("A tabela de vendas está vazia.")
        input("\nPressione Enter para voltar.")
        return

    tabela_venda()
    try:
        opcao_produto = int(input("Digite o número do produto que deseja remover (ou digite 0 para voltar):\n"))
        if 1 <= opcao_produto <= len(tabela_vendas):
            produto_removido = tabela_vendas.pop(opcao_produto - 1)
            os.system ('cls') or None
            print(f"Produto '{produto_removido['produto']}' removido com sucesso!")
            sleep(2)
        elif opcao_produto == 0:
            return
        else:
            os.system('cls') or None
            print("Opção inválida! Tente novamente.")
            sleep(1)
            os.system('cls') or None
    except ValueError:
        erro()
        return remover_produto()

# Função de Feedback
def sugestao():
 while True:
    os.system('cls') or None
    print("FEEDBACK \n\n")
    print("1 - Escrever Feedback")
    print("2 - Ver Feedbacks")
    print("3 - Sair")
        
    try:
         colheita = int(input('Digite o número da opção:\n'))
         if colheita == 1:
                escrever_feedback()
         elif colheita == 2:
                ver_feedbacks()
         elif colheita == 3:
                os.system('cls') or None
                return
         else:
            os.system('cls') or None
            print("Opção inválida! Tente novamente.")
            sleep(1)
            os.system('cls') or None
    except ValueError:
            erro()


# Lista para armazenar feedbacks
feedbacks = []

# Funções destinadas a função feedback 
def escrever_feedback():
    os.system('cls') or None
    feedback = input("Digite seu feedback:\n")
    if feedback.strip() != "": 
        feedbacks.append(feedback) # Adiciona o feedback a lista
        os.system('cls') or None
        print("Feedback recebido com sucesso!")
        sleep(2)
    else:
        os.system('cls') or None
        print("Feedback não pode ser vazio!")
        sleep(1)
        os.system('cls') or None
        
def ver_feedbacks():
    os.system('cls') or None
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
                os.system('cls') or None
                print("Entrada inválida! Digite um número.")
                sleep(1)
                os.system('cls') or None
    else:
        os.system('cls') or None
        print("Nenhum feedback recebido ainda.")    
        sleep(1)
        os.system('cls') or None
        
# Função de Saída
def saida():
    os.system('cls') or None
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
    os.system('cls') or None
    sys.exit()
  
# Função de erro do sistema, caso digite valores incorretos.  
def erro():
    while True:
        os.system('cls') or None
        entrada = input('ERRO! Digite um valor numérico para voltar:\n')
        if entrada.isdigit():
            os.system('cls') or None
            return int(entrada)
        
# Função pra chamar as outras funções mais o tratamento de erros do sistema.
def main():
    while True:
        home()
        
        try:
            opcao = int(input('Escolha uma opção:\n'))
            os.system('cls') or None
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
                os.system('cls') or None
        except ValueError:
            erro()

os.system('cls') or None
if __name__ == '__main__':
    main()
            

