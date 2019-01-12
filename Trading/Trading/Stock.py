import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

class Stock(object):
    def exec(self):
        start = datetime.datetime(2018, 12, 1)
        end = datetime.datetime(2018, 12, 15)
        df = web.DataReader("078930.KS", "yahoo", start, end)
        print(df.head())
        con = sqlite3.connect("kospi.db")
        df.to_sql('078930', con, if_exists='replace')
        con.close()

    def read_head(self):
        con = sqlite3.connect("kospi.db")
        readed_df = pd.read_sql("SELECT * FROM '078930' order by Date desc", con, index_col = 'Date')
        con.close()
        print(readed_df.head())


if __name__=='__main__':
    stock = Stock()
    stock.exec('')


