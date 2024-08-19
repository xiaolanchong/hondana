import re
import urllib.parse


re_spaces = re.compile(r'(^.+?href=")(.+?)(".+?$)')

with open(r'f:\wodetien\Japanese\hondana\scifi.html', encoding='utf8') as file:
    for line in file.readlines():
        line = line.rstrip()
        m = re_spaces.match(line)
        if not m:
            print(line)
            continue
        prefix, url, suffix = m.groups()
        if 'https://' in url:
            print(line)
            continue
        safe_string = urllib.parse.quote_plus(url)
        url = url.replace(' ', '%20')
        url = url.replace('[', urllib.parse.quote_plus('['))
        url = url.replace(']', urllib.parse.quote_plus(']'))
        print(f'{prefix}{url}{suffix}')
