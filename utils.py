from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Silva', idade=24)
    print(pessoa)
    db_session.add(pessoa)
    db_session.commit()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    #pessoa = Pessoas.query.filter_by(nome='Otavio').first()
    #print(pessoa.idade)

def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Bitencourt').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Silva').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    #exclui_pessoa()
    consulta_pessoas()