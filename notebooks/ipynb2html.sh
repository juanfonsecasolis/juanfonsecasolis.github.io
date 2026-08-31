#!/bin/bash
# References
# 1. https://stackoverflow.com/questions/12317483/array-of-arrays-in-bash#:~:text=The%20basis%20of%20this%20answer,it%20was%20an%20n%2Dd%20array.

NB_CONVERT="python3 -m nbconvert"
FLAGS="--from markdown+footnotes --output-dir='../html' --to html --template=../template.tpl --config=../conf.json --embed-images"

if [[ -z "$1" ]]; then
    echo "No notebook name received, running script against all notebooks registered..."  
    notebooks=("principiosSolid" "transformadaOndeletas" "evaluacionCodecOpus" "pruebasDePares" "pruebasEstresSistemasLIT" "echoesAndReverberations" "movingAverageEarlyAlerts" "interpolationAsymetricKernels")
else
    echo "Running script against '$1'..."
    notebooks=("$1")
fi

for notebook in "${notebooks[@]}"; do
    cd "$notebook"
    $NB_CONVERT "$notebook.ipynb" $FLAGS
    cd ..
done
