# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:19:30 2019

@author: Yi-Shiang chang
"""
import logging
from msilib.schema import Error
import cx_Oracle
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


# 類別 (物件導向特色)
class DbConnector:
    # 建構子
    def __init__(self, database_info='ys_economic', user_info='postgres', password_info='951612',
                 host_info='localhost', port_info='5432', db_type='postgres'):
        # self 代表自身
        self.db_type = db_type  # 屬性 或稱 field
        self.database_info = database_info # 資料庫的名稱
        self.user_info = user_info # 使用者帳號
        self.password_info = password_info # 使用者密碼
        self.host_info = host_info # 資料庫seerver 位置 IP
        self.port_info = port_info # 開放的port

        if self.db_type == 'oracle':
            dsn_tns = cx_Oracle.makedsn(self.host_info, self.port_info, service_name=self.database_info)
            self.connection = cx_Oracle.connect(user=self.user_info, password=self.password_info, dsn=dsn_tns,
                                                encoding='UTF-8')
            self.cursor = self.connection.cursor()
        else:
            # 建立連線
            self.connection = psycopg2.connect(user=self.user_info, password=self.password_info, host=self.host_info,
                                               port=self.port_info, database=self.database_info)
            self.cursor = self.connection.cursor()
        self.engine = create_engine('postgresql://' + self.user_info + ':' + self.password_info + '@'
                                    + self.host_info + ':' + self.port_info + '/' + self.database_info, echo=False)
    def _close_cursor(self):
        self.cursor.close()

    def _close_connection(self):
        self.connection.close()

    def read_from_db(self, sql_list):
        if self.db_type == 'oracle':
            try:
                query_result_list = []
                for query in sql_list:
                    self.cursor.execute(query)
                    data = self.cursor.fetchall()
                    cols = list(map(lambda x: x[0], self.cursor.description))
                    dataframe = pd.DataFrame(data, columns=cols)
                    query_result_list.append(dataframe)
                    self.connection.commit()
            except (Exception, cx_Oracle.Error) as error:
                logging.info("Error while connecting to Oracle\n, The error is{}".format(error))
                self.cursor.execute("ROLLBACK")
            finally:
                if len(query_result_list) == 0:
                    return [pd.DataFrame([])]
                else:
                    return query_result_list
        elif self.db_type == 'postgres':
            try:
                query_result_list = []
                for query in sql_list:
                    self.cursor.execute(query)
                    data = self.cursor.fetchall()
                    # map(函數, 可跌代物件)
                    cols = list(map(lambda x: x.name, self.cursor.description))
                    dataframe = pd.DataFrame(data, columns=cols)
                    query_result_list.append(dataframe)
                    self.connection.commit()
                    # print(cols)
            except (Exception, cx_Oracle.Error) as error:
                self.cursor.execute("ROLLBACK")
                print("Error while connecting to postgres, The error is\n{}".format(error))
                logging.info("Error while connecting to postgres, The error is\n{}".format(error))
            finally:
                if len(query_result_list) == 0:
                    return [pd.DataFrame([])]
                else:
                    return query_result_list

    def upload_to_db(self, dataframe, schema, table):
        if self.db_type == 'postgres':
            # logging.info("# Upload to：{}".format(schema))
            # create query
            col_list = list(dataframe.columns)
            col_str = ','.join(col_list)
            insert_query = """ INSERT INTO {}.{} ({}) VALUES""".format(schema, table, col_str)
            dataframe = dataframe.astype(str)
            dataframe = str(tuple(dataframe.itertuples(index=False, name=None)))
            if len(col_list) == 1:
                raise AssertionError("這裡有問題")
                # dataframe = dataframe[1:-1].replace(',', "")
            else:
                dataframe = dataframe[1:-1]  # 去掉前後括號
            insert_query = insert_query + dataframe
            try:
                self.cursor.execute(insert_query)
                self.connection.commit()
            except (Exception, psycopg2.Error) as error:
                raise AssertionError("Error while connecting to PostgreSQL", error)
        else:
            raise ValueError("No support")

    def upload_to_db_not_exist(self, dataframe, table, schema, primary_key):
        if isinstance(primary_key, list):
            primary_key_copy = primary_key
            primary_key = ""
            for key in primary_key_copy:
                primary_key += key+','
            primary_key = primary_key.rstrip(',')
        if self.db_type == 'postgres':
            col_list = list(dataframe.columns)
            col_str = ','.join(col_list)
            col_str = "({})".format(col_str)
            df = dataframe.copy()
            df.reset_index(drop=True, inplace=True)
            dataframe = dataframe.astype(str)
            if dataframe.shape[0] == 1:
                one_tag = True
            else:
                one_tag = False
            if one_tag:
                dataframe = str(tuple(dataframe.itertuples(index=False, name=None)))[1:-1].rstrip(',')
            else:
                dataframe = str(tuple(dataframe.itertuples(index=False, name=None)))[1:-1]
            insert_query = """INSERT into {}.{} {} values {} ON CONFLICT ({}) DO NOTHING;""".format(
                schema, table, col_str, dataframe, primary_key)
            self.cursor.execute(insert_query)
            self.connection.commit()
        else:
            raise ValueError("No support")

    def exe_sql(self, sql_list):
        if self.db_type == 'postgres':
                for sql in sql_list:
                    self.cursor.execute(sql)
                    self.connection.commit()
        else:
            raise ValueError("No support")



a = DbConnector()
b = DbConnector()