import pprint
import random
import logging
from faker import Factory
from workout import MongoWorkout


logger = logging.getLogger(__name__)


class RemoveDuplicates(MongoWorkout):
    """ Show how to remove duplicates from file
    using aggregation pipeline
    """
    name = 'RemoveDuplicates'
    collection = 'removeDuplicates'

    # pipeline to find duplicates
    pipeline = [
        {
            "$group": {
                "_id": {
                    "number": "$number",
                    "name": "$name",
                },
                "duplicateIds": {"$addToSet": "$_id"},
                "count": {"$sum": 1},
            },
        },
        {
            "$match": {
                "count": {
                    "$gt": 1,
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "duplicateIds": "$duplicateIds",
                "count": "$count",
            }
        }
    ]

    def prepare(self):
        fake = Factory.create('en_US')
        for num in range(0, 10):
            document = {
                'number': num,
                'name': fake.name(),
            }
            doc = self.insert_document(document.copy())
            logger.info("Original: {}".format(doc))

            repeat = random.randint(1, 6)
            for _ in range(1, repeat):
                doc = self.insert_document(document.copy())
                logger.info("Duplicate: {}".format(doc))

    def run(self):
        results = self.db[self.collection].aggregate(self.pipeline)
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(list(results))
