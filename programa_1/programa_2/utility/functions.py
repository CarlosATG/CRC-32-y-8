"""
Módulo que contiene funciones útiles para el proyecto.
"""
from bitarray import bitarray
from bitarray.util import hex2ba, ba2int
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
		posicion = len(key)

		remanente = mensaje[:posicion]

		while posicion < len(mensaje):
			if remanente[0] == '1':
				remanente = self.xor(key,remanente)+mensaje[posicion]
			else:
				remanente = self.xor('0'*posicion,remanente) + mensaje[posicion]

			posicion+=1

		if remanente[0] == "1":
			remanente = self.xor(key,remanente)
		else:
			remanente = self.xor('0'*posicion,remanente)

		return remanente
	def encodedData(self,data,key, init):
		mensaje= hex2ba(data)
		binario= ba2int(mensaje)
		print(binario, type(binario))
		bina= bin(binario)
		bini= bina[2:]
		print(bina)
		remanente = self.crc(bini,key)
		Mensaje_codi = str(bini)+remanente
		self.cdw += Mensaje_codi
		print("Data Remainder is : " ,remanente)
		print("Transmitted Value is : " ,Mensaje_codi)
		if init == remanente:
			return True, remanente
		else:
			return False, remanente

