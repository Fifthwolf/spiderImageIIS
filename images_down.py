# -*- coding: UTF-8 -*-
import cgi, urllib, re, os
import public

print("Content-Type: text/html\n")

def mkdir(path):
    if not os.access(path, os.R_OK):
        path_last = len(path) - 1
        if path[path_last] == '/' or path[path_last] == '\\':
            path = path[0: path_last]

        mkdir(os.path.dirname(path))

        if not os.path.isfile(path):
            os.mkdir(path, 0755)

info = public.GetValue(cgi.FieldStorage())

images = info.get('images')
path = info.get('path')[0]

if path[len(path) - 1] != '/':
    path = path + '/'

mkdir(path)

for img in images:
    file = re.findall(r"\/([^/]+\.\w+$)", img)
    urllib.urlretrieve(img, path + str(file[0]))

print 1
