import os
import re

def replace_front_matter(file_path, year, nav_order):
    front_matter = f"""---
layout: default
parent: {year}
nav_order: {nav_order}
---

"""

    # Read the current content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Check if the front matter is already present
    if content.startswith('---'):
        # Remove existing front matter by finding the second '---'
        content = content[content.find('---', 2) + 3:]

    # Write the new front matter and the existing content back to the file
    with open(file_path, 'w') as file:
        file.write(front_matter + content)

# Path to the directory containing the markdown files
directory_path = 'summaries'

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.md'):
        # Extract the date using a regular expression
        match = re.search(r'(\d{2})-(\d{2})-(\d{4})', filename)
        if match:
            month = int(match.group(1))
            day = int(match.group(2))
            year = match.group(3)
            
            # Calculate the approximate day of the year inverted
            inverted_day = 400 - (month * 31 + day)
            
            file_path = os.path.join(directory_path, filename)
            replace_front_matter(file_path, year, inverted_day)
