import sqlite3 as lite
import pandas as pd



class Member(object):
    def exec(self, input_id, input_pw):
        conn = lite.connect("test.db")
        query = """select * from member where id like '{}' and pass like '{}';""".format(input_id,input_pw)
        df = pd.read_sql_query(query, conn)
        print( df.iloc[:])



if __name__ == '__main__':
    Member.exec(Member, 1,1234)










