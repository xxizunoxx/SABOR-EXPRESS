# Classe criada e seus atributos
class musica:
    nome = ''
    artista = ''
    duracao = int

# Objetos que utilizam a classe
musica1 = musica()
musica1.nome = 'Numb'
musica1.artista = 'Linkin Park'
musica1.duracao = 190

musica2 = musica()
musica2.nome = 'Somewhere I Belong'
musica2.artista = 'Linkin Park'
musica2.duracao = 214

musica3 = musica()
musica3.nome = 'In The End'
musica3.artista = 'Linkin Park'
musica3.duracao = 217

# a função vars mostra os atributos da classe de cada objeto
print(vars(musica1))
print(vars(musica2))
print(vars(musica3))