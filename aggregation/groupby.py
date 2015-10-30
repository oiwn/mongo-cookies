import pprint
import logging
from faker import Factory
from workout import MongoWorkout

logger = logging.getLogger(__name__)


class GroupBySimple(MongoWorkout):
    """ Show how to group elements
    """
    name = 'GroupBySimple'
    collection = 'groupbysimple'

    # pipeline to find duplicates
    pipeline = []

    def prepare(self):
        fake = Factory.create('en_US')
        for num in range(1, 6):
            document = {
                'number': num,
                'name': fake.name(),
            }
            doc = self.insert_document(document.copy())
            logger.info("Original: {}".format(doc))

            for _ in range(1, num):
                doc = self.insert_document(document.copy())
                logger.info("Duplicate: {}".format(doc))

    def run(self):
        results = self.db[self.collection].aggregate(self.pipeline)
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(list(results))
