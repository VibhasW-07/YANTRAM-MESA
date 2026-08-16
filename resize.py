import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace "h-10 md:h-16" with "h-14 md:h-20"
    # But only for the Bharati Logo tag
    # Let's match the Bharati logo img tag
    pattern = r'(<img src="assets/images/Bharati_logo_clg.png"[^>]*?class=")([^"]*)(")'
    
    def replacer(match):
        prefix = match.group(1)
        cls = match.group(2)
        suffix = match.group(3)
        # replace size
        cls = cls.replace('h-10', 'h-14')
        cls = cls.replace('md:h-16', 'md:h-20')
        return prefix + cls + suffix
        
    content = re.sub(pattern, replacer, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
