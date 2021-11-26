import os
import logging


ROOT_DIR=os.path.dirname(os.path.abspath("config.py")) 


def get_dir_project():
    logging.info(ROOT_DIR)
    return ROOT_DIR