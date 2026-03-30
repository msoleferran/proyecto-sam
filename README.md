# Herramienta para analizar archivos SAM
**Autor**: Maria Solé Ferran
## Descripción

Esta herramienta permite analizar archivos **SAM** (Sequence Alignment/Map) para obtener métricas básicas sobre la calidad del alineamiento. El programa nos imprime la siguiente información: 

- Número *total* de lecturas alineadas.
- Número de lecturas con MAPQ (MAPping Quality) de 60. 
- El porcentaje que representan estas lecturas sobre el total.

Esta herramienta está gestionada con **Nextflow** para ejecutar el script de forma reproducible. 

## Requisitos
- Python 3.10+
- uv
- Nextflow


## Estructura del proyecto
- `README.md`: documentación del programa
- `main.nf`: pipeline de Nextflow
- `main.py`: script de python
- `data`: carpeta con un archivo de prueba (`test.sam`)
- `pyproject.toml`: y `uv.lock`: dependecias del proyecto Python

## Instalación
### Clonar el repositorio
Clona el repositorio utilizando:
```bash
git clone https://github.com/msoleferran/proyecto-sam.git
```

Luego, muévete al directorio del proyecto:
```bash
cd proyecto-sam
```

### Instalar dependencias con uv
```bash
uv sync
```

### Uso
El archivo de entrada debe ser un `.sam`. 
Para usar el script utiliza el parámetro `--sam`, e indica la ruta del archivo a analizar:

```bash
nextflow run main.nf --sam ruta/al/archivo.sam
```

### Ejemplo
Podemos analizar un archivo ejemplo(`test.sam`), localizado en `data/`:

```bash
nextflow run main.nf --sam $PWD/data/test.sam
```

El programa debería imprimirnos: 

```bash
Resultados análisis: 

- Total de lecturas alineadas: 98128 
- Lecturas con MAPQ = 60: 50089 
- Porcentaje: 51.0%
```

Espero que os sea de utilidad! :)
