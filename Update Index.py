import os

def generate_links():
    links = ""
    for item in os.listdir('.'):
        # Check if the item is a directory
        if os.path.isdir(item) and not item.startswith('.'): # Ignore hidden directories like .DS_Store
            # Attempt to find the first .html file in the directory
            for file in os.listdir(item):
                if file.endswith('.html'):
                    # Assuming the first .html file is the main file you want to link to
                    links += f'<li><a href="{item}/{file}">{item}</a></li>\n'
                    break # Stop looking once the first .html file is found
    return links

def update_index():
    html_content = f'''<html>
<head><title>Index</title></head>
<body>
    <h1>Index</h1>
    <ul>
    {generate_links()}
    </ul>
</body>
</html>'''
    with open('index.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    update_index()
