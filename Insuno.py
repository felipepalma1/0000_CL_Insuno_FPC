# -*- coding: utf-8 -*-

from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator

from java.util import List, ArrayList

import random

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.registerIntruderPayloadGeneratorFactory(self)

        # Salida
        salida = (
            "Insuno.BurpExtender"
            ".registerExtenderCallbacks"
        )
        print(salida, self)

        return

    def getGeneratorName(self):

        # Salida
        salida = (
            "Insuno.BurpExtender"
            ".getGeneratorName"
        )
        print(salida, self)

        return "Insuno"
    
    def createNewInstance(self, attack):
        
        # Salida
        salida = (
            "Insuno.BurpExtender"
            ".createNewInstance"
        )
        print(salida, self, attack)

        return Insuno(self, attack)

class Insuno(IIntruderPayloadGenerator):

    def __init__(self, extender, attack):
        self._extender = extender
        self._helpers = extender._helpers
        self._attack = attack
        self.max_payloads = 10
        self.num_iterations = 0


        print("Inicializacion Insuno desde Insuno.Insuno instanciado en ", self)
        print("\n")

        return

    def hasMorePayloads(self):
        # Salida
        salida = (
            "Insuno.hasMorePayloads"
        )
        print(salida, self)
        print("\n")

        return True

    def getNextPayload(self,carga_cruda):

        # Salida
        salida = (
            "Insuno.getNextPayload"
        )

        print(salida, self, carga_cruda)
        print("\n")
        
        carga_formalizada = "".join(chr(x) for x in carga_cruda) 
        carga_envenenada = self.envenenar(carga_formalizada)

        # Segunda Salida
        salida = (
            "Insuno.getNextPayload.carga_formalizada"
        )

        print(salida, carga_formalizada)
        
        salida = (
            "Insuno.getNextPayload.carga_envenenada"
        )

        print(salida, carga_envenenada)
        
        print("\n")

        return carga_envenenada
    
    def reset(self):
        print("reset")
        return

    
    def envenenar(self,carga_formalizada):

        diccionario_objetivo = open('biblioteca/diccionario/diccionario-xss-poliglota.txt', 'r')
        contenido = diccionario_objetivo.readlines()
        diccionario_objetivo.close()

        carga_envenenada = contenido[0]
        
        return carga_envenenada


