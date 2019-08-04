#!/bin/bash
ipython nbconvert --to html JFonseca.suavizadoTraficoServidorWeb.ipynb
ipython nbconvert --to html JFonseca.interpolacionBL.ipynb

sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.interpolacionBL.html > JFonseca.interpolacionBL2.html
sed 's/max-width: calc(100% - 14ex);/max-width: 100%;/g' JFonseca.suavizadoTraficoServidorWeb.html > JFonseca.suavizadoTraficoServidorWeb2.html

rm JFonseca.interpolacionBL.html
rm JFonseca.suavizadoTraficoServidorWeb.html

mv JFonseca.interpolacionBL2.html JFonseca.interpolacionBL.html
mv JFonseca.suavizadoTraficoServidorWeb2.html JFonseca.suavizadoTraficoServidorWeb.html

#awk '{gsub(/max-width: calc(100% - 14ex);/,"max-width: 100%;")}' $1.html

#ex -s -c '%s/max-width: calc(100% - 14ex);/max-width: 100%;/g|x' $1.html
