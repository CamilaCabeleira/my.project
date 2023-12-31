"""
El ejercicio para mañana miércoles sería el siguiente:

Dada esta url = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

pasar los parámetros "a=1" y "b=2" como parámetros de una petición GET e imprimir el resultado
pasar un diccionario {'a':1,'b'=2} como payload de una petición POST e imprimir el resultado
si el resustado en ambos casos no es 3 elevar una excepción: AssertionError()

"""
import requests
import unittest

URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

A = 3
B = 2

parametros = {
    "a": A,
    "b": B
}

response = requests.get(URL, params=parametros)

print(response.text)

if float(response.text) != 5:
    raise AssertionError()

data = {
    "a": A,
    "b": B
}

response = requests.post(URL, json=data)

print(response.json()["result"])

if float(response.json()["result"]) != 5:
    raise AssertionError()

class TestSuma(unittest.TestCase):


    def test_sum_all_(self):
    resultado = data(A, B)
    self.assertEqual(resultado, 3)
