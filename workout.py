""" Base class to build mongodb cookies
"""
from settings import db_connection


class MongoWorkout(object):
    db = None
    name = 'default'  # name of example

    def __init__(self, collection):
        self.db = db_connection()[collection]

        # prepare run and cleanup database
        self.prepare()
        self.run()
        self.cleanup()

    def prepare(self, data):
        """ Put some data into the database
        """
        pass

    def cleanup(self):
        """ Cleanup collection
        """
        self.db.drop()

    def run(self):
        raise NotImplemented("{} is not implemented".format(self.name))
