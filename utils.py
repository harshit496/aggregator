from urllib.parse import urlparse
from datetime import datetime

def url_parser(url):

    parts = urlparse(url)
    directories = parts.path.strip('/').split('/')
    queries = parts.query.strip('&').split('&')

    elements = {
        'scheme': parts.scheme,
        'netloc': parts.netloc,
        'path': parts.path,
        'params': parts.params,
        'query': parts.query,
        'fragment': parts.fragment,
        'directories': directories,
        'queries': queries,
    }

    return elements

def convert_to_datetime(date_time: str):
    date, time = date_time.split("T")
    # date = date.rstrip(date[-1])
    datetime_string = date+" "+time
    return datetime.fromisoformat(datetime_string)
