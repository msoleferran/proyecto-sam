#!/usr/bin/env nextflow

// ---PARAMETROS DEL WORKFLOW---
// Definimos la ruta, hay que cambiarla utilizando --sam

params.sam = "${projectDir}/*.sam"

// --- PROCESO DE ANALISIS ---

process ANALIZAR_SAM {
    input: 
    path sam

    output: 
    stdout

// corremos el script con uv 
    script:
    """
    uv run python3 ${projectDir}/main.py ${sam}
    """
}

// --- WORKFLOW ---
// Corremos el analisis y forzamos que se muestre en pantalla

workflow {
    ANALIZAR_SAM(params.sam).view()
}
