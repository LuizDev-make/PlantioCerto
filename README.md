# PlantioCerto

## Descrição do Projeto

O **PlantioCerto** é um aplicativo de linha de comando (CLI) desenvolvido para auxiliar agricultores e entusiastas da agricultura 
a gerenciar colheitas, vendas de produtos agrícolas, e receber feedbacks de clientes. O objetivo do aplicativo é fornecer ferramentas 
que ajudem no planejamento e execução de atividades relacionadas ao cultivo, desde o início da colheita até a venda dos produtos
no mercado.


## Funcionalidades

1. **Histórico de Colheitas**: Permite ao usuário registrar e visualizar o histórico de colheitas, bem como os dias restantes para a próxima colheita.
2. **Tipos de Solo**: Oferece ao usuário a possibilidade de selecionar entre diferentes tipos de solo adequados ao plantio.
3. **Sugestão de Sementes**: Sugere tipos de sementes (feijão, milho, batata-doce, macaxeira) com informações detalhadas sobre cada uma.
4. **Vendas**: Gerencia uma tabela de vendas onde o usuário pode adicionar, atualizar e remover produtos, além de exibir a tabela com os preços dos produtos à venda.
5. **Feedbacks**: Os usuários podem dar feedbacks sobre a aplicação e visualizar feedbacks de outros usuários.
6. **Sistema de Navegação Simples**: O menu principal oferece uma navegação intuitiva por todas as funcionalidades.


## Como Funciona

- **Histórico de Colheitas**: Permite ao usuário definir a data de início da colheita e verificar o tempo restante para a próxima colheita.
- **Solo**: Escolha entre solos de tipos diferentes (Massapê e Salmourão), o que impacta nas escolhas de sementes e na colheita.
- **Sugestão de Sementes**: A partir do tipo de solo escolhido, o sistema sugere as melhores sementes para plantar.
- **Vendas**: Gere uma tabela de vendas onde é possível adicionar produtos, definir preços, e gerenciar as vendas dos produtos cultivados.
- **Feedback**: Envie sugestões ou críticas e visualize as opiniões de outros usuários.


## Como Executar

1. Clone o repositório para sua máquina local.
   ```bash
   git clone https://github.com/seu-usuario/plantio-certo.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd plantio-certo
   ```
3. Certifique-se de que você tem o Python instalado na sua máquina (versão 3.7+).
4. Execute o programa no terminal:
   ```bash
   python plantio_certo.py
   ```


## Estrutura do Código

- **home()**: Exibe o menu principal do sistema.
- **colheitas()**: Gerencia o histórico e detalhes das colheitas.
- **solos()**: Permite ao usuário escolher o tipo de solo para o plantio.
- **sementes()**: Fornece sugestões de sementes adequadas para o solo selecionado.
- **vendas()**: Gerencia a tabela de vendas de produtos agrícolas.
- **sugestao()**: Recebe e exibe feedbacks dos usuários.
- **main()**: Função principal que orquestra a navegação do sistema.


## Bibliotecas
*Listas das bibliotecas usadas:*

1. **sys**: 
   - Usada para controlar a saída do programa com a função `sys.exit()`. Isso permite encerrar o programa de forma controlada ao selecionar a opção de "Sair".

2. **io**: 
   - Usada para lidar com a leitura e escrita de arquivos. No código, ela é usada para abrir arquivos de texto, como `feijao.txt`, `milho.txt`, `batatadoce.txt`, e `macaxeira.txt`, que contêm informações sobre sementes e transcrevê-las no padrão latino de carcteres`(UTF - 8)`.

3. **datetime e timedelta**: 
   - Usada para manipular datas e horários. No código, essas bibliotecas são usadas para registrar a data de início das colheitas e calcular os dias restantes até a colheita, por meio de `datetime.now()` e `timedelta`.

4. **os.system**: 
   - Usada para executar comandos do sistema, como `cls`, que limpa o terminal. No código, isso é usado repetidamente para limpar a tela após cada operação, mantendo a interface limpa.

5. **time.sleep**: 
   - Usada para fazer o programa "pausar" por um tempo determinado em segundos. Isso é usado para dar um pequeno atraso em algumas operações, como limpar o terminal, permitindo ao usuário ver as informações antes que a tela seja atualizada.


## Pré-requisitos

- **Python 3.7+** instalado.
- Caso a Máquina seja **Mac/IOS** altera o código de limpesa de terminal *('cls') para ('clear')*

## Exemplo de Uso

Ao iniciar a aplicação, você será solicitado a fornecer seu nome, após o qual terá acesso ao menu principal, onde poderá navegar pelas opções de colheitas, tipos de solo, sugestões de sementes, vendas e feedback.

## Melhorias Futuras

- Integração com APIs meteorológicas para sugerir o melhor momento de plantio e colheita.
- Expansão da lista de sementes e solos disponíveis.
- Criação de um sistema de alerta para colheitas.


Esse READ ME fornece uma descrição clara do projeto, como ele funciona, e instruções de como utilizá-lo. Se você tiver alguma dúvida ou desejar incluir mais informações, entre em contato.

# Uso:

Após iniciar o aplicativo, você verá um menu principal com as seguintes opções:

- Colheitas: Gerencie as colheitas atuais e anteriores.
- Tipos de Solo: Visualize informações sobre diferentes tipos de solo.
- Sugestão de Sementes: Obtenha sugestões de sementes baseadas no tipo de solo.
- Vendas: Gerencie os produtos à venda e seus preços.
- Feedback: Registre e visualize feedbacks de clientes.
- Sair: Encerre o aplicativo.

Navegue pelo menu usando os números correspondentes às opções e siga as instruções na tela.


## Autor
Luiz Eduardo - Desenvolvedor Principal
Github (https://github.com/LuizDev-make)
  
