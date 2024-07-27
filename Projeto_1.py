# App PlantioCerto
# ALuno: Luiz Eduardo Nascimento, Projetos 1
# 1° Período BSI

import sys
from random import shuffle
from datetime import datetime, timedelta
#solicita nome de usuário
usuario = input(("Digite seu nome:\n"))
lista_solo = [] # Armazena o tipo de solo escolhido na função solos

# Menu inicial
def home():
    print('\n-----------------------------')
    print(f"Bem vindo, {usuario}!\n\n[1] COLHEITA\n[2] TIPOS DE SOLO\n[3] SUGESTÃO DE SEMENTES\n[4] VENDAS\n[5] FEEDBACK\n[6] SAIR")
    print('-----------------------------\n')
    

# Histórico de colheitas
historico_colheitas = []
# Data de início da colheita (simulado)
inicio_colheita = datetime.now()
dias_para_colheita = 7  # Número de dias para a colheita

# Função de Colheita
def colheitas():
    while True:
        try:
            colheita = int(input('COLHEITA:\n\n1- Atualizar Data de Início\n2- Mostrar Detalhes da Colheita\n3- Ver Histórico de Colheitas\n4- Voltar\n\nEscolha uma opção:\n'))
            if colheita == 1:
                atualizar_colheita()
            elif colheita == 2:
                mostrar_detalhes_colheita()
            elif colheita == 3:
                if historico_colheitas:
                    print("Histórico de Colheitas:")
                    for i, (inicio, dias) in enumerate(historico_colheitas, start=1):
                        print(f"{i}. Início: {inicio.strftime('%Y-%m-%d %H:%M:%S')}, Dias para colheita: {dias}")
                else:
                    print("Nenhuma colheita registrada ainda.")
            elif colheita == 4:
                return
            else:
                erro("colheita inválida! Tente novamente:\n")
        except ValueError:
            erro()                    
 
# Função de colheita
def atualizar_colheita():
    global inicio_colheita
    inicio_colheita = datetime.now()
    print("Data de início da colheita atualizada.")
    historico_colheitas.append((inicio_colheita, dias_para_colheita))

def mostrar_detalhes_colheita():
    global inicio_colheita
    dias_restantes = (inicio_colheita + timedelta(days=dias_para_colheita) - datetime.now()).days
    print(f"\nDetalhes da Colheita:")
    print(f"Data de início: {inicio_colheita.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Dias restantes para a colheita: {max(dias_restantes, 0)}")
    print(f"Tipo de solo escolhido: {', '.join(lista_solo) if lista_solo else 'Nenhum'}")



# Função de Tipos de solo   
def solos():  
    while True:
        try:
            solo = int(input("\n\ncolheita o tipo de solo:\n1- Latossolo\n2- Cambriossolo\n3- Sair\n\nDigite um número:\n"))
            if solo == 1:
                print(f"\n\nUsuário: {usuario}\nTipo de solo: Latossolo")
                lista_solo.append('Latossolo')
                home()
                break
            elif solo == 2:
                print(f"\n\nUsuário: {usuario}\nTipo de solo: Cambriossolo")
                lista_solo.append('Cambriossolo')
                home()
                break
            elif solo == 3:
                home()
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            erro()

# Função de Sugestão de sementes
def sementes():
    lista_sementes = ['feijão', 'batata doce', 'milho', 'cana-de-açúcar', 'macaxeira']
    shuffle(lista_sementes) # mistura a lista 
    print(f"SUGESTÃO DE SEMENTES:\n\nUsuário: {usuario}\nTipo de solo: {lista_solo}\n\n")
    sugestao = lista_sementes[:2] # mostra apenas 2 itens da lista por vez
    print(sugestao)
    while True:
        try:
            voltar = int(input('\n\nPara voltar digite 1.\n'))
            if voltar == 1:
                home()
                break
        except ValueError:
            erro()

# Função de vendas 
def vendas():
    print("VENDAS:\n\n")
    print('Tabela Fipe:')
    while True:
        try:
            opcao_vendas = int(input('\n\n\n1- Atualizar Tabela\n2 - Sair\n\ncolheita uma opção:\n'))
            if opcao_vendas == 1:
                print('Atualizando Tabela...')
                home()
                break
            elif opcao_vendas == 2:
                home()
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            erro()

# Função de Feedback
def sugestao():
 while True:
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
                home()
                break
         else:
            erro("colheita inválida! Tente novamente:\n")
    except ValueError:
            erro("Entrada inválida! Tente novamente:\n")


# Lista para armazenar feedbacks
feedbacks = []

# Funções destinadas a função feedback 
def escrever_feedback():
    feedback = input("Digite seu feedback:\n")
    if feedback.strip() != "": 
        feedbacks.append(feedback) # Adiciona o feedback a lista
        print("Feedback recebido com sucesso!")
    else:
        print("Feedback não pode ser vazio!")
        
def ver_feedbacks():
    if feedbacks:
        print("Feedbacks recebidos:")
        for i, feedback in enumerate(feedbacks, start=1):
            print(f"{i}. {feedback}") # mostra o feedback sepradaos em sequência numérica
        while True:
            try:
                colheita = int(input("\nDigite o número do feedback que deseja visualizar mais detalhadamente (ou 0 para voltar):\n"))
                if colheita == 0:
                    return  # Retorna ao menu anterior
                elif 1 <= colheita <= len(feedbacks):
                    print(f"\nFeedback {colheita}: {feedbacks[colheita - 1]}")
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida! Digite um número.")
    else:
        print("Nenhum feedback recebido ainda.")    
        
        
# Função de Saída
def saida():
    print("SAINDO...\t\t")
    sys.exit()
  
# Função de erro do sistema, caso digite valores incorretos.  
def erro():
    while True:
        entrada = input('ERRO! Digite um valor válido:\n')
        if entrada.isdigit():
            return int(entrada)
    
        


def main():
    while True:
        home()
        try:
            opcao = int(input('colheita uma opção:\n'))
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
        except ValueError:
            erro()
            
if __name__ == '__main__':
    main()
            

