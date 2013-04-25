#!-*-coding: utf-8 -*-
"""
Copyright 2013, Airead Fan, aireadfun.com
Licensed under the Eiffel Forum License 2.

http://www.aireadfun.com
"""

"""
http://www.weather.com.cn/data/sk/101281601.html 
{
    "weatherinfo": {
        "city": "哈尔滨", // 城市中文名
        "city_en": "haerbin", // 城市英文名
        "date_y": "2012年8月18日", // 发布日期
        "date": "", // ?
        "week": "星期六", // 周信息
        "fchh": "18", // ？
        "cityid": "101050101", // 城市ID
        "temp1": "18℃~26℃", // 今日气温
        "temp2": "17℃~29℃", // 明日气温
        "temp3": "18℃~23℃", // 第三日气温
        "temp4": "13℃~24℃", // 第四日气温
        "temp5": "15℃~31℃", // 第五日气温
        "temp6": "14℃~32℃", // 第六日气温
        "tempF1": "64.4℉~78.8℉", // 今日气温（华氏）
        "tempF2": "62.6℉~84.2℉", // 明日气温（华氏）
        "tempF3": "64.4℉~73.4℉", // 第三日气温（华氏）
        "tempF4": "55.4℉~75.2℉", // 第四日气温（华氏）
        "tempF5": "59℉~87.8℉", // 第五日气温（华氏）
        "tempF6": "57.2℉~89.6℉", // 第六日气温（华氏）
        "weather1": "多云", // 今日天气
        "weather2": "晴转多云", // 明日天气
        "weather3": "雷阵雨转小雨", // 第三日天气
        "weather4": "多云", // 第四日天气
        "weather5": "晴", // 第五日天气
        "weather6": "晴", // 第六日天气
        "img1": "1", // ? 可能是天气图标编号
        "img2": "99", // ? 可能是天气图标编号
        "img3": "0", // ? 可能是天气图标编号
        "img4": "1", // ? 可能是天气图标编号
        "img5": "4", // ? 可能是天气图标编号
        "img6": "7", // ? 可能是天气图标编号
        "img7": "1", // ? 可能是天气图标编号
        "img8": "99", // ? 可能是天气图标编号
        "img9": "0", // ? 可能是天气图标编号
        "img10": "99", // ? 可能是天气图标编号
        "img11": "0", // ? 可能是天气图标编号
        "img12": "99", // ? 可能是天气图标编号
        "img_single": "1", // ? 可能是天气图标编号
        "img_title1": "多云", // ? 可能是天气图标对应的 title
        "img_title2": "多云", // ? 可能是天气图标对应的 title
        "img_title3": "晴", // ? 可能是天气图标对应的 title
        "img_title4": "多云", // ? 可能是天气图标对应的 title
        "img_title5": "雷阵雨", // ? 可能是天气图标对应的 title
        "img_title6": "小雨", // ? 可能是天气图标对应的 title
        "img_title7": "多云", // ? 可能是天气图标对应的 title
        "img_title8": "多云", // ? 可能是天气图标对应的 title
        "img_title9": "晴", // ? 可能是天气图标对应的 title
        "img_title10": "晴", // ? 可能是天气图标对应的 title
        "img_title11": "晴", // ? 可能是天气图标对应的 title
        "img_title12": "晴", // ? 可能是天气图标对应的 title
        "img_title_single": "多云", // ? 可能是天气图标对应的 title
        "wind1": "西南风小于3级转西风3-4级", // 今日风向风力信息
        "wind2": "西风小于3级转西南风3-4级", // 明日风向风力信息
        "wind3": "西南风小于3级转3-4级", // 第三日风向风力信息
        "wind4": "西南风小于3级转3-4级", // 第四日风向风力信息
        "wind5": "西南风小于3级转3-4级", // 第五日风向风力信息
        "wind6": "西南风小于3级转3-4级", // 第六日风向风力信息
        "fx1": "西南风", // ? 
        "fx2": "西风", // ? 
        "fl1": "小于3级转3-4级", // 今日风力信息
        "fl2": "小于3级转3-4级", // 明日风力信息
        "fl3": "小于3级转3-4级", // 第三日风力信息
        "fl4": "小于3级转3-4级", // 第四日风力信息
        "fl5": "小于3级转3-4级", // 第五日风力信息
        "fl6": "小于3级转3-4级", // 第六日风力信息
        "index": "热",
        "index_d": "天气较热，建议着短裙、短裤、短套装、T恤等夏季服装。年老体弱者宜着长袖衬衫和单裤。",
        "index48": "炎热",
        "index48_d": "天气炎热，建议着短衫、短裙、短裤、薄型T恤衫、敞领短袖棉衫等清凉夏季服装。",
        "index_uv": "中等", // 紫外线信息
        "index48_uv": "弱", // ? 48 小时紫外线信息
        "index_xc": "较适宜", // ? 
        "index_tr": "适宜", // ? 旅游指数
        "index_co": "舒适", // ? 舒适指数
        "st1": "25",
        "st2": "17",
        "st3": "28",
        "st4": "19",
        "st5": "18",
        "st6": "16",
        "index_cl": "较适宜", // ? 晨练指数
        "index_ls": "适宜", // ? 晾晒指数
        "index_ag": "极易发"
    }
}
"""

import urllib
import json

townInfos = {}

def getCityInfos():
    d = {}

    try:
        file = open("willie/modules/townid.txt", "r")
    except Exception as e:
        print e
        return d
    contents = file.readlines()
    file.close()
    
    for line in contents:
        list = line.split()
        d[list[1]] = list[0]

    return d

def getHtml(url):
    if not url:
        return 'no url'

    try:
        page = urllib.urlopen(url)
    except Exception as e:
        print e
        return "urlopen exception"

    html = page.read()
    page.close()
    return html

def getRealidUrl(townid):
    url = 'http://m.weather.com.cn/data5/city%s.xml' % townid
    return url

def getTownRealID(location):
    townid = townInfos[location.encode('utf-8')]
    print "townid:", townid
    url = getRealidUrl(townid)
    print "realid url:", url
    html = getHtml(url)
    print html
    realid = html.split('|')[1]

    return realid
    
def getWeatherUrl(realid):
    url = 'http://m.weather.com.cn/data/%s.html' % realid
    return url

def getWeatherInfo(realid):
    url = getWeatherUrl(realid)
    html = getHtml(url)
    info = json.loads(html)
    return info
    
def infoGet(info, key):
    return info['weatherinfo'][key]

def getWeatherMsg(info):
    """
    ['city date_y week 今日气温temp1, weather1, wind1, index_d',
    '明天气温temp2, weather2, wind2']
    """
    i = info
    msg = []
    tmp = u"%s 今日气温%s, %s, %s, %s" % (infoGet(i, 'city'), infoGet(i, 'temp1'), infoGet(i, 'weather1'), infoGet(i, 'wind1'), infoGet(i, 'index_d'))
    msg.append(tmp)
    tmp = u"明天气温%s, %s, %s" % (infoGet(i, 'temp2'), infoGet(i, 'weather2'), infoGet(i, 'wind2'))
    msg.append(tmp)

    return msg

def weatherReport(location):
    global townInfos
    
    if townInfos == {}:
        townInfos = getCityInfos()
        if townInfos == {}:
            return "read cityinfos failed"
    realid = getTownRealID(location)
    weatherInfo = getWeatherInfo(realid)
    print location, "id", realid
    # print json.dumps(weatherInfo, indent = 4)
    msg = getWeatherMsg(weatherInfo)
    return msg

def weather(willie, trigger):
    """.weather location - Show the weather at the given location."""
    location = trigger.group(2)
    if not location:
        location = u"北京"
        
    print 'location:', location
    info = weatherReport(location)
    print info[0]
    willie.say(info[0])
    willie.say(info[1])
weather.commands = ['weather', 'w']
weather.example = '.weather 洛阳'