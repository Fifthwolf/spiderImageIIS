# -*- coding: UTF-8 -*-
import cgi, urllib, re, os, sys
import public

reload(sys)
sys.setdefaultencoding('utf-8')

print("Content-Type: text/html\n")

def mkdir(path):
    if not os.access(unicode(path, 'utf-8'), os.R_OK):
        path_last = len(path) - 1
        if path[path_last] == '/' or path[path_last] == '\\':
            path = path[0: path_last]

        mkdir(os.path.dirname(path))

        if not os.path.isfile(path):
            name = re.findall(r"(.+)\\([^\\]+)", path)[0]
            pathcn = name[0] + '\\' + str(name[1]).strip().decode('utf-8')
            os.mkdir(pathcn)

info = public.GetValue(cgi.FieldStorage())

images = info.get('images')
rootPath = info.get('path')[0]

if rootPath[len(rootPath) - 1] != '\\':
    rootPath = rootPath + '\\'

for img in images:
    file = re.findall(r"(.+),(.+)", img)[0]
    imgSource = file[0]
    filename = re.findall(r"\/([^/]+\.\w+$)", imgSource)[0]
    path = rootPath + file[1]
    mkdir(path)
    urllib.urlretrieve(imgSource, unicode(path, 'utf-8') + '\\' + unicode(filename, 'utf-8'))

print 1
