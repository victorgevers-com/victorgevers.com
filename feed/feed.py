import feedparser

# Parse the RSS feed from the XML file
feed = feedparser.parse('feed.xml')

# Create and open an HTML file to write the output
with open('feed.html', 'w', encoding='utf-8') as f:
    # Write the header of the HTML file
    f.write("<html><head><title>Victor Gevers RSS Feed</title></head><body>")
    f.write("<h1>Victor Gevers RSS Feed</h1>")
    
    # Loop through each entry (item) in the feed
    for entry in feed.entries:
        f.write(f"<div class='post'>")
        f.write(f"<h2><a href='{entry.link}'>{entry.title}</a></h2>")
        f.write(f"<p><em>Published on: {entry.published}</em></p>")
        f.write("</div><hr/>")
    
    # Write the footer of the HTML file
    f.write("</body></html>")

print("RSS feed has been parsed and saved to feed.html")

