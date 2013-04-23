"""
echo.py - Willie Web Search Module
Copyright 2013, Airead Fan, aireadfun.com
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net
"""

import re
import willie.web as web
import json

def echo(willie, trigger):
    """echo somethings"""
    print trigger
echo.commands = ['e', 'echo']
echo.priority = 'high'
echo.example = '.echo'