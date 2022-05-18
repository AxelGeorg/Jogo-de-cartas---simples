

from Model.Jogador import Jogador
from Model.Lista_Jogadores import ListaJogadores


class Tela:

    def __init__(self):
        self._jogadoresTela = ListaJogadores()

    @property
    def jogadoresTela(self):
        return self._jogadoresTela

    @jogadoresTela.getter
    def GetJogadoresTela(self):
        return self._jogadoresTela.GetListaJogadores

    def DefineJogadoresTela(self):
        jogadorUm = Jogador()
        jogadorUm.nome = input('Digite seu nome: ')
        jogadorUm.pontos = 0

        self._jogadoresTela.adicionar_jogador(jogadorUm)

        qtdOutrosJogadores = 0
        while qtdOutrosJogadores == 0:
            qtdOutrosJogadores = int(
                input('Digite quantidade de jogadores Robô (min. 1): '))

        for idxRobo in range(qtdOutrosJogadores):
            jogadorRobo = Jogador()
            jogadorRobo.nome = 'Robô ' + str(idxRobo)
            jogadorRobo.pontos = 0
            self._jogadoresTela.adicionar_jogador(jogadorRobo)

    def IniciaJogo(self, baralho, listaJogadores):

        jogadores = ListaJogadores()
        jogadores.SetListaJogadores = listaJogadores

        idxRodada = 0
        while baralho.quantidade() != 0:

            if jogadores.GetIndexJogadorAtual == 0:
                idxRodada += 1
                print(F"Rodade {str(idxRodada)}")

            jogador = jogadores.obter_proximo_jogador()

            carta = baralho.GetItemListaCartas(0)
            jogador.pontos += carta.simboloCarta

            print(
                f"Jogador {jogador.nome} retirou a carta {carta.simboloCarta}. Pontuacao Total {jogador.pontos}")
            baralho.retirar_carta()

            if baralho.quantidade() == 0:
                break

        print('\nFim do Jogo!')

    def MostraResultado(self, listaJogadores):
        listaResultado = ListaJogadores()
        listaResultado.SetListaJogadores = listaJogadores
        listaResultado.obter_lista_ordenada_pontos()

        """ for jogadorRanking in listaResultado._lista_jogadores:
            print(f"Jogador {jogadorRanking.nome} - Pontos {jogadorRanking.pontos}") """

        ganhador = listaResultado.GetItemListaJogadores(-1)
        print(f"Jogador {ganhador.nome} Venceu com {ganhador.pontos} pontos")
