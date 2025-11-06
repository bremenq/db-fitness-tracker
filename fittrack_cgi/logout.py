#!/usr/bin/env python3

import cgitb
import sys
import os

cgitb.enable()

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auth_utils

def main():
    destroy_cookie = auth_utils.destroy_session()
    
    print(destroy_cookie)
    print("Location: index.html\n")

if __name__ == '__main__':
    main()

