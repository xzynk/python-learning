"""Ejercicio desarrollo sobre Fechas"""

from datetime import datetime

fecha_actual = datetime.now()
fecha_nacimiento = datetime(1989, 9, 4, 14, 15, 25)
tiempo_transcurrido = fecha_actual - fecha_nacimiento

print(f"Esta es la fecha actual: {fecha_actual}")
print(f"Mi fecha de nacimiento: {fecha_nacimiento}")
print(f"Y han pasado en total:{tiempo_transcurrido}")

# Dificultad extra
format_dia_mes_anio = fecha_nacimiento.strftime("%d-%m-%Y")
format_hora_minuto_segundo = fecha_nacimiento.strftime("%H:%M:%S")
format_dia_mes = fecha_nacimiento.strftime("%d")
format_dia_semana = fecha_nacimiento.strftime("%w")
format_nombre_del_dia = fecha_nacimiento.strftime("%A")
format_nombre_del_mes = fecha_nacimiento.strftime("%B")
format_anio_dos_digitos = fecha_nacimiento.strftime("%y")
format_dia_del_anio = fecha_nacimiento.strftime("%j")
format_am_pm = fecha_nacimiento.strftime("%p")
format_doce_horas = fecha_nacimiento.strftime("%I")


print("Ejercicio Extra:")
print("Mi fecha de nacimiento en diferentes formatos:")
print(f"Formateado a dia, mes, año: {format_dia_mes_anio}")
print(f"Formateado a hora, minuto, segundo: {format_hora_minuto_segundo}")
print(f"Formateado a dia del mes: {format_dia_mes}")
print(f"Formateado a dia de la semana: {format_dia_semana}")
print(f"Formateado nombre del dia: {format_nombre_del_dia}")
print(f"Formateado nombre del mes: {format_nombre_del_mes}")
print(f"Formateado año sin miles: {format_anio_dos_digitos}")
print(f"Formateado a numero del dia del año: {format_dia_del_anio}")
print(f"Formateado a AM o PM: {format_am_pm}")
print(f"Formateado hora en formato de 12 horas: {format_doce_horas}")
