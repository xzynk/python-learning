"""HERENCIA Y POLIMORFISMO"""

# LA HERENCIA ES UN MECANIMOS QUE PERMITE QUE UNA
# CLASE HERE LOS ATRIBUTOS Y métodoS DE OTRA CLASE


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        return f"{self.name} hace un sonido:"


class Dog(Animal):
    def speak(self):
        return f"{super().speak()} ladra"


class Cat(Animal):
    def speak(self):
        return f"{super().speak()} maulla"


un_perro = Dog("Yura")
un_gato = Cat("Ali")
print(un_perro.speak())
print(un_gato.speak())

# POLIMORFIRSMO ES LA CAPACIDAD DE QUE DIFERENTES
# CLASES PUEDEN SER TRATADAS DE LA MISMA MANERA A TRAVES DE UNA
# INTERFAZ EN COMUN

animales = [Dog("Max"), Cat("Alo")]
for animal in animales:
    print(animal.speak())

# PYTHON SOPORTA HERENCIA MULTIPLE, LO QUE SIGNFICA QUE UNA CLASE
# PUEDE HEREDERAR DE MAS UNA SUPERCLASE


class Flyer:
    def fly(self):
        return "Puede Volar"


class Swimmer:
    def swim(self):
        return "Puede nadar"


class Duck(Flyer, Swimmer):
    def quack(self):
        return "Hace cuack cuack"


pato = Duck()
print(pato.fly())
print(pato.swim())
print(pato.quack())


# EJERCICIO EXTRA


class Empleados:
    def __init__(self, nombre, apellido, codigo):
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.in_charge = []

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def fullname(self):
        return f"Mi nombre es: {self.nombre} {self.apellido}"

    def in_charge_of(self, employee):
        # Evitar que un empleado se gerencie a si mismo
        if employee == self:
            return f"{self.nombre} no puedes gerenciarte a ti mismo"

        self.in_charge.append(employee)
        return f"{self.nombre} {self.apellido} ahora gerencia a: {self.in_charge[-1]}"

    def show_all_in_charge(self):
        return [str(employee) for employee in self.in_charge]

    def get_job_title(self):
        return "Mi cargo es de:"

    def show_code(self):
        return f"Mi código es: {self.código}"


class Gerente(Empleados):
    def can_manage(self):
        return "Puedo gerenciar a Gerentes de proyectos y Programadores"

    def get_job_title(self):
        return f"{super().get_job_title()} Gerente"

    def change_name(self, new_name):
        self.nombre = new_name


class GerenteDeProyectos(Empleados):
    def can_manage(self):
        return "Puedo gerenciar a Programadores"

    def in_charge_of(self, employee):
        if isinstance(employee, Gerente):
            return "No puedes gerenciar a alguien de mayor cargo"

        return super().in_charge_of(employee)

    def get_job_title(self):
        return f"{super().get_job_title()} Gerente de Proyectos"


class Programador(Empleados):
    def get_job_title(self):
        return f"{super().get_job_title()} Programador"

    def in_charge_of(self, employee):
        return "NO TIENES PERMISOS"


print("GERENTE")
gerente = Gerente("Julio", "Verne", 858969)
print(gerente.fullname())
print(gerente.can_manage())
print(gerente.get_job_title())
print(gerente.show_code())
gerente.change_name("Raul")
print("GERENTE DE PROYECTOS")
gerente_de_proyectos = GerenteDeProyectos("Max", "Well", 233411)
print(gerente_de_proyectos.fullname())
print(gerente_de_proyectos.can_manage())
print(gerente_de_proyectos.get_job_title())
print(gerente_de_proyectos.show_code())
print("PROGRAMADOR")
programador = Programador("Graham", "Bell", 132)
print(programador.fullname())
print(programador.get_job_title())
print(programador.show_code())
print("GERENTE TIENE A CARGO A:")
print(gerente.in_charge_of(gerente_de_proyectos))
print(gerente.in_charge_of(gerente))
print(gerente.show_all_in_charge())
print("SUB GERENTE TIENE A CARGO A:")
print(gerente_de_proyectos.in_charge_of(programador))
print(gerente_de_proyectos.in_charge_of(gerente))
print("PROGRAMADOR TIENE A CARGO A:")
print(programador.in_charge_of(gerente_de_proyectos))
