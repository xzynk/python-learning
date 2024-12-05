# Herencia y Polimorfismo

#### 1 - Herencia
La herencia es un mecanismo que permite que una clase (clase hija o subclase) heredar atributos y metodos de otra clase (clase base o superclase). Esto promueve la reutilizacion de caodigo, ya que las subclases pueden reutilizar la logica de las superclases y, si es necesario, tambien puede sobrescribir o extender la funcionalidad.

#### ¿Que se debe saber sobre la herencia?
- **Superclase:** Es la clase de la que heredan otras clases. Tambien se le llama **clase padre** o **clase base**
- **Subclase:** Es la clase que hereda de la superclase. Tambien llamada **clase hija**
- **Metodo y atributos heredados:** Una subclase hereda todos los metodos y atributos de la superclase. Esto significa que puede utilizar esos metodos y atributos como si los hubiera definido ella misma.
- **Sobreescritura de metodos:** Una subclase puede sobreescribir los metodos de la superclase para modificar o extender su comportamiento.
- **Uso de super():** Con la funcion `super()`, una subclase puede llamar a un metodo o inicializar atributos de su superclase.

```python
class Animal:
	def __init__(self, name):
		self.name = name
	def speak(self):
		return f"{self.name} hace un sonido"

class Dog(Animal):
	def speak(self):
		return f"{self.name} ladra"

class Cat(Animal):
	def speak(self):
		return f"{self.name} maulla"

mi_perro = Dog("Rex")
print(mi_perro.speak()) #Rex ladra

mi_gato = Cat("Luna")
print(mi_gato.speak()) #Luna maulla

#Dog y Cat son subclases de Animal
#Ambas subclases sobrescriben el metodo speak de Animal
```

#### 2 - Polimorfismo
El **polimorfismo** es la capacidad de que diferentes clases pueden ser tratadas de la misma manera a traves de una interfaz comun. En otras palabras, objetos, diferentes clases puede ser accedidos mediante las mismos metodos, siempre y cuando comportan la misma firma (nombre y parametros del metodo).

#### ¿Que se debe saber sobre el Polimorfismo?
- **Polimorfismo en tiempo de ejecucion:** Diferentes objetos pueden tener diferentes implementaciones de un metodo, pero se pueden invocar de la misma manera. El metodo especifico.
- **Polimorfismo a traves de la herencia:** Las subclase pueden sobrescribir metodos de la superclase, lo que permite que el mismo metodo, se comporte demanera diferente segun el objeto que lo invoca.
- **Interface y polimorfismo:** Si varias clases implementan los mismos metodos (aunque no tengan una relacion de herencia directa) puedes tratarla de manera uniforme.

```python
animales = [Dog("Max") , Cat("Nina")]

for animal in animales:
	print(animal.speak())
```

#### 3 - Herencia Multiple:
**Python** soporta **herencia multiple**, lo que signfica que una clase puede heredar de mas de una superclase.

```python
class Flyer:
	def fly(self):
		return "Puede Volar"

class Swimmer:
	def swim(self):
		return "Puede nadar"

class Duck(Flyer, Swimmer):
	def quack(self):
		return "Hace cuak cuack"
```

Aqui, Duck hereda de ambas clases **Flyer** y **Swimmer**. Por lo tanto, puede usar metodos de ambas:

```python
pato = Duck()
print(pato.fly()) # Puede Volar
print(pato.swim()) # Puede nadar
print(pato.quack()) # Hace cuack cuack
```

Con la herencia multiple, Python resuelve los metodos que se deben invocar usando el **MRO (Method Resolution Order)** Esto determina el orden en el cual buscan los metodos cuando son llamados.

#### 4 - Super y el orden de la resolucion de metodos (MRO)
La funcion `super()` te permite acceder a metodos de la clase padre. Esto es particularmente util cuando trabajar con **herencia multiple**.

```python
class Animal:
	def speak(self):
		return "Animal emite un sonido"

class Dog(Animal):
	def speak(self):
		return super().speak() + "y ladra"

mi_perro = Dog()
print(mi_perro.speak()) #Animal emite un sonido y ladra
```

Aqui, `super().speak` llama al metodo speak de la clase Animal y luego el metodo en la subclase **Dog** agrega su propio comportamiento.
