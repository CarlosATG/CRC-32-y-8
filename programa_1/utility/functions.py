"""
Módulo que contiene funciones útiles para el proyecto.
"""
from bitarray import bitarray
from bitarray.util import ba2hex
class CRC:
	def __init__(self):
		self.cdw = ''

	def xor(self,a,b):
		result = []
		for i in range(1,len(b)):
			if a[i] == b[i]:
				result.append('0')
			else:
				result.append('1')
		return  ''.join(result)

	def crc(self,mensaje, key):
		posicion = len(key) #caso de Bluetooth seria 9 y de Wifi 33

		remanente = mensaje[:posicion]#Crea un vector con la misma cantidad de valores que la llave, usando el mensaje como base

		while posicion < len(mensaje):
			if remanente[0] == '1':#Si el bit del polinomio está prendido, su valor sera el del anterior más la propagación
				remanente = self.xor(key,remanente)+mensaje[posicion]
			else:
				remanente = self.xor('0'*posicion,remanente) + mensaje[posicion]##Si el bit del polinomio está apagado, su valor sera el del anterior

			posicion+=1

		if remanente[0] == "1":
			remanente = self.xor(key,remanente)
		else:
			remanente = self.xor('0'*posicion,remanente)

		return remanente

	def encodedData(self,text,llave, vector):
		data=text+vector
		remanente = self.crc(data,llave)
		Mensaje_codi = text+remanente
		self.cdw += Mensaje_codi
		final = bitarray(Mensaje_codi)
		Hexa= ba2hex(final)
		return remanente, Hexa
