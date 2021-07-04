#!/bin/sh
var=$(date +"%d_%m_%Y")
python download_epaper.py
python convert_to_pdf.py
mkdir ${var}
mv *.png ${var}
mv *.pdf ${var}
