# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestClass::test_dyo_no_id 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 9,
                    'line': 1
                }
            ],
            'message': 'Cannot query field "name" on type "Dyo".'
        },
        {
            'locations': [
                {
                    'column': 3,
                    'line': 1
                }
            ],
            'message': 'Field "dyo" argument "id" of type "String!" is required but not provided.'
        }
    ]
}
