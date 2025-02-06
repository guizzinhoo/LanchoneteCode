
import time
pedido = []
conta = 0

def menu():
    while True:
        time.sleep(0.35)
        print('\n')
        print('   BEM-VINDO AO DRIVE THRU!   ')
        time.sleep(0.35)
        time.sleep(0.35)
        print('         FAÇA SEU PEDIDO:           ')
        time.sleep(0.35)
        print('-' * 40)
        print('         0 - SAIR                    ')
        time.sleep(0.35)
        print('         1 - HAMBURGUER               ')
        time.sleep(0.35)
        print('         2 - REFRIGERANTE       ')
        time.sleep(0.35)
        print('         3 - BATATA FRITA      ')
        time.sleep(0.35)
        print('-' * 40)
        print('\n')
        time.sleep(0.35)

        try:
            resposta = int(input('DIGITE A OPÇÃO ESCOLHIDA: '))
            if resposta == 0:
                print('\n')
                print('SAINDO DO SISTEMA...')
                break
            elif resposta == 1:
                hamrburguer()
            elif resposta == 2:
                refrigerante()
            elif resposta == 3:
                fritas()
            else:
                print('\n')
                print('ATENÇÃO: A OPÇÃO DIGITADA É INVÁLIDA.')
                print('\n')

        except ValueError:
            print('\n')
            print('ATENÇÃO: ERRO DE FORMATAÇÃO. DIGITE UM NÚMERO VÁLIDO.')
            print('\n')

def hamrburguer():
    global conta
    try:
        burguer = int(input('\n OPÇÕES DE HAMBURGUERES: \n 1 - SMALLMAC R$11.50 \n 2 - QUARTEIRINHO R$09.30 \n 3 - MACSHARK R$12.00 \n DIGITE A OPÇÃO ESCOLHIDA: '))

        if burguer == 1:
            pedido.append('UM SMALLMAC')
            conta += 11.50
        elif burguer == 2:
            pedido.append('UM QUARTEIRINHO')
            conta += 9.30
        elif burguer == 3:
            pedido.append('UM MACSHARK')
            conta += 12.00
        else:
            print('\n')
            print('A OPÇÃO DIGITADA NÃO EXISTE NO CARDÁPIO')
            print('\n')

    except ValueError:
        print('Erro ao processar o pedido')
def refrigerante():
    global conta
    try:
        refri = int(input('\n OPÇÕES DE REFRIGERANTES: \n 1 - COCA-GRUDA R$08.50 \n 2 - GUANTARÁ R$06.25 \n 3 - BEBSI R$05.00 \n DIGITE A OPÇÃO ESCOLHIDA: '))

        if refri == 1:
            pedido.append('UMA COCA-GRUDA')
            conta += 8.50
        elif refri == 2:
            pedido.append('UM GUANTARÁ')
            conta += 6.25
        elif refri == 3:
            pedido.append('UMA BEBSI')
            conta += 5.00
        else:
            print('\n')
            print('A OPÇÃO DIGITADA NÃO EXISTE NO CARDÁPIO')
            print('\n')

    except ValueError:
        print('Erro ao processar o pedido')
def fritas():
    global conta
    try:
        batata = int(input('\n TAMANHOS: \n 1 - GRANDE R$10.00 \n 2 - MÉDIA R$07.50 \n 3 - PEQUENA R$05.00 \n DIGITE A OPÇÃO ESCOLHIDA: '))

        if batata == 1:
            pedido.append('BATATA GRANDE')
            conta += 10
        elif batata == 2:
            pedido.append('BATATA MÉDIA')
            conta += 7.50
        elif batata == 3:
            pedido.append('BATATA PEQUENA')
            conta += 5.00
        else:
            print('\n')
            print('A OPÇÃO DIGITADA NÃO EXISTE NO CARDÁPIO')
            print('\n')

    except ValueError:
        print('Erro ao processar o pedido')

def main():
    menu()
    if pedido:
        pedido_formatado = ', '.join(pedido)
        print(f'AGRADECEMOS A PREFERÊNCIA! \n SEU PEDIDO É DE {pedido_formatado}')
        print(f'SUA CONTA FICOU R${conta:.2f}')
    else:
        print("Nenhum pedido foi realizado.")

main()
