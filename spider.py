import argparse
import threading
import urllib.request
import urllib.error
from queue import Queue
import time
from parser import get_title_and_hrefs
from storage import Storage


parser = argparse.ArgumentParser()
parser.add_argument('action', choices=['load', 'get'])
parser.add_argument('url', type=str, default="http://www.vesti.ru/")
parser.add_argument('--depth', type=int, default=2)
parser.add_argument('-n', type=int, default=2)
args = parser.parse_args()
current_url = args.url

storage = Storage()


if args.action == "load":
    def get_url(current_url, current_depth, root_url):
        try:
            request = urllib.request.urlopen(current_url, timeout=10)
            encoding = request.headers['content-type'].split('charset=')[-1]
            html = request.read().decode(encoding)
            title, hrefs = get_title_and_hrefs(html)
            current_depth += 1
            for href in hrefs:
                if current_depth < args.depth and href not in urls:
                    urls.append(href)
                    url_queue.put((href, current_depth, root_url))
            storage.insert(title=title, root=root_url,
                           current_url=current_url, html=html)
        except (AttributeError, LookupError,
                UnicodeDecodeError, urllib.error.URLError):
            pass

    def process_queue():
        while True:
            current_url, current_depth, root_url = url_queue.get()
            get_url(current_url, current_depth, root_url)
            url_queue.task_done()

    urls = [current_url]
    start = time.time()
    url_queue = Queue()
    get_url(current_url, 0, current_url)
    for url in range(30):
        t = threading.Thread(target=process_queue)
        t.daemon = True
        t.start()
    url_queue.join()
    print("Execution time = {0:.5f}".format(time.time() - start))

elif args.action == "get":
    cursor = storage.get(current_url, args.n)
    for res in cursor:
        print("{}: \"{}\"".format(res["url"], res["title"]))
