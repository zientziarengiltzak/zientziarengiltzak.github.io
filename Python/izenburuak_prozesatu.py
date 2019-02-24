# -*- coding: utf-8 -*-
"""
Webgunea sortzeko python fitxategiak
Galeria eguneratzeko
"""

import csv

def toHTML(s):
    replacements = (
        ("á", "&aacute;"),
        ("é", "&eacute;"),
        ("í", "&iacute;"),
        ("ó", "&oacute;"),
        ("ú", "&uacute;"),
        ("ñ", "&ntilde;"),
        ("?", "&iquest;"),
    )
    for a, b in replacements:
        s = s.replace(a, b);
    return s



file = open('galeria.out','w') 
 
with open('izenburuak.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',',);
    line_count = 0;
    for row in csv_reader:
        if line_count == 0:
            file.write('  <div class="row">\n');
            
        file.write('      <div class="col-md-3 col-sm-6 portfolio-item">' + '\n');
        file.write('        <a href="' + str(row[0]) + '" class="portfolio-link" data-toggle="modal">' + '\n');
        file.write('          <div class="portfolio-hover">' + '\n');
        file.write('            <div class="portfolio-hover-content">' + '\n');
        file.write('              <i class="fa fa-plus fa-3x"></i>' + '\n');
        file.write('            </div>' + '\n');
        file.write('          </div>' + '\n');
        file.write('          <img src="img/hitzaldiak/' + str(row[1]) + '" class="img-responsive" alt="">'+ '\n');
        file.write('        </a>' + '\n');
        file.write('        <div class="portfolio-caption">' + '\n');
        file.write('          <h4>' + toHTML(str(row[2])) + '</h4>' + '\n');
        file.write('          <p class="text-muted">' + toHTML(str(row[3])) + '</p>' + '\n');
        file.write('        </div>' + '\n');
        file.write('      </div>' + '\n');
        
        if line_count == 3:
            file.write('  </div>\n\n');
            line_count = -1;
        line_count += 1


