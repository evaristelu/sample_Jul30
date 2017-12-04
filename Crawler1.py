import re, urllib2, urlparse

def download(url, user_agent='Rafa', num_retries=2):
    print 'downloading url...'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print'Download error'
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                'retry 5** error'
                return download(url, user_agent, num_retries-1)
        return html


def link_crawler(seed_url, link_regex):
    'from seed_url matched by link_regrex'

    crawler_queue = [seed_url]

    seen = set(crawler_queue)

    while crawler_queue:
        url = crawler_queue.pop()
        html = download(url)

        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawler_queue.append(link)


def get_links(html):
    'return list of link from html'

    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)

    return webpage_regex.findall(html)

