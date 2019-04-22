#/usr/bin/env python
# -*- coding:utf-8 -*-

import random

import pandas as pd
import platform
import json
from pymongo import MongoClient
import matplotlib.pyplot as plt



class MgDB:
    def __init__(self,params_file):
        self._platform = platform.system()  # Get platform type
        # Windows will be : Windows
        # Linux will be : Linux
        file_name = ""
        if self._platform == 'Windows':
            self._file_path = "D:\config"
            file_name = self._file_path + "\{}".format(params_file)
        elif self._platform == 'Linux':
            self._file_path = "/home"
            file_name = self._file_path + "/{}".format(params_file)
            # file_name = "/home/{}".format(params_file)
        with open(file_name, 'r') as fr:
            self.params = json.load(fr)

        print(self.params)

        self.conn = MongoClient('127.0.0.1', 27017)
        self.db = self.conn.cqdata

    def insert(self,coll_name,data):
        self.db[coll_name].insert(data)

    def get_collection(self,coll_name):

        return self.db[coll_name]


if __name__ == '__main__':
    mydb = MgDB('db_params.json')
    data = {'name':'robin','age':32}
    mydb.insert('test',data)

    my_coll = mydb.get_collection('test')
    df = pd.DataFrame(list(my_coll.find()))
    print(df)

