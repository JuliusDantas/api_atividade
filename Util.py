from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Archanjo', idade=50)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome="Archanjo").first()
    #print(pessoa.nome)
    #print(pessoa.idade)
    print(pessoa)


def consulta_pessoas_Filtro():
    pessoaFiltro = Pessoas.query.filter_by(nome="Archanjo").first()
    print(pessoaFiltro)

def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Archanjo").first()
    pessoa.idade = 48
    pessoa.save()
    print(pessoa.nome)
    print(pessoa.idade)

def deleta_pessoas():
    pessoa = Pessoas.query.filter_by(nome="Archanjo").first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()
    altera_pessoas()
    consulta_pessoas_Filtro()
    deleta_pessoas()