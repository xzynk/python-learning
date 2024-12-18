# Formatos de Fecha en Python

Extendamos un poco cuales son los formatos de Fecha

#### Códigos relacionados con la fecha

| **Código** |                    **Significado**                    |                    **Ejemplo**                    |
|:-----------|:-----------------------------------------------------:|:-------------------------------------------------:|
| `%a`       |         Nombre abreviado del día de la semana         |                   `Sun`, `Mon`                    |
| `%A`       |         Nombre completo del día de la semana          |                `Sunday`, `Monday`                 |
| `%w`       |            Día de la semana (0 = Domingo)             |                `0`, `1`, ..., `6`                 |
| `%d`       |            Día del mes con ceros iniciales            |                    `01`, `02`                     |
| `%b`       |               Nombre abreviado del mes                |                   `Jan`, `Feb`                    |
| `%B`       |                Nombre completo del mes                |               `January`, `February`               |
| `%m`       |            Mes con ceros iniciales (01-12)            |                    `01`, `02`                     |
| `%y`       |              Año sin siglo (dos dígitos)              |                    `21`, `99`                     |
| `%Y`       |            Año con siglo (cuatro dígitos)             |                  `2021`, `1999`                   |
| `%j`       |                 Día del año (001-366)                 |                   `001`, `365`                    |
| `%U`       | Número de la semana del año (Domingo como primer día) |                    `00`, `52`                     |
| `%W`       |  Número de la semana del año (Lunes como primer día)  |                    `00`, `52`                     |
| `%c`       |                 Fecha y hora completa                 |             `Sun Dec 5 14:02:00 2021`             |
| `%C`       |                   Siglo como número                   |                    `20`, `21`                     |
| `%x`       |                 Fecha local (formato)                 | `12/05/21` (depende de la configuración regional) |
| `%X`       |                 Hora completa (local)                 |                    `14:02:00`                     |

#### Codigos relacionados con la hora

| **Código** |                **Significado**                |                    **Ejemplo**                    |
|:-----------|:---------------------------------------------:|:-------------------------------------------------:|
| `%H`       |      Hora (24 horas) con ceros iniciales      |                    `00`, `23`                     |
| `%I`       |      Hora (12 horas) con ceros iniciales      |                    `01`, `12`                     |
| `%p`       |                    AM o PM                    |                    `AM`, `PM`                     |
| `%M`       |          Minutos con ceros iniciales          |                    `00`, `59`                     |
| `%S`       |         Segundos con ceros iniciales          |                    `00`, `59`                     |
| `%f`       |       Microsegundos con ceros iniciales       |                `000000`, `999999`                 |
| `%z`       |              Desplazamiento UTC               |                 `+0000`, `-0400`                  |
| `%Z`       |           Nombre de la zona horaria           |                `UTC`, `EST`, `CST`                |
| `%X`       |             Hora local (formato)              | `14:02:00` (depende de la configuración regional) |
| `%s`       | Timestamp en segundos desde Epoch (Unix Time) |                   `1638727320`                    |
