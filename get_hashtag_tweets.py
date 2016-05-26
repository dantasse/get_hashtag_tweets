#!/usr/bin/env python

# Given a hashtag, get all the tweets, stuff them in a json.

import argparse, csv, collections, json, twython, ConfigParser
parser = argparse.ArgumentParser()
parser.add_argument('--config_file', default='config.txt')
parser.add_argument('--hashtag', default='chi2016')
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

results=twitter.search(q=args.hashtag)
