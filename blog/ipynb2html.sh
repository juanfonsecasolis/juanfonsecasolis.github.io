#!/bin/bash

NB_CONVERT="python3 -m nbconvert"
FLAGS="--output-dir='./html' --to html --template=./template.tpl"

$NB_CONVERT JFonseca.suavizadoTraficoServidorWeb.ipynb $FLAGS
$NB_CONVERT JFonseca.interpolacion.ipynb $FLAGS
$NB_CONVERT JFonseca.pruebasRendimiento.ipynb $FLAGS
$NB_CONVERT JFonseca.pairwisetesting.ipynb $FLAGS
$NB_CONVERT JFonseca.evaluacionPerdidaCalidadAudioOpus.ipynb $FLAGS
$NB_CONVERT JFonseca.pruebasFormalesSoftware.ipynb $FLAGS
$NB_CONVERT JFonseca.audioVideoQualityStreaming.ipynb $FLAGS
$NB_CONVERT JFonseca.wavelets.ipynb $FLAGS
$NB_CONVERT JFonseca.solid.ipynb $FLAGS
$NB_CONVERT JFonseca.consejosIniciarRolAutomatizadorPruebas.ipynb $FLAGS
$NB_CONVERT JFonseca.solid.ipynb $FLAGS