"""
echo.py - Willie Web Search Module
Copyright 2013, Airead Fan, aireadfun.com
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net
"""

def echo(willie, trigger):
    """echo somethings"""
    print "================================="
    print trigger
    print "sender:", trigger.sender
    print "nick:", trigger.nick
    print "event:", trigger.event
    print "bytes:", trigger.bytes
    print "match:", trigger.match
    print "groups:", trigger.groups
    print "args:", trigger.args
    print "admin:", trigger.admin, ", list:", willie.config.core.get_list('admins')
    print "owner:", trigger.owner, ", owner is", willie.config.owner
    print "host", trigger.host
    print "ops:", trigger.ops
    print "isop:", trigger.isop
echo.commands = ['echo', 'e']
echo.priority = 'high'
echo.example = '.echo'