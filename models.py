from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base=declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoas {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class PessoasDocumento(Base):
    __tablename__ = 'PessoaDocumento'
    id = Column(Integer, primary_key=True)
    Pessoas_id = Column(Integer, ForeignKey('pessoas.id'))
    CPF = Column(String(14))
    pessoas = relationship("Pessoas")

class Atividades(Base):
    __tablename__ = 'Atividade'
    id = Column(Integer, primary_key=True)
    Pessoas_id = Column(Integer, ForeignKey('pessoas.id'))
    nome = Column(String(80))
    pessoas = relationship("Pessoas")

    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()