# -*- coding: utf-8 -*-
"""
Webgunea sortzeko python fitxategiak
Galeria eguneratzeko
"""

import csv

def tohtml(s):
    replacements = (
        ("á", "&aacute;"),
        ("é", "&eacute;"),
        ("í", "&iacute;"),
        ("ó", "&oacute;"),
        ("ú", "&uacute;"),
        ("ñ", "&ntilde;"),
        ("¿", "&iquest;"),
        ("«", "&laquo;"),
        ("»", "&raquo;"),
    )
    for a, b in replacements:
        s = s.replace(a, b);
    return s


def processhitzaldia(ref, title, name, argazkia, youtube):
    code = ref[1:]

    res = '<!-- ' + code + ' -->\n\n'
    res = res + '<div class="portfolio-modal modal fade" id="'+ code +'" tabindex="-1" role="dialog" aria-hidden="true">\n'
    res = res + '   <div class="modal-dialog">\n'
    res = res + '       <div class="modal-content">\n'
    res = res + '           <div class="close-modal" data-dismiss="modal">\n'
    res = res + '               <div class="lr">\n'
    res = res + '                   <div class="rl">\n'
    res = res + '                   </div>\n'
    res = res + '               </div>\n'
    res = res + '           </div>\n'
    res = res + '           <div class="container">\n'
    res = res + '               <div class="row">\n'
    res = res + '                   <div class="col-lg-8 col-lg-offset-2">\n'
    res = res + '                       <div class="modal-body">\n'
    res = res + '                           <div class="row">\n'
    res = res + '                               <div class="col-md-4">\n'
    res = res + '                                   <img src="img/hitzaldiak/' + argazkia + '" class="img-responsive" alt="">\n'
    res = res + '                               </div>\n'
    res = res + '                               <div class="col-md-8">\n'
    res = res + '                                   <h3>' + tohtml(title) + '</h3>\n'
    res = res + '                                   <h2  class="porfolio-izena">' + tohtml(name) + '</h2>\n'
    res = res + '                               </div>\n'
    res = res + '                           </div>\n'
    res = res + '                           <div class="row">\n'
    with open('hitzaldiak/' + code + '.lab', 'r') as file_lab:
        for line in file_lab:
            res = res + '                               ' + tohtml(line) + '\n'

    res = res + '                           </div>\n'
    res = res + '                           <div class="row">\n'
    res = res + '                               <h3>Biografia</h3>\n'
    with open('hitzaldiak/' + code + '.bio', 'r') as file_bio:
        for line in file_bio:
            res = res + '                               ' + tohtml(line) + '\n'

    res = res + '                           </div>\n'
    res = res + '                       </div>\n'
    res = res + '                       </br>\n'
    if youtube!='':
        res = res + '                       <iframe width="640" height="360" src="https://www.youtube.com/embed/' + youtube + '" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>\n'        
    res = res + '                       </br>\n'
    res = res + '                       <button type="button" class="btn btn-primary" data-dismiss="modal"><i class="fa fa-times"></i>Itxi</button>\n'
    res = res + '                   </div>\n'
    res = res + '               </div>\n'
    res = res + '           </div>\n'
    res = res + '       </div>\n'
    res = res + '   </div>\n'
    res = res + '</div>\n'

    return (res)


file_galeria_main = open('parts/01_galeria.io', 'w+')
file_galeria_all = open('parts/01B_galeria_all.io', 'w+')
file_hitzaldiak_main = open('parts/03_hitzaldiak.io', 'w+')
file_hitzaldiak_all = open('parts/03B_hitzaldiak_all.io', 'w+')

with open('hitzaldiak/00_izenburuak.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';',)
    line_count = 0
    row_count = 0
    content = ''
    for row in csv_reader:
        code = str(row[0])
        jpg = str(row[1])
        title = str(row[2])
        name = str(row[3])
        argazkia = str(row[4])
        youtube = str(row[5])

        #Control for the elements in a row and for the rows
        if line_count == 0:
            row_count += 1
            content = '  <div class="row">\n'

        content = content + '      <div class="col-md-3 col-sm-6 portfolio-item">' + '\n'
        content = content + '        <a href="' + code + '" class="portfolio-link" data-toggle="modal">' + '\n'
        content = content + '          <div class="portfolio-hover">' + '\n'
        content = content + '            <div class="portfolio-hover-content">' + '\n'
        content = content + '              <i class="fa fa-plus fa-3x"></i>' + '\n'
        content = content + '            </div>' + '\n'
        content = content + '          </div>' + '\n'
        content = content + '          <img src="img/hitzaldiak/' + jpg + '" class="img-responsive" alt="">'+ '\n'
        content = content + '        </a>' + '\n'
        content = content + '        <div class="portfolio-caption">' + '\n'
        content = content + '          <h4>' + tohtml(title) + '</h4>' + '\n'
        content = content + '          <p class="text-muted">' + tohtml(name) + '</p>' + '\n'
        content = content + '        </div>' + '\n'
        content = content + '      </div>' + '\n'

        if line_count == 3:
            content = content + '  </div>\n\n'
            line_count = -1;
            if row_count <= 2:
                file_galeria_main.write(content)
            else:
                file_galeria_all.write(content)
            content = ''
        line_count += 1

        try:
            modal = processhitzaldia(code, title, name, argazkia, youtube)
        except:
            modal = ''

        if row_count < 3:
            file_hitzaldiak_main.write(modal)
            file_hitzaldiak_main.write('\n\n')
        else:
            file_hitzaldiak_all.write(modal)
            file_hitzaldiak_all.write('\n\n')


content = content + '  </div>\n\n'
if row_count <= 2:
    file_galeria_main.write(content)
else:
    file_galeria_all.write(content)
