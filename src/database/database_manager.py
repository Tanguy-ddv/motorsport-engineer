"""
The Database Manager is used to address queries to the database.
"""
import sqlite3 as sql
import os

class DatabaseManager:
    """The Database Manager is used to adress queries to the database."""

    def __init__(self, db_path: str, table_sql_path: str,  script_path_folder, debug: bool=False) -> None:
        """
        Initialize an instance of DatabaseManager.
        
        args:
        db_path: The path to the database.
        table_sql_path: the path to the sql file that creates tables.
        script_path_folder: the folder containging all the sql files to be executed.
        debug: when passed to true, the delation of the database is not done at the destruction of the instance.
        """
        self.__db_path = db_path
        self.__debug = debug
        self.__create_database(table_sql_path, script_path_folder)
        

    def __execute_select_query(self, query: str):
        """Execute a select query on the database."""
        if not query.startswith("SELECT"):
            print("The query is wrong:\n", query, "\nShould start by 'SELECT'")
        if not os.path.isfile(self.__db_path):
            print("The database has not been created yet.")
        try:
            conn = sql.connect(self.__db_path)
            cur = conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
            description = [description[0] for description in cur.description]
            cur.close()
            conn.close()
            return result, description
        except sql.Error as error:
            print("An error occured while querying the database with:\n",query,"\n",error)

    def __execute_insert_query(self, query: str):
        """Execute an insert query on the database."""
        if not query.startswith("INSERT INTO"):
            print("The query is wrong:\n", query, "\nShould start by 'INSERT INTO'")
            return None
        if not os.path.isfile(self.__db_path):
            print("The database has not been created yet.")
            return None
        try:
            conn = sql.connect(self.__db_path)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            cur.close()
            conn.close()
        except sql.Error as error:
            print("An error occured while querying the database with:\n",query,"\n",error)

    def __execute_sql_script(self, script_path: str):
        """Execute a script query on the database."""
        conn = sql.connect(self.__db_path)
        cur = conn.cursor()
        with open(script_path, 'r', encoding='utf-8') as f:
            script = f.read()
        if script:
            cur.executescript(script)
            conn.commit()
        conn.close()

    def __create_database(self, table_sql_path: str ,script_path_folder: str):
        """
        Create the database and execute the scripts in it.

        table_sql_path: the path to the sql file that creates tables.
        script_path_folder: the path to the folder containing all the scripts.
        """
        if os.path.exists(self.__db_path):
            os.remove(self.__db_path)
        
        conn = sql.connect(self.__db_path)
        conn.close()

        self.__execute_sql_script(table_sql_path)

        script_file_paths = []
        for root, _, files in os.walk(script_path_folder):
            for file in files:
                if file.endswith('.sql') and file != table_sql_path:
                    script_file_paths.append(os.path.join(root, file))

        for script_path in script_file_paths:
            print(script_path)
            self.__execute_sql_script(script_path)

    def __del__(self):
        """Destroy the DatabaseManager. Delete the database"""
        if os.path.exists(self.__db_path) and not self.__debug:
            os.remove(self.__db_path)
