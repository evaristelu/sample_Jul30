import bs4, requests, urllib2, lxml.html
from bs4 import BeautifulSoup


broken_html = '<ul class = country><li>Area<li>Population</ul>'

soup = BeautifulSoup(broken_html, 'html.parser')

fixed_html = soup.prettify()

print fixed_html
print '\n\n'


tree = lxml.html.fromstring(broken_html)
fixed_html2 = lxml.html.tostring(tree, pretty_print=True)
print fixed_html2


def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading', url
    header = {'user_agent': 'user_agent'}
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error', e.reason
        html = None
        err = hasattr(e, 'code')
        print err
    return html


# download('http://www.meetup.com')
#
# Command + Option + Shift + [

