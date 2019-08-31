import datetime
import os
from ariadne import ScalarType

datetime_scalar = ScalarType("Datetime")


@datetime_scalar.value_parser
def parse_datetime_value(value):
    if value:
        try:
            return datetime.fromtimestamp(value)
        except Exception as e:
            if os.getenv('ENV') != 'prod':
                raise e
            raise ValueError(f'The datetime value ({value}) is not valid,'
                             'please provide a timestamp.')
