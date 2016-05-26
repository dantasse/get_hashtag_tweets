#!/usr/bin/env python

# Given a hashtag, get all the tweets, stuff them in a json.

import argparse, csv, collections, json, twython, ConfigParser, time
parser = argparse.ArgumentParser()
parser.add_argument('--config_file', default='config.txt')
parser.add_argument('--hashtag', default='chi2016')
parser.add_argument('--outfile')
args = parser.parse_args()

config = ConfigParser.ConfigParser()
config.read(args.config_file)

# Man, I thought the runaround was easier than this.
twitter = twython.Twython(config.get('twitter', 'app_key'), 
        config.get('twitter', 'app_secret'),
        oauth_version=2)
ACCESS_TOKEN=twitter.obtain_access_token()

twitter = twython.Twython(config.get('twitter', 'app_key'),
        access_token=ACCESS_TOKEN, oauth_version=2)

if not args.hashtag.startswith('#'):
    args.hashtag = '#' + args.hashtag

statuses = []
max_id = None
for i in range(10): # retrieve max 10 * 100 tweets
    if not max_id:
        results=twitter.search(q=args.hashtag, count=100)
    else:
        results=twitter.search(q=args.hashtag, count=100, max_id=max_id)
    statuses += results['statuses']
    if len(results['statuses']) == 0:
        break
    else:
        max_id = min(r['id'] for r in results['statuses']) - 1
        print len(statuses)
    time.sleep(1)

if not args.outfile:
    args.outfile = args.hashtag.strip('#') + '.json'
json.dump(statuses, open(args.outfile, 'w'), indent=2)
