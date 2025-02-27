import pandas as pd
import os
import re

# Read the CSV file
df = pd.read_csv('Renewal Lease Data Document.csv')

# Read the template
with open('Renewal Letter Template.tex', 'r', encoding='utf-8') as file:
    template = file.read()

# Create output directory if it doesn't exist
output_dir = 'tmp'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Find all placeholders in the template
placeholders = re.findall(r'\{\[(.*?)\]\}', template)

# Process each row in the CSV
for index, row in df.iterrows():
    letter_content = template
    
    # Replace placeholders with actual values
    for placeholder in placeholders:
        if placeholder in df.columns:
            value = str(row[placeholder])
            
            # Handle excel formatting issues for money values
            value = re.sub(r'\s*\$\s*(\d+)\s*', r'\\$\1', value).strip()
            
            # Replace placeholder in the template
            letter_content = letter_content.replace(f'{{[{placeholder}]}}', value)

    # Construct filename based on 'Name' column, handling special characters
    filename = f"renewal_letter_{row['Name'].replace(' ', '_')}.tex"
    
    # Write the modified content to a new .tex file
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as output_file:
        output_file.write(letter_content)

print("Letters generated successfully.")
