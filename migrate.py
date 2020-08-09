#!/usr/bin/env python

import configparser
import logging
from migrator import client
from migrator import helpers

# Read in configuration file for API stuff
config = configparser.ConfigParser()
config.read('config.ini')

# New simple help scout client
client = client.HelpScoutClient(config)

# Fetch clients list
sites = client.fetch_sites_list()
if sites is None or len(sites['items']) == 0:
    logging.error('There are no sites found, exiting')
    exit

# Present list of sites
sourceSiteId = None
targetSiteId = None

print("\n")
print('Please choose a SOURCE site from the list:\n')
print ("\n".join(helpers.render_sites_list(sites['items'])))

# Gather source site input
sourceSiteId = int(input('Enter choice [0-' + str(len(sites['items'])-1) + "]:\n"))
helpers.clear_screen()

print('Please choose a DESTINATION site from the list:\n')
print ("\n".join(helpers.render_sites_list(sites['items'])))

# Gather target site input
targetSiteId = int(input('Enter choice [0-' + str(len(sites['items'])-1) + "]:\n"))
helpers.clear_screen()

if sourceSiteId == targetSiteId:
    logging.error('The source site and target site cannot be the same, exiting')
    exit

# Validate source site has plenty of articles and collections
sourceCollections = client.fetch_site_collections(sites['items'][sourceSiteId]['id'])
print(sites['items'][sourceSiteId], sourceCollections)

# Validate target site has no articles and collections

