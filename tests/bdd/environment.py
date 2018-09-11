import traceback
import logging


def after_scenario(context, scenario):
    logging.debug('teardown entities')
    for entity in getattr(context, 'created_entities', []):
        try:
            logging.debug('deleting %s', entity)
            entity.delete()
        except Exception:
            logging.warning('teardown could not delete %s:\n%s', entity, traceback.format_exc())
