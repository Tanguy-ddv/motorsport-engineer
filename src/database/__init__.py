"""The Database package is used to query the database."""
from database.database_manager import DatabaseManager
from utils.paths import DATABASE_PATH, TABLES_SQL_PTH, SQL_PATH_FILES 

DBManager = DatabaseManager(DATABASE_PATH, TABLES_SQL_PTH, SQL_PATH_FILES)
# Import this instance and use it every time it is needed to make a query.