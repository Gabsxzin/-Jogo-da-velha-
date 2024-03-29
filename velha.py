import tkinter as tk
import random


def verifica_vitoria(tabuleiro, jogador):

    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False
 

def tabuleiro_cheio(tabuleiro):
    return all(tabuleiro[i][j] != " " for i in range(3) for j in range(3))


def fazer_jogada(i, j):
    global tabuleiro, jogador_atual, vitoria

    if tabuleiro[i][j] == " " and not vitoria:
        tabuleiro[i][j] = jogador_atual
        botoes[i][j].config(text=jogador_atual)

        if verifica_vitoria(tabuleiro, jogador_atual):
            vitoria_label.config(text=f"Jogador {jogador_atual} venceu!")
            vitoria = True
        elif tabuleiro_cheio(tabuleiro):
            vitoria_label.config(text="Empate!")
            vitoria = True
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"
            status_label.config(text=f"Jogador {jogador_atual} é sua vez")


def reiniciar_jogo():
    global tabuleiro, jogador_atual, vitoria
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    vitoria = False
    vitoria_label.config(text="")
    status_label.config(text="Jogador X é sua vez")
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text=" ", state=tk.NORMAL)


tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "X"
vitoria = False


janela = tk.Tk()
janela.title("Jogo da Velha")


status_label = tk.Label(
    janela, text="Jogador X é sua vez", font=("Helvetica", 12))
status_label.pack()

vitoria_label = tk.Label(janela, text="", font=("Helvetica", 12, "bold"))
vitoria_label.pack()


tabuleiro_frame = tk.Frame(janela)
tabuleiro_frame.pack()

botoes = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        botoes[i][j] = tk.Button(tabuleiro_frame, text=" ", font=("Helvetica", 24), width=5, height=2,
                                 command=lambda i=i, j=j: fazer_jogada(i, j))
        botoes[i][j].grid(row=i, column=j)


reiniciar_button = tk.Button(janela, text="Reiniciar", font=(
    "Helvetica", 12), command=reiniciar_jogo)
reiniciar_button.pack()


janela.mainloop()