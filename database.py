import os
from sqlalchemy import create_engine, text

db_conn_str=os.environ['DB_CONN_STR']

engine = create_engine(
  db_conn_str, 
  connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_jobs():
  with engine.connect() as conn:
    result=conn.execute(text("select * from jobs"))
    col_names=result.keys()
    jobs=[]
    for row in result.all():
      jobs.append(dict(zip(col_names, row)))
    return jobs

def load_job(id):
  with engine.connect() as conn:
    result=conn.execute(
      text(f"select * from jobs where id = {id}")
    )
    rows=[]
    for row in result.all():
      rows.append(row._mapping)
    if len(rows)==0:
      return None
    else:
      return [dict(row) for row in rows]