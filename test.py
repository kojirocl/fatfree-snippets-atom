#!/usr/bin/env python

import glob
from lxml import etree

def validar_xml_scope(linea):
    if linea == 'source.php':
        return linea
    else:
        return 'text.html.basic'

def validar_xml_content(ambito, linea):
    if ambito.find("php")==0 and linea.find(";")==-1:
        linea = linea + ";"
    return linea.replace("'","\'")

def arma_cadena_cson(datos):
    src = "\'." + validar_xml_scope(datos.findtext("scope")).strip() + "\':"
    descripcion = "\'" + datos.findtext("description").strip() + "\':"
    lanzador = "\'prefix\': \'" + datos.findtext("tabTrigger").strip() + "\'"
    cuerpo = "\'body\': \"\"\"" + validar_xml_content(src, datos.findtext("content")).strip() + "\"\"\""
    #string = "'"+ doc.findtext("scope")  + "':\n\t'"+ doc.findtext("description") + "':\n" + "\n\t'prefix':'" + doc.findtext("tabTrigger") + "'\n\t'body':'" + doc.findtext("content") + "'"
    return src + "\n\t" + descripcion + "\n\t\t" + lanzador + "\n\t\t" + cuerpo + "\n\n"

def main(lista_archivos, ruta_salida):
    for file in lista_archivos:
        doc = etree.parse(file)
        #texto = texto + arma_cadena_cson(datos=doc)
        entrada = open(file, 'r')
        salida = open (cambia_nombre(entrada.name, ruta_salida), 'w')
        entrada.close()
        salida.write(arma_cadena_cson(doc))
        salida.close()


def cambia_nombre(nombre, ruta):
    return ruta + nombre.split('\\')[1].replace('.sublime-snippet', '.cson')


path = "C:/Users/usuario/Google Drive/fatfree-snippets-master/fatfree-snippets-master/*.sublime-snippet"
path_output = "C:/Users/usuario/Google Drive/fatfree-snippets-master/atom/"

files=glob.glob(path)
texto = ""

if __name__ == "__main__":
    main(files, path_output)
