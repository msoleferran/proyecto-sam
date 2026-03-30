#!/usr/bin/env python3

import sys
import re
from rich.console import Console

# Capturamos como ruta el primer argumento de la linea de comandos
sam_path = sys.argv[1]

# Generamos las variables para calcular los parámetros
total_aligned = 0
total_mapq_60 = 0

# Abrimos el archivo y lo leemos linea a linea
with open(sam_path, mode="r") as file:
    for line in file:
# Nos saltamos las lineas que empiezan con @, es decir, las cabeceras
        if re.match("^@", line):
            continue 

# Contamos cada alineamiento
# Separamos las columnas y nos quedamos  con la quinta que son los valores MAPQ 
# Contamos los MAPQ que son 60

        total_aligned += 1
        columns = line.split("\t")
        mapq_count = int(columns[4])
        if mapq_count == 60:
            total_mapq_60 += 1

percent_60_counts = (total_mapq_60 / total_aligned) * 100

# Forzamos que nextflow muestre a la terminal los resultados
console = Console(force_terminal=True)

# Hacemos print de los resultados con el modulo rich
console.print("\n[bold magenta]Resultados análisis:[/bold magenta]",
	     "\n\n- [bold]Total de lecturas alineadas[/bold]:", total_aligned, 
	     "\n- [bold]Lecturas con MAPQ = 60[/bold]:", total_mapq_60, 
	     "\n- [bold]Porcentaje[/bold]:", str(round(percent_60_counts, 1)) + "%")
