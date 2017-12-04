import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')


print res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)


'''
try:
    res.raise_for_status()
except Exception as exc:
    print res.raise_for_status()
    print 'there is a problem: %s' %exc
'''