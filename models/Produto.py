
from enum import Enum

class Setor(Enum):
    ACOUGUE = 'A�ougue'
    FRIOS_LATICINIOS = 'Frios e latic�nios'
    ADEGA_BEBIDAS = 'Adega e bebidas'
    HIGIENE_LIMPEZA = 'Higiene e limpeza'
    HORTIFRUTI_MERCEARIA = 'Hortifruti e mercearia'
    PADARIA = 'Padaria'
    ENLATADOS = 'Enlatados'
    CEREAIS = 'Cereais'

class TipoProduto(Enum):
    ALIMENTICIO = 'Aliment�cio'
    PRODUTO_LIMPEZA = 'Produto de limpeza'
    OUTROS = 'Outros'
    
class Produto:
    def __init__(self, id, codigo, nome, preco, quantidade, setor, tipo):
        self.__id = id
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        self.__setor = setor  # Inst�ncia da enumera��o Setor
        self.__tipo = tipo  # Inst�ncia da enumera��o TipoProduto

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def get_setor(self):
        return self.__setor

    def set_setor(self, setor):
        if isinstance(setor, Setor):
            self.__setor = setor
        else:
            raise ValueError("Setor deve ser uma inst�ncia de Setor.")

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        if isinstance(tipo, TipoProduto):
            self.__tipo = tipo
        else:
            raise ValueError("Tipo deve ser uma inst�ncia de TipoProduto.")