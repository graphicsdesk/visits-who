from bs4 import BeautifulSoup
import datetime
import os
import requests

EVENTS_URLS = {
    'brown': 'https://apply.college.brown.edu/portal/brown-near-you?c=&country=',
    'columbia': 'https://apply.college.columbia.edu/portal/register?c=&country=',
    'mit': 'https://mitadmissions.org/visit/mit-visits-you/fall-travel',
    'princeton': 'https://apply.princeton.edu/portal/upcoming_events?c=&country=',
    'stanford': 'https://apply.stanford.edu/portal/stanfordinyourarea?c=&country=',
    'uchicago': 'https://prospects.uchicago.edu/register/?c=&country=',
    'upenn': 'https://key.admissions.upenn.edu/portal/penn-in-your-town?c=&country=',
    'yale': 'https://apps.admissions.yale.edu/portal/events?c=&country=',
    
    'eco': 'http://www.exploringcollegeoptions.org/',

    # 'cornell': 'https://admissions.cornell.edu/visit/cornell-your-hometown',
    # As of 7/7, Cornell's page only has EEE events. It's complicated to scrape.

    # 'harvard': 'https://college.harvard.edu/admissions/choosing-harvard/meet-us-your-hometown',
    # As of 5/12, Harvard's page only has ECO events. It's complicated to scrape.
    # 7/7: Harvard's page has no events.

    # 'dartmouth': '',
    # As of 7/7, the Dartmouth Visits You page has nothing

    # 'eee': 'http://exploringeducationalexcellence.org/events_only.php',
    # Got a 406, manually curl'd 5/12, 7/7 entries
}

def now(hours=True):
    f_string = '%Y-%m-%d'
    if hours:
        f_string += 'T%H:%M:%S'
    return datetime.datetime.now().strftime(f_string)

def download_page(page_name):
    r = requests.get(EVENTS_URLS[page_name])
    r.raise_for_status()

    with open(f'./documents/{page_name}/events_{now()}.html', 'wb') as f:
        f.write(r.content)

for page in EVENTS_URLS.keys():
    date = now(hours=False)
    if all(date not in fname for fname in os.listdir(f'./documents/{page}')):
        # Documents not yet scraped for today
        download_page(page)
