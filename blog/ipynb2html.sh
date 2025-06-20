#!/bin/bash

python3 -m nbconvert JFonseca.suavizadoTraficoServidorWeb.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.interpolacion.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.pruebasRendimiento.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.pairwisetesting.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.evaluacionPerdidaCalidadAudioOpus.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.pruebasFormalesSoftware.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.audioVideoQualityStreaming.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.wavelets.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.solid.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.consejosIniciarRolAutomatizadorPruebas.ipynb --to html --template=./template.tpl
python3 -m nbconvert JFonseca.solid.ipynb --to html --template=./template.tpl
