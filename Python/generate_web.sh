#!/bin/bash

python3 ./izenburuak_prozesatu.py

cat 00_head.io > index.html
cat 01_galeria.io >> index.html
cat 02_inter.io >> index.html
cat 03_hitzaldiak.io >> index.html
cat 04_foot.io >> index.html
