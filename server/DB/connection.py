# USE THIS FOR LOCAL DB CONNECTIONS / OS LEVEL DATABASES

# import os
# import ssl
# from dotenv import load_dotenv
# from sqlalchemy import text
# from sqlalchemy.ext.asyncio import create_async_engine

# load_dotenv()

# DB_USER = os.getenv('DB_USER')
# DB_PASS = os.getenv('DB_PASS')
# DB_HOST = os.getenv('DB_HOST')
# DB_NAME = os.getenv('DB_NAME')
# DB_PORT = os.getenv('DB_PORT')

# DB_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# # Create a default SSL context for secure transport
# ssl_context = ssl.create_default_context(cafile="asset-management-db-ssl-public-cert.cert")

# # Pass the SSL context to the underlying aiomysql driver
# engine = create_async_engine(
#     DB_URL, 
#     pool_pre_ping=True,
#     connect_args={"ssl": ssl_context}
# )

# async def query(sql, params=None):
#     if params is None:
#         params = {}

#     async with engine.connect() as connection:
#         res = await connection.execute(text(sql), params)

#         if res.returns_rows:
#             return [dict(row._mapping) for row in res]
        
#         return {"inserted_id": res.lastrowid, "affected_rows": res.rowcount}
# -------------------------------------------------------------------------------

# USE THIS FOR REMOTE DATABASE CONNECTIONS

import os
import pymysql
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = int(os.getenv('DB_PORT'))
SSL_CA_FILE = os.getenv("SSL_CA_FILE")

def get_connection():
    """Establishes and returns a new database connection."""
    return pymysql.connect(
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        ssl={
            "ca": SSL_CA_FILE,
            "check_hostname": True
        }
    )

def query(sql, params=None):
    """Executes a SQL query and handles the connection lifecycle."""
    if params is None:
        params = {}

    cnx = get_connection()
    try:
        # pymysql uses DictCursor class instead of dictionary=True
        cursor = cnx.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute(sql, params)

        if cursor.description is not None:
            results = cursor.fetchall()
            return results
        else:
            cnx.commit()
            return {
                "inserted_id": cursor.lastrowid, 
                "affected_rows": cursor.rowcount
            }
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
            
        # pymysql uses the .open property
        if cnx.open:
            cnx.close()