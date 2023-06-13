"""
Módulo que contiene funciones útiles para el proyecto.
"""
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

	def crc(self,message, key):
		pick = len(key)

		tmp = message[:pick]

		while pick < len(message):
			if tmp[0] == '1':
				tmp = self.xor(key,tmp)+message[pick]
			else:
				tmp = self.xor('0'*pick,tmp) + message[pick]

			pick+=1

		if tmp[0] == "1":
			tmp = self.xor(key,tmp)
		else:
			tmp = self.xor('0'*pick,tmp)

		checkword = tmp
		return checkword
	def encodedData(self,data,key, init):
		# l_key = len(key)
		# append_data = data + '0'*(l_key-1)
		remanente = self.crc(data,key)
		codeword = data+remanente
		self.cdw += codeword
		print("Data Remainder is : " ,remanente)
		print("Transmitted Value is : " ,codeword)
		if init == remanente:
			return True, remanente
		else:
			return False, remanente

# def detect_errors(Cadena, polinomio, vector):
#     """
#     Calcula el CRC decuardo a los parametros enviados.
#     """
#     # Código para calcular CRC
#     # ...
#     Abin= bin((int(Cadena, 16)))
#     print(type(Abin))
#     print(Abin)
#     CRC = [int(x, 2) for x in polinomio]
#     Vec_init = [int(x, 2) for x in vector]
#     txt = [int(x) for x in Abin[2:]]
#     remanente = division(txt, CRC,Vec_init)
#     resultado =""
#     #for bit in remanente:
#      #   Abin+= str(bit)
#       #  resultado+= str(bit)
#     #codificado= Abin+"".join(str(remanente))
#     for bit in remanente:
#         resultado+=str(bit)
#     return resultado
# def division(text, crc, vector):
#     for bit in text:
#         propagacion = vector[0] ^ bit
#         for i in range(0, len(vector) - 1):
#             # print(i, " | ", c[i+1], " ^ (" , p, " & ", CRC[i+1], " ) = ", end=" ")
#             vector[i] = vector[i + 1] ^ (propagacion & crc[i + 1])
#             # print(c[i])
#         # print("z"," | ", c[-1], " <== " , p, " = ", end=" ")
#         vector[-1] = propagacion
#         # print(c[-1])
#         # print(b, p, c)
#     print(vector)
#     return vector

