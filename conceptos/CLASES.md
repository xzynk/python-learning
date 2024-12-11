# Clases

Las **Clases** en Python son una forma de definir estructuras que permiten organizar datos y funciones de manera eficiente, utilizando el paradigma de programacion orienteda a objetos (OOP). Las clases son plantillas para crear objetos, y los objetos son instancias de clases.

#### Elementos clave de las clases

1. **Clase:** Es una plantilla para crear objetos Define un conjunto de atributos y metodos que el objeto tendria.

```python
class MiClase
	pass # Clase Vacia
```

 2. **Objeto :** Es una instancia de una clase. Un objeto es una entidad que contiene datos y comportamientos definidos en la clase.

	 ```python
	 obj = MiClase() #Creacion de un objeto de MiClase
	 ```

3. **Atributos:**
	- **Atributos de Instancia:** Son variables que pertenecen a cada objeto y se definen dentro de los metodos de la clase, normalmente con el constructor `__init__()`
	- **Atributos de Clase:** Son variable que pertenecen a la clase en si y se comparten en todas las instancias de la clase.

```python
class MiClase:
	atributo_clase = 'Valor de Clase' # Atributo de clase
	
	def __init__(self,valor):
		self.atributo_instancia = valor # Atributo de Instancia

obj = MiClase("Valor de instancia")
print (obj.atributo_instancia) # Valor de instancia
print (MiClase.atributo_clase) # Valor de Clase
```

4. **Metodos:**
	- Son funciones definidas dentro de la clase que operan sobre los atributos del objeto
	- Los metodos tienen como primer argumento **self** que es una referencia al objeto actual **(la instancia de la clase)**

```python
class MiClase:
	def __init__(self, nombre):
		self.nombre = nombre

	def saludar(self):
		print (f"Hola, {self.nombre}")

obj = MiClase("Ana")
obj.saludar() #Hola, Ana
```

**Constructor __init__()**  
El constructor es el metodo especial que se ejecuta automaticamente cuando se crea un objeto de la clase. Es donde se inicializan los atributos del objeto.

**Metodos especiales (dunder methods o metodos magicos)**  
Python tiene varios metodos especiales que permiten definir comportamientos personalizados en los objetos. Estos metodos tienen nombres que comienzan y terminan con __ (doble guion bajo)

- `__str__(self)`: Define como representar el objeto cuando se convierte en cadena de texto usando `str() o print() )`
- `__repr__(self)`: Defne una representacion mas detalladas usado por `repr()` o en la consola iteractiva
- `__len__(self)`: Defineque devolver cuando se usa `len()`
- `__getitem__(self, key)`: Define como acceder a los elementos del objeto usando corchetes

**Encapsulamiento**  
El encapsulamiento es una forma de proteger los datos de acceso externo
- `_atributo`  : Indiica que el atributo es **"protegido"**
- `__atributo` : Implementa el **name mangling** que cambia el nombre a uno unico