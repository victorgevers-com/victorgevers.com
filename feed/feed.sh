#!/bin/bash

# Download the RSS feed
curl -s https://medium.com/feed/@victor_gevers -o feed.xml

# Start the HTML file
echo "<html><head><title>RSS Feed</title></head><body><h1>RSS Feed from Victor Gevers</h1><ul>" > feed.html

# Use python to generate the feed.xml
python feed.py

# Clean up
rm feed.xml

echo "RSS feed has been parsed and saved to feed.html"
