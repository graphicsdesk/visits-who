**Where does Columbia Visits You visit?**

## Setup

1. Run `pipenv shell` to enter the virtual environment subshell
2. Run `jupyter notebook` to start the local notebook server

## Cron

You can use Linux's built-in task scheduler [Cron](http://man7.org/linux/man-pages/man8/crond.8.html) to schedule scrapings at a regular interval.

1. Run `crontab -e` to edit the instructions for `cron`.
2. To run Cron without starting a virtual environment, use the `python` executable in the bin directory of the `visits-who` virtual environment when running `scraper.py`. You can find this directory by running `pipenv shell` and copying the path to `bin` that pipenv prints.
3. [Write the Cron job](https://help.dreamhost.com/hc/en-us/articles/215767047-Creating-a-custom-Cron-Job). Mine, which runs at 10 AM every day, looks like this:
```
0 10 * * * cd ~/cs_projects/visits-who && ~/.local/share/virtualenvs/visits-who-cV-S4XRR/bin/python scraper.py
```

## TODOs

- [ ] Research peer programs to ECO/EEE, decide whether to include them in this analysis
- [ ] Sync documents to S3 from local machine
