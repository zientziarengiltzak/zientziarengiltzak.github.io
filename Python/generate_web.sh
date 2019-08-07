#!/bin/bash

python3 ./izenburuak_prozesatu.py

cat ./parts/00_head.io > index.html
cat ./parts/01_galeria.io >> index.html
cat ./parts/02_inter.io >> index.html
cat ./parts/03_hitzaldiak.io >> index.html
cat ./parts/04_foot.io >> index.html

cat ./parts/00B_head.io > hitzaldiak.html
cat ./parts/01B_galeria_all.io >> hitzaldiak.html
cat ./parts/02B_inter.io >> hitzaldiak.html
cat ./parts/03B_hitzaldiak_all.io >> hitzaldiak.html
cat ./parts/04_foot.io >> hitzaldiak.html


mv -f index.html hitzaldiak.html ./../