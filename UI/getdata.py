import pandas as pd
import sqlite3

#db데이터 저장
class getdata_db():
    # read db life_list
    conn = sqlite3.connect("life.db")
    Life = pd.read_sql("SELECT * FROM life", conn, index_col=None)
    dbLife_list = Life.values.tolist()

    # read db etc
    conn = sqlite3.connect("etc.db")
    etc = pd.read_sql("SELECT * FROM Etc", conn, index_col=None)
    dbetc_list = etc.values.tolist()

