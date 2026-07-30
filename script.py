import urllib.request
import os

url = 'https://raw.githubusercontent.com/punkpeye/awesome-mcp-servers/main/README.md'
print("Downloading MCP list from", url)
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

file_path = r'c:\Users\Girish Lade\OneDrive\Desktop\MCP-Directory\MCP Directory 2.md'

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('# All Available MCP Tools Directory\n\n')
    f.write('Here is a comprehensively curated and structured directory of all available Model Context Protocol (MCP) servers found on the internet.\n\n')
    
    start_idx = data.find('## Server Implementations')
    if start_idx != -1:
        f.write(data[start_idx:])
    else:
        f.write(data)

print("Successfully structured and saved all MCPs to", file_path)
