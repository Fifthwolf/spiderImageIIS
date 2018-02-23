# -*- coding: UTF-8 -*-
import cgi, urllib, re
import public

print("Content-Type: text/html\n")

info = public.GetValue(cgi.FieldStorage())

images = info.get('images')
common = info.get('common')[0]
path = info.get('path')[0]

if path[len(path) - 1] != '/':
    path = path + '/'

for img in images:
    file = re.findall(r"\/([^/]+)(\.\w+$)", img)

    #B站img加http
    if common == 2:
        img = 'http:'+ img

    print path + str(file[0][0]) + str(file[0][1])
    urllib.urlretrieve(img, path + str(file[0][0]) + str(file[0][1]))

print 1