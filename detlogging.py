import logging
from pprint import pformat

class _CustomAdapter(logging.LoggerAdapter):
    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """
    def process(self, msg, kwargs):
        return pformat(vars(msg)), kwargs


def _logger():
    import logging

    border = '---------------------------------------------------------------------------------'
    message = [ border
              , '{pathname} -> {funcName} L:{lineno}'
              , ''
              , '{message}'
              , border
              ]
    logging.basicConfig(format='\n'.join(message), style='{')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    adapter = _CustomAdapter(logger, '')
    return adapter.debug


detlog = _logger()
