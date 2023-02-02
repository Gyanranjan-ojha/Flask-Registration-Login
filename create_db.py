import pymysql
import os
import traceback
import datetime
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(verbose=True,dotenv_path=env_path)

db_name = os.getenv("MYSQL_DB")

def create_database():
  try:
    mysql_conn = pymysql.connect(
      host=os.getenv("MYSQL_HOST"),
      user=os.getenv("MYSQL_USER"),
      password=os.getenv("MYSQL_PASSWORD"),
      port=int(os.getenv("MYSQL_PORT"))
    )
    cur = mysql_conn.cursor()
    cur.execute("SHOW DATABASES")
    dbs = []
    for i in cur.fetchall():
      dbs+=i
    if db_name not in dbs:
      cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
      print(f"INFO - {datetime.datetime.now()} {db_name} database successfully created...")
    # else:
    #   print(f"INFO - {datetime.datetime.now()} {db_name} database already existed...")
    mysql_conn.close()
  except Exception:
    print(traceback.format_exc())