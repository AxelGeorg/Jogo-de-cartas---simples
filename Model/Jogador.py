
class Jogador:

    def __ini__(self):
        self._pontos
        self._nome

    @property
    def pontos(self):
        return self._pontos

    @pontos.setter
    def pontos(self, pontos):
        self._pontos = pontos

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
