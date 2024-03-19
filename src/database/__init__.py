"""The Database package is used to query the database."""
from .database_manager import DatabaseManager
from utils.paths import DATABASE_PATH, TABLES_SQL_PTH, SQL_PATH_FILES, IN_GAME_SQL_PATH

DBManager = DatabaseManager(DATABASE_PATH, TABLES_SQL_PTH, SQL_PATH_FILES, IN_GAME_SQL_PATH)
# Import this instance and use it every time it is needed to make a query.
__all__ = ['DBManager']