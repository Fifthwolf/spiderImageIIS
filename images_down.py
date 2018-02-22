# -*- coding: UTF-8 -*-
import cgi, urllib
import public

print("Content-Type: text/html\n")

info = public.GetValue(cgi.FieldStorage())

images = info.get('images')
common = info.get('common')

#print images
#print common

print 0

m = 0
path = 'E:/inetpub/wwwroot/pythonproject/img/'
for img in images:
    #B站img加http
    if common == 2:
        img = 'http:'+ img
    urllib.urlretrieve(img, path + str(m) + '.jpg')
    m = m + 1

print 1