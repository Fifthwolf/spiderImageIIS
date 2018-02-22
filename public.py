#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class GetValue(object):

    def __init__(self, form):
        self.form = form

    def get(self, name):
        list = []
        try:
            self.value = self.form[name].value
            list = [self.value]
        except:
            for value in self.form[name]:
                list.append(value.value)
        finally:
            return list