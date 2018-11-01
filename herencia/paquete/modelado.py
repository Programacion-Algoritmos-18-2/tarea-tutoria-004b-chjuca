class Persona(object):							#Creamos la clase Persona 
  
	def __init__ (self): 						#Creamos el Metodo __init__
		self.nombres= " "						#Atributo nombres de la clase Persona 
		self.edad= 0							#Atributo edad de la clase Persona 
	
	def agregarNombres(self,n): 				#Funcion agregarNombres da valor a el atributo nombres 
		self.nombres= n
	
	def agregarEdad(self,n):					#Funcion agregarEdad da valor a el atributo edad
		self.edad= n
	
	def obtenerNombres(self):					#Esta funcion devuelve el atributo nombre
		return self.nombres
	
	def obtenerEdad(self):						#Esta funcion devuelve el atributo edad
		return self.edad
	
	def presentar_datos(self):					#Esta funcion devuelve una cadena con el valor devuelto por la funcion obtener edad y el atributo nombres
		c= "%s-%s "%(self.obtenerEdad(),self.nombres)
		return c



class Estudiante(Persona):							#Creamos la clase Estudiante que es una Persona 

	def __init__(self):								#Creamos el Metodo __init__
		super(Estudiante,self).__init__()			#Heredamos los atributos de la clase Persona 
		self.nota = 0								#Atributo nota de la clase Estudiante
	
	def agregarNota(self,n):						#Funcion agregarNota da valor a el atributo nota
		self.nota= n

	def presentar_datos(self):						#Esta funcion devuelve una cadena con el valor devuelto por presentar_datos y el atributo nota
		#c="%s-%s-%s"%(self.nombres,self.edad,self.nota
		c="%s-%s"%(super(Estudiante,self).presentar_datos(),self.nota)
		return c