import re
import requests

response = requests.get('https://web.archive.org/web/20200327073745/'
                        'https://www.columbia.edu/~fdc/sample.html')

find = re.findall(r'<h3\sid="\w+">(.*?)</h3>', response.text)
print(find)
