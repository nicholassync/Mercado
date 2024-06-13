
from enum import Enum


    
class  Produto:
    def __init__(self):
        self.__id = None
        self.__codigo = None
        self.__nome = None
        self.__preco = None
        self.__quantidade = None
        self.__setor = None  
        self.__tipo = None
        
    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def get_setor(self):
        return self.__setor

    def set_setor(self, setor):
        self.__setor = setor
        
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

