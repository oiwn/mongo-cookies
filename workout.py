""" Base class to build mongodb cookies
"""
from settings import db_connection


class MongoWorkout(object):
    db = None
    name = 'default'  # name of example
    collection = 'test'  # define collection used

    def __init__(self):
        self.db = db_connection()

        # prepare run and cleanup database
        self.prepare()
        self.run()
        self.cleanup()

    def prepare(self):
        """ Put some data into the database
        """
        pass

    def cleanup(self):
        """ Cleanup collection
        """
        self.db[self.collection].drop()

    def run(self):
        raise NotImplemented("{} is not implemented".format(self.name))
