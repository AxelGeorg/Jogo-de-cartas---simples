

class ListaJogadores:

    def __init__(self):
        self._lista_jogadores = []
        self._index_JogadorAtual = 0

    @property
    def index_JogadorAtual(self):
        return self._index_JogadorAtual

    @index_JogadorAtual.getter
    def GetIndexJogadorAtual(self):
        return self._index_JogadorAtual

    @property
    def lista_jogadores(self):
        return self._lista_jogadores

    @lista_jogadores.getter
    def GetListaJogadores(self):
        return self._lista_jogadores

    @lista_jogadores.setter
    def SetListaJogadores(self, listaJogadores):
        self._lista_jogadores = listaJogadores

    def GetItemListaJogadores(self, index):
        return self._lista_jogadores[index]

    def adicionar_jogador(self, j):
        self._lista_jogadores.append(j)

    def obter_proximo_jogador(self):
        indexMax = len(self.lista_jogadores) - 1

        if (self._index_JogadorAtual == indexMax):
            self._index_JogadorAtual = 0
        else:
            self._index_JogadorAtual += 1

        return self.GetItemListaJogadores(self._index_JogadorAtual)

    def obter_lista_ordenada_pontos(self):
        self._lista_jogadores.sort(key=lambda x: x.pontos)
