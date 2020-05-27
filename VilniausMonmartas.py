import re
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.vilniausmonmartras.lt/butai')
rg_link = re.compile(
	'<tr><td><strong>(.*?)</strong></td><td>(.*?)kambariai</td><td>(.*?)m<sup>2</sup></td><td>.(.)aukštas</td><tdclass=.*?>(.*?)</td><td>(.*?)</td><tdclass=.*?>(.*?)</td><tdclass=.*?><ahref=(.*?)class=.*?title=.*?>.*?</a></td></tr>'
)
