#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pymysql

MYSQL_USER     = 'root'
MYSQL_PASSWORD = 'myN3wPassw0rd'
MYSQL_HOST     = 'localhost'
MYSQL_DBNAME   = 'test'

def execMysqlQry(query):
	conn = pymysql.connect(user=MYSQL_USER, passwd=MYSQL_PASSWORD, host=MYSQL_HOST, db=MYSQL_DBNAME, charset='utf8')
	cur = conn.cursor()
	n = cur.execute(query)
	print('运行Mysql语句，影响 %d 行' % n)
	conn.commit()
	cur.close()
	conn.close()



firstQry = "delete from tuser where login='0148'"
execMysqlQry(firstQry)
