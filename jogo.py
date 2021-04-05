import PySimpleGUI as sg
sg.theme('Material2')
def tela():
    estilo = [
        [sg.Text('__ PEDRA PAPEL TESOURA__')],
        [sg.Text(size=(55, 2))],
        [sg.Button('pedra')],
        [sg.Button('papel')],
        [sg.Button('tesoura')],
        [sg.Text(size=(55,22), key='resultado')],
        [sg.Button('mostrar dados')],
        [sg.Text(size=(55, 1), key='encerramento')],
        [sg.Text(size=(55, 1), key='vitorias')],
        [sg.Text(size=(55, 2))],
        [sg.Text('feito por bruno dos santos'), sg.Button('sair')]
    ]
    janela = sg.Window('P P T').layout(estilo)
    jogadas = 0
    vitoria = 0
    derrota = 0
    while True:
        e, v = janela.read()
        if e == sg.WINDOW_CLOSED or e == 'sair':
            break
        import jogo2
        computador2 = jogo2.comp()
        if e == 'pedra':
            jogadas += 1
            if computador2 == 'pedra':
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou pedra. empate')
            elif computador2 == 'papel':
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou pedra. você perdeu')
                derrota += 1
            else:
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou pedra. você ganhou')
                vitoria += 1
        if e == 'papel':
            jogadas += 1
            if computador2 == 'pedra':
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou papel. você ganhou')
                vitoria += 1
            elif computador2 == 'papel':
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou papel. empate')
            else:
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou papel. você perdeu')
                derrota += 1
        if e == 'tesoura':
            jogadas += 1
            if computador2 == 'pedra':
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou tesoura. você perdeu')
                derrota += 1
            elif computador2 == 'papel':
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou tesoura. você ganhou')
                vitoria += 1
            else:
                janela['resultado'].update(f'o computador jogou {computador2} e você jogou tesoura. empate')
        if e == 'mostrar dados':
            janela['encerramento'].update(f'até agora tivemos {jogadas} jogadas.')
            janela['vitorias'].update(f'o computador ganhou {derrota} é você ganhou {vitoria}.')




tela()
