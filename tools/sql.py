from langchain.tools import Tool
import sqlite3
from pydantic.v1 import BaseModel
from typing import List

def sqlite_conn():
    conn = sqlite3.connect("db.sqlite")
    return conn

def list_tables():
    cur = sqlite_conn().cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cur.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)

def run_query(query):
    cur = sqlite_conn().cursor()
    try:
        cur.execute(query)
        result = cur.fetchall()
        return result
    except sqlite3.OperationalError as err:
        return f"The following error occured {str(err)}"

class RunQueryArgsSchema(BaseModel):
    query: str

run_query_tool = Tool.from_function(
    name="run_query",
    description="run a sqlite query",
    func=run_query,
    args_schema=RunQueryArgsSchema
)

def describe_tables(table_names):
    cur = sqlite_conn().cursor()
    tables = ', '.join("'" + table + "'" for table in table_names)
    rows = cur.execute(f"SELECT sql FROM sqlite_master WHERE type='table' and name IN ({tables});")
    return '\n'.join(row[0] for row in rows if row[0] is not None)

class DescribeTablesArgsSchema(BaseModel):
    tables_names: List[str]

describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, returns the schema of those tables",
    func=describe_tables,
    args_schema=DescribeTablesArgsSchema
)