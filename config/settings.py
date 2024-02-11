from decouple import config

LOG_LEVEL = config("LOG_LEVEL", default="INFO")
TOKEN = config("TOKEN")
TRANSACTIONS_OUTPUT_TABLE = config("TRANSACTIONS_OUTPUT_TABLE")
POSITIONS_OUTPUT_TABLE = config("POSITIONS_OUTPUT_TABLE")
SECURITIES_OUTPUT_TABLE = config("SECURITIES_OUTPUT_TABLE")
BUYINGPOWERS_OUTPUT_TABLE = config("BUYINGPOWERS_OUTPUT_TABLE")
INSERTER_MAX_RETRIES = config("INSERTER_MAX_RETRIES", default=3, cast=int)
REQUEST_MAX_RETRIES = config("REQUEST_MAX_RETRIES", default=3, cast=int)
REQUEST_BACKOFF_FACTOR = config("REQUEST_BACKOFF_FACTOR", default=2, cast=float)
MSSQL_SERVER = config("MSSQL_SERVER")
MSSQL_DATABASE = config("MSSQL_DATABASE")
MSSQL_USERNAME = config("MSSQL_USERNAME")
MSSQL_PASSWORD = config("MSSQL_PASSWORD")
