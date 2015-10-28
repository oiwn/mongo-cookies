import logging
import argparse

from weblib.logs import default_logging

from settings import LOG_LEVEL, TASKS
from utils.run_interface import ScrapersRunInterface


logger = logging.getLogger('cli')


def setup_loggin():
    # setup default logging
    default_logging(grab_log='var/grab.log', level=LOG_LEVEL, mode='a',
                    propagate_network_logger=False,
                    network_log='var/grab.network.log')


if __name__ == '__main__':
    setup_loggin()
    parser = argparse.ArgumentParser(description='command line interface')

    parser.add_argument('-T', '--task', type=str,
                        help='run scraper: {}'.format(TASKS.keys()))

    args = parser.parse_args()

    if args.task:
        scraper = ScrapersRunInterface.crawl(args.task)
        logger.info(scraper.render_stats())
    else:
        print TASKS.keys()
