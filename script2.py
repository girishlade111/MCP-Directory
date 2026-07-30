import urllib.request
import os

urls_to_fetch = [
    ('wong2/awesome-mcp-servers', 'https://raw.githubusercontent.com/wong2/awesome-mcp-servers/main/README.md'),
    ('Official modelcontextprotocol/servers', 'https://raw.githubusercontent.com/modelcontextprotocol/servers/main/README.md'),
    ('appcypher/awesome-mcp-servers', 'https://raw.githubusercontent.com/appcypher/awesome-mcp-servers/main/README.md')
]

file_path = r'c:\Users\Girish Lade\OneDrive\Desktop\MCP-Directory\MCP Directory 2.md'

with open(file_path, 'a', encoding='utf-8') as f:
    for name, url in urls_to_fetch:
        print(f"Fetching from {name}...")
        try:
            response = urllib.request.urlopen(url)
            data = response.read().decode('utf-8')
            
            f.write(f'\n\n<br><br>\n\n# --- ADDED FROM: {name} ---\n\n')
            
            # For wong2, we skip header stuff and start from "## Categories" or something similar if exists, otherwise append all.
            # But just appending all is safest to make sure we don't miss anything.
            f.write(data)
            print(f"Successfully appended {name}")
        except Exception as e:
            print(f"Failed to fetch {name}: {e}")

print("Done adding more MCPs to the directory.")
