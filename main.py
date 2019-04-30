from bs4 import BeautifulSoup
import requests
import datetime

ROOT_URL = 'https://apply.college.columbia.edu/portal/register'
EVENTS_URL = ROOT_URL + '?c=&country='

def now():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def download_page():
    r = requests.get(EVENTS_URL)
    r.raise_for_status()

    with open(f'./documents/events_{now()}.html', 'wb') as f:
        f.write(r.content)

def get_events():
    r = requests.get(EVENTS_URL)
    r.raise_for_status()

    events = []
    soup = BeautifulSoup(r.content, 'html.parser')
    region_lists = soup.find(id='content').div.find_all('ul')

    for region_list in region_lists:
        events = region_list.find_all('li')
        for event in events:
            url = ROOT_URL + event.a.get('href')
            print(url)

    return events

download_page()
