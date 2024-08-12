#!/bin/bash

# Check if feeds.txt exists
if [[ ! -f feeds.txt ]]; then
    echo "feeds.txt not found!"
    exit 1
fi

# Loop through each line in feeds.txt
while IFS= read -r feed_url
do
    # Extract the value after /feed/ as the filename
    filename=$(echo "$feed_url" | sed -n 's#.*/feed/\(.*\)#\1#p')

    # Special case for blog.victorgevers.com
    if [[ "$feed_url" == *"blog.victorgevers.com"* ]]; then
        filename="blog"
    fi

    # If filename extraction is successful, download the feed
    if [[ -n "$filename" ]]; then
        output_file="${filename}.xml"
        echo "Downloading $feed_url to $output_file"
        curl -s "$feed_url" -o "$output_file"
    else
        echo "Failed to extract filename from $feed_url"
    fi
done < feeds.txt

echo "Download complete!"
