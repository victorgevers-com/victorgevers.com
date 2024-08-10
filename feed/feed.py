import feedparser
import re

# Function to remove all <img> tags from the content
def remove_images(content):
    return re.sub(r'<img[^>]*>', '', content)

# Function to truncate content to 200 characters after removing images
def truncate_content(content, limit=200):
    # First, remove all <img> tags
    content = remove_images(content)
    # Then truncate to the specified character limit
    if len(content) > limit:
        return content[:limit] + "..."
    return content

# Function to extract the first <img> tag from content
def extract_first_image(content):
    match = re.search(r'<img[^>]+>', content)
    if match:
        return match.group(0)
    return ""

# Parse the RSS feed from the XML file
feed = feedparser.parse('feed.xml')

# Create and open an HTML file to write the output
with open('feed.html', 'w', encoding='utf-8') as f:
    # Write the header of the HTML file with indentation
    f.write("<html>\n")
    f.write("  <head>\n")
    f.write("    <title>Victor Gevers RSS Feed</title>\n")
    f.write("  </head>\n")
    f.write("  <body>\n")
    f.write("    <h1>Victor Gevers RSS Feed</h1>\n")
    
    # Loop through each entry (item) in the feed
    for entry in feed.entries:
        f.write("    <div class='post'>\n")
        
        # Initialize a flag to track if the image has been added
        image_added = False
        
        # Extract and insert the first image if found
        if 'content' in entry:
            for content in entry.content:
                if not image_added:
                    first_image = extract_first_image(content.value)
                    if first_image:
                        f.write(f"      {first_image}\n")
                        image_added = True  # Set the flag to true after adding the image
        
        # Write the title as a link
        f.write(f"      <h2><a href='{entry.link}'>{entry.title}</a></h2>\n")
        
        # Write the truncated content
        if 'content' in entry:
            for content in entry.content:
                # Remove images and then truncate the content
                truncated_content = truncate_content(content.value)
                f.write(f"      <div class='content'>{truncated_content}</div>\n")
                break  # Only process the first content item after the image
        
        # Write categories as tags
        if 'tags' in entry:
            f.write("      <ul class='tags'>\n")
            for tag in entry.tags:
                f.write(f"        <li>{tag.term}</li>\n")
            f.write("      </ul>\n")
        
        f.write("    </div>\n")
        f.write("    <hr/>\n")
    
    # Write the footer of the HTML file with indentation
    f.write("  </body>\n")
    f.write("</html>\n")

print("RSS feed has been parsed and saved to feed.html")
