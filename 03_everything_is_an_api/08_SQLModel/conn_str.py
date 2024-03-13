from dotenv import load_dotenv, find_dotenv
import os

_ : bool = load_dotenv(find_dotenv())

conn_str: str = os.environ['DATABASE_CONN_STRING']

# print(conn_str)

