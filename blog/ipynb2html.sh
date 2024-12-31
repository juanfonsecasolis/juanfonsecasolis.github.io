#!/bin/bash
#jupyter nbconvert JFonseca.suavizadoTraficoServidorWeb.ipynb --to html --template template.tpl
#jupyter nbconvert JFonseca.interpolacionBL.ipynb --to html --template template.tpl
#jupyter nbconvert JFonseca.pruebasRendimiento.ipynb --to html --template template.tpl
#jupyter nbconvert JFonseca.pairwisetesting.ipynb --to html --template template.tpl
#jupyter nbconvert JFonseca.evaluacionPerdidaCalidadAudioOpus.ipynb --to html --template template.tpl
#jupyter nbconvert JFonseca.pruebasFormalesSoftware.ipynb --to html --template template.tpl
#jupyter nbconvert JFonseca.audioVideoQualityStreaming.ipynb --to html --template template.tpl
#jupyter nbconvert JFonseca.wavelets.ipynb --to html --template template.tpl
#jupyter nbconvert JFonseca.consejosIniciarRolAutomatizadorPruebas.ipynb to html --template template.tpl

jupyter nbconvert JFonseca.suavizadoTraficoServidorWeb.ipynb --to html
jupyter nbconvert JFonseca.interpolacionBL.ipynb --to html
jupyter nbconvert JFonseca.pruebasRendimiento.ipynb --to html
jupyter nbconvert JFonseca.pairwisetesting.ipynb --to html
jupyter nbconvert JFonseca.evaluacionPerdidaCalidadAudioOpus.ipynb --to html
jupyter nbconvert JFonseca.pruebasFormalesSoftware.ipynb --to html
jupyter nbconvert JFonseca.audioVideoQualityStreaming.ipynb --to html
jupyter nbconvert JFonseca.wavelets.ipynb --to html
jupyter nbconvert JFonseca.consejosIniciarRolAutomatizadorPruebas.ipynb --to html

sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.interpolacionBL.html > JFonseca.interpolacionBL2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.suavizadoTraficoServidorWeb.html > JFonseca.suavizadoTraficoServidorWeb2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.pruebasRendimiento.html > JFonseca.pruebasRendimiento2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.pairwisetesting.html > JFonseca.pairwisetesting2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.evaluacionPerdidaCalidadAudioOpus.html > JFonseca.evaluacionPerdidaCalidadAudioOpus2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.pruebasFormalesSoftware.html > JFonseca.pruebasFormalesSoftware2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.audioVideoQualityStreaming.html > JFonseca.audioVideoQualityStreaming2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.wavelets.html > JFonseca.wavelets2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.consejosIniciarRolAutomatizadorPruebas.html > JFonseca.consejosIniciarRolAutomatizadorPruebas2.html

rm JFonseca.interpolacionBL.html
rm JFonseca.suavizadoTraficoServidorWeb.html
rm JFonseca.pruebasRendimiento.html
rm JFonseca.pairwisetesting.html
rm JFonseca.evaluacionPerdidaCalidadAudioOpus.html
rm JFonseca.pruebasFormalesSoftware.html
rm JFonseca.audioVideoQualityStreaming.html
rm JFonseca.wavelets.html
rm JFonseca.consejosIniciarRolAutomatizadorPruebas.html

mv JFonseca.interpolacionBL2.html JFonseca.interpolacionBL.html
mv JFonseca.suavizadoTraficoServidorWeb2.html JFonseca.suavizadoTraficoServidorWeb.html
mv JFonseca.pruebasRendimiento2.html JFonseca.pruebasRendimiento.html
mv JFonseca.pairwisetesting2.html JFonseca.pairwisetesting.html
mv JFonseca.evaluacionPerdidaCalidadAudioOpus2.html JFonseca.evaluacionPerdidaCalidadAudioOpus.html
mv JFonseca.pruebasFormalesSoftware2.html JFonseca.pruebasFormalesSoftware.html
mv JFonseca.audioVideoQualityStreaming2.html JFonseca.audioVideoQualityStreaming.html
mv JFonseca.wavelets2.html JFonseca.wavelets.html
mv JFonseca.consejosIniciarRolAutomatizadorPruebas2.html JFonseca.consejosIniciarRolAutomatizadorPruebas.html
