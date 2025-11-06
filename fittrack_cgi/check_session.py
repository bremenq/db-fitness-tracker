#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auth_utils

print("Content-Type: application/json")
print()

user = auth_utils.check_session()
if user:
    print('{"logged_in": true, "username": "' + user['username'] + '"}')
else:
    print('{"logged_in": false}')
