import tkinter
from tkinter import *
from tkinter import ttk

# cores ----------------------------------------------------------------
co0 = "#FFFFFF"     # branca / white
co1 = "#333333"     # preta pesado / dark black
co2 = "#fcc058"     # laranja / orange
co3 = "#38576b"     # valor / value
co4 = "#3297a8"     # azul / blue
co5 = "#fff873"     # amarela / yellow
co6 = "#fcc058"     # laranja / orange
co7 = "#e85151"     # vermelha / red
co8 = co4     # + verde
co10 = "#fcfbf7"
fundo = "#3b3b3b" # preta / black

# criando janela principal
janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.config(bg=fundo)

#D Dividindo a janela em dois------------------------------------------
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# Cnfigurando o frame de cima------------------------------------------
# app_x -> Label do jogador "X"
app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
# app_x -> Label "joagador 1"
app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
# app_xp pontucao na tela
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)

# Separador :
# app_separador -> Label ":"
app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separador.place(x=110, y=20)

# app_0 -> Label "O" (jogador 0)
app_0 = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_0.place(x=175, y=10)

# app_0 -> Label "joagador 2"
app_0 = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_0.place(x=165, y=70)

# app_xp pontucao na tela
app_0_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_0_pontos.place(x=130, y=20)


# Criando logica do app------------------------------------------

jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1','2','3'], ['4','5','6'], ['7','8',9]]

jogando = 'X'
jogar = ''
contador = 0
contador_de_rodada = 0

def iniciar_jogo():
    b_jogar.place(x=800, y=350)
    # pra controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar
    
        
        # comparando o valor recebido
        if i==str(1):
            
            # verificando se a posicao esta vazia ou nao
            if b_0['text']=='':                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
                
                # apos o contador ser maior ou igual a 5,
                # verifica se ouve algum vencedor de acordo
                # com os padroes sequintes dentro da tabela                
                if contador>=5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!="":
                        vencedor(jogando)
                        
                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!="":
                        vencedor(jogando)
                        
                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!="":
                        vencedor(jogando)
                    
                    #empate
                    if contador>9:
                        vencedor("foi empate")
        
        if i==str(2):
            
            # verificando se a posicao esta vazia ou nao
            if b_1['text']=='':
                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
        
        if i==str(3):
            
            # verificando se a posicao esta vazia ou nao
            if b_2['text']=='':
                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1

        if i==str(4):
            
            # verificando se a posicao esta vazia ou nao
            if b_3['text']=='':
                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1

        if i==str(5):
            
            # verificando se a posicao esta vazia ou nao
            if b_4['text']=='':
                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
        
        if i==str(6):
            
            # verificando se a posicao esta vazia ou nao
            if b_5['text']=='':
                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
        
        if i==str(7):
            
            # verificando se a posicao esta vazia ou nao
            if b_6['text']=='':
                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
        
        if i==str(8):
            
            # verificando se a posicao esta vazia ou nao
            if b_7['text']=='':
                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
        
        if i==str(9):
            
            # verificando se a posicao esta vazia ou nao
            if b_8['text']=='':
                
                # verificando quem esta a jogar e assim definir a cor do simbolo
                if jogando == 'X':
                    cor=co7
                if jogando == 'O':
                    cor=co8
                    
                # definindo a cor do texto do botao
                # e marcar aquela posicao da tabela
                # com o valor do jogador actual
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando
                
                # verificando quem esta a jogar, para poder de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
                
        # apos o contador ser maior ou igual a 5,
        # verifica se ouve algum vencedor de acordo
        # com os padroes sequintes dentro da tabela                
        if contador>=5:
            # linhas
            if tabela[0][0] == tabela[0][1] == tabela[0][2]!="":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2]!="":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2]!="":
                vencedor(jogando)
                        
            #colunas
            if tabela[0][0] == tabela[1][0] == tabela[2][0]!="":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2]!="":
                vencedor(jogando)
                        
            #diagonais
            if tabela[0][0] == tabela[1][1] == tabela[2][2]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0]!="":
                vencedor(jogando)
                    
            #empate
            if contador>=9:
                vencedor("Foi empate")
        
        # print(i)
    
    # para decidir o vencedor
    def vencedor(i):
        global tabela
        global score_1
        global score_2
        global contador_de_rodada
        global contador
        
        # desabilitando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        app_vencedor = Label(frame_baixo, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor.place(x=40, y=220)
        
        if i == 'X':
            score_2+=1
            app_vencedor['text'] = 'Jogador 2 venceu'
            app_0_pontos['text'] = score_2
        
        if i == 'O':
            score_1+=1
            app_vencedor['text'] = 'Jogador 1 venceu'
            app_x_pontos['text'] = score_1
        
        if i == 'Foi empate':
            app_vencedor['text'] = 'Foi um empate'
        
        def start():
            # limpando os botoes
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''
            
            # limpando os botoes
            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'
            
            app_vencedor.destroy()
            b_jogar.destroy()
            
        # Botao jogar -> button 0
        b_jogar = Button(frame_baixo, command=start, text='Proxima rodada', height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        b_jogar.place(x=70, y=195)
        
        def jogo_acabou():
            b_jogar.destroy()
            app_vencedor.destroy()
            
            terminar()
        if contador_de_rodada>=5:
            jogo_acabou()
        else:
            contador_de_rodada+=1
            # reinicilizando a tabela
            tabela = [['1','2','3'], ['4','5','6'], ['7','8',9]]
            contador = 0
            
    
    # para terminar o jogo
    def terminar():
        global tabela
        global contador_de_rodada
        global score_1
        global score_2
        global contador
        
        tabela = [['1','2','3'], ['4','5','6'], ['7','8',9]]
        contador_de_rodada = 0
        score_1 = 0
        score_2 = 0
        contador = 0
        
        # desabilitando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        app_fim = Label(frame_baixo, text='Jogo Acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_fim.place(x=35, y=90)
        
        # Jogar de novo
        def jogar_de_novo():
            app_0_pontos['text'] = '0'
            app_x_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()
            # chamando a funcao iniciar o jogo
            iniciar_jogo()
            
        # Botao jogar de novo
        b_jogar = Button(frame_baixo, command=jogar_de_novo, text='Jogar de novo', height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        b_jogar.place(x=80, y=195)

    # Cnfigurando o frame de baixo------------------------------------------

    # linhas verticais
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5 , anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co0)
    app_.place(x=90, y=15)
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5 , anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co0)
    app_.place(x=157, y=15)

    # linhas horizontais
    app_ = Label(frame_baixo, text='', width=46, padx=2, pady=1, relief='flat', anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co0)
    app_.place(x=30, y=63)
    app_ = Label(frame_baixo, text='', width=46, padx=2, pady=1, relief='flat', anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co0)
    app_.place(x=30, y=127)

    # linha 0 "b_0" -> button 0
    b_0 = Button(frame_baixo, command=lambda:controlar('1'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_0.place(x=30, y=15)
    # linha 0 "b_1" -> button 1
    b_1 = Button(frame_baixo, command=lambda:controlar('2'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_1.place(x=96, y=15)
    # linha 0 "b_2" -> button 2
    b_2 = Button(frame_baixo, command=lambda:controlar('3'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_2.place(x=163, y=15)

    # linha 1 "b_0" -> button 0
    b_3 = Button(frame_baixo, command=lambda:controlar('4'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_3.place(x=30, y=75)
    # linha 1 "b_0" -> button 1
    b_4 = Button(frame_baixo, command=lambda:controlar('5'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_4.place(x=96, y=75)
    # linha 1 "b_0" -> button 2
    b_5 = Button(frame_baixo, command=lambda:controlar('6'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_5.place(x=163, y=75)

    # linha 2 "b_0" -> button 0
    b_6 = Button(frame_baixo, command=lambda:controlar('7'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_6.place(x=30, y=135)
    # linha 1 "b_0" -> button 1
    b_7 = Button(frame_baixo, command=lambda:controlar('8'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_7.place(x=96, y=135)
    # linha 1 "b_0" -> button 2
    b_8 = Button(frame_baixo, command=lambda:controlar('9'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    b_8.place(x=163, y=135)

# Botao jogar -> button 0
b_jogar = Button(frame_baixo, command=iniciar_jogo,text='Jogar', width=10, height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
b_jogar.place(x=85, y=195)



janela.mainloop()
