# Fechas

Python ofrece varias maneras de trabajar con fechas y horas, proporcionando gran flexibilidad para hacer cálculos, formatear, comparar y manipular datos temporales. Aquí están los aspectos claves sobre fechas en Python:

# 1- Módulos principales para fechas y tiempos

- **datetime**: la librería principal para trabajar con fechas y horas. Ofrece tipos como date,time, datetime, timedelta.
- **time**: orientada al manejo de tiempos en formato de época (epoch) y funciones de reloj.
- **calendar:** ofrece funciones para manejar calendarios.
- **dateutil** (externo): extensión que facilita la manipulación de fechas y tiempos, permite manejo avanzado de zonas horarias.

# 2- Usando datetime

El módulo datetime es el más completo para trabajar con fechas y horas en Python.

```python
from datetime import datetime, date, time, timedelta
```

##### Crear fechas y tiempos

- **Fecha Actual :** datetime.now()
- **Fecha/Hora Especifica:** datetime(2024,10,16,15,30)
- **Solo Fecha: ** date(2024,10,16)
- **Solo Hora:** time(15)

##### Componentes

Puedes extraer partes de una fecha usando atributos:

```Python
now = datetime.now()
year = now.year #Año actual
month = now.month #Mes actual
dar = now.day #Dia actual
hour = now.hour #Hora actual
minute = now.minute #Minuto actual
second = now.second #Segundo actual
```

##### Comparación de fechas
Las fechas se puede comparar usando operadores como < , > , == , etc.

```python
date1 = datetime(2024, 1, 1)
date2 = datetime(2023, 1, 1)
print(date1 > date2)  # True, ya que date1 es después de date2
```

# 3- Formatos de fechas

Para convertir fechas y horas a *strings* y viceversa, *strftime* y *strptime* son útiles:

- ##### Formato a strings(strftime)
```Python
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")  # "2024-10-16 15:30:00"
```

***Principales códigos de formato:***
- %Y: Año Completo(2024)
- %m: Mes(01-12)
- %d: Día (01-31)
- %H: Hora(00 a 23)
- %M: Minuto (00 a 59)
- %S: Segundo (00 a 59)

Extendemos mas estos codigos [aqui](FORMATOS_DE_FECHA.md)

- ##### Conversión de string a fecha (strptime)
```python
date_string = "2024-10-16 15:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
```

# 4- Operaciones con timedata

Para hacer cálculos de tiempo (sumar/restar días,horas,etc.) *timedelta* es el tipo ideal.

```Python
now = datetime.now()
one_week_later = now + timedelta(weeks=1)  # Agrega 7 días
two_days_before = now - timedelta(days=2)  # Resta 2 días
```

**Diferencia entre fechas**
La resta de dos fechas da un *timedelta:*

```Python
date1 = datetime(2024, 1, 10)
date2 = datetime(2024, 1, 1)
diff = date1 - date2
print(diff.days)  # 9 días de diferencia
```

# 5- Zonas Horarias con pytz

Python no incluye zonas horarias por defecto, pero puedes agregar soporte mediante pytz (requiere instalación).

```python
from datetime import datetime
import pytz

# Fecha con zona horaria UTC
utc = pytz.UTC
now_utc = datetime.now(utc)

# Convertir a otra zona horaria
est = pytz.timezone('America/New_York')
now_est = now_utc.astimezone(est)
print(now_est)
```

# 6- Manejo de Fechas en formato de época (Unix timestamp)

La *epoch* es la cantidad de segundos desde el 1 de enero de 1970.

**Obtener época actual**
```python
epoch_time = datetime.now().timestamp()
```

**Convertir desde época a fecha**
```python
date_from_epoch = datetime.fromtimestamp(epoch_time)
```

# 7- Manejo de Fechas Relativas con dateutil

La librería *dateutil* permite trabajar con fechas relativas (como “el próximo martes”).

```Python
from dateutil.relativedelta import relativedelta
# Fecha un año adelante
next_year = datetime.now() + relativedelta(years=1)
# Fecha el próximo mes
next_month = datetime.now() + relativedelta(months=1)
```