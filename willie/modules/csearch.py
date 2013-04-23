#!-*-coding: utf-8 -*-
"""
search.py - Willie Web Search Module
Copyright 2008-9, Sean B. Palmer, inamidst.com
Copyright 2012, Edward Powell, embolalia.net
Copyright 2013, Airead Fan, aireadfun.com
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net
"""

import re
import willie.web as web
import json
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def google_ajax(query):
    """Search using AjaxSearch, and return its JSON."""
    if isinstance(query, unicode):
        query = query.encode('utf-8')
    uri = 'http://ajax.googleapis.com/ajax/services/search/web'
    args = '?v=1.0&safe=off&q=' + web.quote(query)
    bytes = web.get(uri + args)
    return json.loads(bytes)

def google_search(query):
    results = google_ajax(query)
    # print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))
    first = results['responseData']['results'][0]
    # print json.dumps(first, sort_keys=True, indent=4, separators=(',', ': '))
    try: return first['unescapedUrl'], first['content']
    except IndexError: return None
    except TypeError:
        return False

def g(willie, trigger):
    """Queries Google for the specified input."""
    print 'trigger.groups', trigger.groups()
    query = trigger.group(2);
    if not query:
        return willie.reply('google what?')
    print 'query is', query
    try:
        uquery = query.encode('utf-8')
    except:
        pass
#   print 'utf-8 query', query #will oops
    uri, content = google_search(uquery)
    content = strip_tags(content)
    if uri:
        if not hasattr(willie.bot, 'last_seen_uri'):
            willie.bot.last_seen_uri = {}
        willie.bot.last_seen_uri[trigger.sender] = uri
    elif uri is False: willie.reply("Problem getting data from Google.")
    else: willie.reply("No results found for '%s'." % query)
    msg = "::%s:: %s - %s" % (query, content, uri)
    print msg
    willie.say(msg)
g.commands = ['google', 'g']
g.rule = ([u'什么是'], r'(.*)')
g.example = '.google netfilter'