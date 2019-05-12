from bs4 import BeautifulSoup
import requests
import datetime

EVENTS_URLS = {
    'brown': 'https://apply.college.brown.edu/portal/brown-near-you?c=&country=',
    'columbia': 'https://apply.college.columbia.edu/portal/register?c=&country=',
    'princeton': 'https://apply.princeton.edu/portal/upcoming_events?c=&country=',
    'stanford': 'https://apply.stanford.edu/portal/stanfordinyourarea?c=&country=',
    'uchicago': 'https://prospects.uchicago.edu/register/?c=&country=',
    'yale': 'https://apps.admissions.yale.edu/portal/events?c=&country=',
    'upenn': 'https://key.admissions.upenn.edu/portal/penn-in-your-town?c=&country=',

    # 'harvard': 'https://college.harvard.edu/admissions/choosing-harvard/meet-us-your-hometown',
    # As of 5/12, Harvard's page only has ECO events. It's complicated to scrape.

    # 'dartmouth': '',
    # As of 5/12, the Dartmouth Visits You page has nothing

    # 'eee': 'http://exploringeducationalexcellence.org/events_only.php',
    # Got a 406, manually curl'd 5/12 entry

    'eco': 'http://www.exploringcollegeoptions.org/',
}

def now():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def download_page(page_name):
    r = requests.get(EVENTS_URLS[page_name])
    r.raise_for_status()

    with open(f'./documents/{page_name}/events_{now()}.html', 'wb') as f:
        f.write(r.content)

for page in EVENTS_URLS.keys():
    download_page(page)
