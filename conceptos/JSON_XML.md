# JSON y XML

JSON y XML son formatos muy utilizados para **almacenar y transmitir datos.** Cada uno tiene sus ventajas y particularidades, y es importante conocer, como manejarlos para trabajar con APIs, base de datos o archivos estructurales.

#### 1. JSON (JavaScript Object Notation)
JSON es un formato de datos ligero y facil de leer para humanos y maquinas. Se utiliza ampliamente en **APIs Web** y aplicaciones para transmitir datos.

##### Caracteristicas de JSON
- Estructuras basadas en pares **claves-valor**
- Facil de leer y escribir.
- Compatible con muchos lenguajes de programacion (Python, Javascript, etc)
- Soporta tipos simples: **string, numbers, arrays, objetos, booleanos y null**
- Menos verboso que XML

```Json
{
	"product": "LAPTOP",
	"price": 1200.99,
	"stock": 25,
	"features": ["SSD", "16GB RAM", "Intel I7"],
	"available": True,
}
```

##### Manejo de JSON en Python
Python ofrece el modulo **json** para manejar archivos y datos JSON.

**Leer JSON desde un string:**
```Python
import json

json_data = '{"name": "Juan", "age" : 30}'
data = json.loads(json_data) # Convierte el string en un diccionario
print(data["name"]) #Salida: Juan
```

**Escribir JSON en un archivo:**
```Python
data = {
		"name": "Laptop",
		"price": 1200.99,
		"stock": 25
}

with open("product.json", "w") as file:
	json.dump(data.file, indent =4)
	#Guarda el JSON en un archivo
```

**Leer JSON desde un archivo:**
```python
with open("product.json", "r") as file:
	data = json.load(file) #Carga el contenido en un diccionario
	print(data[name])  #Salida: Laptop
```

##### Ventajas de JSON
- Ligerio y rapido para transmitir datos
- Estructura clara y facil de entender
- Compatible con muchos lenguajes de programacion

#### 2. XML (eXtensible Markup Language)
XML es un formato mas antiguo que JSON y es ampliamente utilizado en **sistemas empresariales** y configuraciones. A diferencia de JSON, XML emplea **etiquetas** para definir los datos.

##### Caracteristicas de XML
- Basado en etiquetas anidadas (similar a HTML)
- Mas verboso que JSON
- Soporta **atributos** dentro de etiquetas
- Se usa en aplicaciones donde la validacion de datos es crucial (como SOAP , RSS)

```Xml
<product>
	<name> Laptop </name>
	<price currency = 'USD'> 1200.99 </price>
	<stock> 25 </stock>
	<features>
		<feature> SSD </feature>
		<feature> 16GB RAM </feature>
		<feature> Intel I7 </feature>
	</features>
</product>
```

##### Manejo de XML en Python
Python tiene varios modulos para trabajar en XML, como xml.etre.elementree y minidom.

**Leer XML**
```python
import xml.etree.ElementTree as ET

tree = ET.parse("product.xml") #Carga el archivo XML
root = tree.getroot()

#Obtener Valores
print(root.find("name").text) #Salida: Laptop
print(root.find("price").text) #Salida: 1200.99
```

**Escribir XML**
```python
import xml.etree.ElementTree as ET

root = ET.Element("product")
ET.subElement(root, "name").text = "Laptop"
ET.subElement(root, "price").text = "1200.99"
ET.subElement(root, "stock").text = "25"

tree = ET.ElementTree(root)
tree.write("product.xml", encoding="utf-8", xml-declaration=true)
```

##### Ventajas XML
- **Atributos** pueden almacenar metadatos (como la moneda en `<price currency="USD">`)
- Se usan donde se necesita mas control sobre la validacion de datos
- Ideal para **documentos, estructura de datos**

**Comparacion entre JSON y XML**

|   **ASPECTO**    |          **JSON**          |        **XML**         |
| :--------------: | :------------------------: | :--------------------: |
|     Sintaxis     |     Pares Clave-Valor      |   Etiquetas Anidadas   |
| Facilidad de Uso | Mas simple y facil de leer | Mas completo y verboso |
|      Tamaño      |     Menor (mas ligero)     |      Mayor Tamaño      |
| Soporte de datos | Arrays, objetos, booleanos | Solo Texto y atributos |
|  Compatibilidad  |  Popular entre Apis Rest   | Usado empresarialmente |
| Esquematizacion  |        No requiere         | Puede Validar DTD/XSI  |

##### Convertir XML a JSON
```python
import xmltodict
import json

with open("product.xml", "r") as file:
	xml_data = file.read()

json_data = json.dumps(xmltodict.parse(xml_data), indent=4)
print(json_data)
```

##### Convertir JSON a XML
```python
import xmltodict

json_data = {
			 "product":{
				 "name" : "Laptop"
				 "price" : "1200.99"
				 "stock" : "25"
			 }
}
xml_data = xmltodict.unparse(json_data, pretty=True)
print(xml_data)
```