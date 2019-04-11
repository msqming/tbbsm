#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import pymysql


def f1(data):
    conn = pymysql.connect(
        host='193.112.112.38',
        port=3306,
        user='root',
        passwd='root123.com',
        db='test04',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = "insert into rykc_comminfo (xinghao,pinglei,new_old,dingwei,pingming,cpu,xianka,neicun,ssd,hhd,model_name,config,pn) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cursor.execute(sql, data)
    conn.commit()

    cursor.close()
    conn.close()

data = pd.read_excel('货品基础信息.xlsx')
# print(data)
data1 = data.fillna('none')

for n in range(data1.shape[0]):
    data = tuple(data1.iloc[n])
    print(data)
    f1(data)