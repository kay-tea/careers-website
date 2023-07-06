from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://cntjtjv9tqkpai3tekb3:pscale_pw_dRXDrRow4EVAgrRXCr9zPgEiBL9ene7B5575CY29qD@aws.connect.psdb.cloud/careers?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={'ssl': {'ssl-ca': '/etc/ssl/cert.pem'}})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
