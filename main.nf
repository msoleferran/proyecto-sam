#!/usr/bin/env nextflow

// ---PARAMETROS DEL WORKFLOW---
// Definimos la ruta, se puede cambiar siempre utilizando --sam

params.sam = "${launchDir}/*.sam"

// --- PROCESO DE ANALISIS ---

process ANALIZAR_SAM {
    input: 
    path sam

    output: 
    stdout

    script:
    """
    uv run python3 ${projectDir}/main.py ${sam} // Corremos el script con uv
    """
}

// --- WORKFLOW ---
// Corremos el analisis y forzamos que se muestre en pantalla

workflow {
    ANALIZAR_SAM(params.sam).view()
}
