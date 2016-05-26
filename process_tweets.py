#!/usr/bin/env python

# Ok, now we've got a big JSON file of tweets, let's find something about them.

import argparse, csv, collections, json
parser = argparse.ArgumentParser()
parser.add_argument('--infile', default='chi2016.json')
args = parser.parse_args()

tweets = json.load(open(args.infile))
print "total # of tweets: " + str(len(tweets))

for tweet in tweets:
    if tweet['place']:
        print tweet['place']['name'] + ' ' + tweet['text']
        # print tweet['text']

places = [t['place']['name'] for t in tweets if t['place']]
print "# of place tweets: " + str(len(places))
print "Places: " + str(collections.Counter(places))
coords = [t['coordinates']['coordinates'] for t in tweets if t['coordinates']]
print len(coords)
print coords
