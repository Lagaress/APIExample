from enum import Enum
from xmlrpc.client import Boolean
import database

from sqlalchemy import Column, Integer, String, Float, Boolean, Enum

# Nadadores Table
class Nadadores(database.Base): 
    __tablename__ = 'Nadadores'

    nadadorId = Column(Integer , primary_key = True)
    nombre = Column(String , nullable = False)
    sexo = Column(Enum('H' , 'M') , nullable = False)

    def __init__(self, nombre, sexo):
        self.nombre = nombre
        self.sexo = sexo

    def __repr__(self):
        return f'Nadadores({self.nombre}, {self.sexo})'

    def __str__(self):
        return self.nombre


# EstiloNatacion Table
class EstiloNatacion(database.Base): 
    __tablename__ = 'EstiloNatacion'

    estiloId = Column(Integer , primary_key = True)
    nombre = Column(String , nullable = False)
    puntos = Column(Integer , nullable = False)

    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos

    def __repr__(self):
        return f'EstiloNatacion({self.nombre}, {self.puntos})'

    def __str__(self):
        return self.nombre


# Competiciones Table
class Competiciones(database.Base): 
    __tablename__ = 'Competiciones'

    competicionId = Column(Integer , primary_key = True)
    nombre = Column(String , nullable = False)
    estiloId = Column(Integer , nullable = False)
    celebrada = Column(Boolean , nullable = False)

    def __init__(self, nombre, estiloId , celebrada):
        self.nombre = nombre
        self.estiloId = estiloId
        self.celebrada = celebrada

    def __repr__(self):
        return f'Competiciones({self.nombre}, {self.estiloId} , {self.celebrada})'

    def __str__(self):
        return self.nombre

# Inscripción Table 
class Inscripcion(database.Base): 
    __tablename__ = 'Inscripcion'

    nadadorId = Column(Integer , primary_key = True)
    competicionId = Column(Integer , nullable = False)
    posicion = Column(Integer , nullable = False)

    def __init__(self, competicionId, posicion):
        self.competicionId = competicionId
        self.posicion = posicion

    def __repr__(self):
        return f'Inscripcion({self.competicionId}, {self.posicion})'
