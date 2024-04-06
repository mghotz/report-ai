from langchain.tools import Tool
import sqlite3

def sqlite_conn():
    conn = sqlite3.connect("db.sqlite")
    return conn

def run_query(query):
    cur = sqlite_conn().cursor()
    cur.execute(query)
    result = cur.fetchall()
    return result


run_query_tool = Tool.from_function(
    name="run_query",
    description="run a sqlite query",
    func=run_query
)