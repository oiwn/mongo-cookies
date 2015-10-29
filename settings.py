import logging
from pymongo import MongoClient


DEBUG = True
LOG_LEVEL = logging.DEBUG
logging.basicConfig(format='%(levelname)s: %(message)s')

# http://docs.mongodb.org/manual/reference/connection-string/
MONGO_DB_NAME = 'mongocookies'
MONGO_DB_URI = 'mongodb://localhost:27017/{}'.format(MONGO_DB_NAME)

# mapping for tasks
TASKS = {
    'find-duplicates': 'aggregation.find_duplicates.FindDuplicates',
}


def db_connection():
    client = MongoClient(MONGO_DB_URI.format(''))
    return client[MONGO_DB_NAME]
