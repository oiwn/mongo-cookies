""" Show how to remove duplicates from file

"""
from workout import MongoWorkout


class RemoveDuplicates(MongoWorkout):
    collection = 'removeDuplicates'

    def run(self):
        print "HERE!"
