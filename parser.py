import re


rtitle = r'<title[^>]*>([^<]+)</title>'
rhref = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def get_title_and_hrefs(html):
    title = re.findall(rtitle, html)[0]
    hrefs = re.findall(rhref, html)
    return title, hrefs
