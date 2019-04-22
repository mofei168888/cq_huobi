#/usr/bin/env python
# -*- coding:utf-8 -*-

import random

import pandas as pd

from pymongo import MongoClient
import matplotlib.pyplot as plt



class MgDB:
    def __init__(self):
        self.conn = MongoClient('127.0.0.1', 27017)
        self.db = self.conn.cqdata

    def insert(self,coll_name,data):
        self.db[coll_name].insert(data)

    def get_collection(self,coll_name):

        return self.db[coll_name]


if __name__ == '__main__':
    mydb = MgDB()
    my_collection = mydb.get_collection('mt_tickers')
    df = pd.DataFrame(list(my_collection.find()))['data'][0]
    newdf = pd.DataFrame(list(df))
    print(list(newdf['symbol']))
