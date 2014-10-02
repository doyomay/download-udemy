# -*- coding: utf-8 -*-

__author__ = 'Gerardo May'

import json
import os
import shutil
import re

json_data = open('curriculum.json')


def renombrar_carpetas(id, nombre, seccion):
    path = 'C:\\Users\\Gerardo May\\Desktop\\udemy-final-downloads\\'
    directorios = os.listdir(path)
    seccion = re.sub('[:\"\'\\\*?<>|]', '\'', seccion)
    print seccion

    nombre_seccion = os.path.join(path, seccion)

    if not os.path.isdir(nombre_seccion):
        try:
            os.mkdir(nombre_seccion)
            print "se creo la carpeta", nombre_seccion
        except:
            print "algo malo paso"
    if id in directorios:
        fullpath = os.path.join(path, id)
        path_rename = os.path.join(path, nombre)
        os.rename(fullpath, path_rename)
        shutil.move(path_rename, nombre_seccion)
        print path_rename

data = json.load(json_data)

video = 0
secciones = 0


for i in data:
    for j in i:
        if i[j] == 'chapter' and j != '__class':
            print ""
            print "**************** %s *******************" % i['title']
            print ""
            print ""
            secciones += 1
            seccion = "%s %s" % (secciones, i['title'])
        if j == 'asset':
            for k in i[j]:
                if k == 'id':
                    video += 1
                    renombrar_carpetas(i[j]['id'], i[j]['title'], seccion)

print ""
print ""
print "Total videos", video
print "Total secciones", secciones


json_data.close()
