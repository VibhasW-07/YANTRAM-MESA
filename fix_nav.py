import os
import glob
import re

html_files = glob.glob('c:/mesaweb/*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Change nav container gap to be more responsive
    content = content.replace('<nav class="hidden md:flex gap-8 items-center">', '<nav class="hidden lg:flex gap-3 xl:gap-8 items-center">')
    # If the user is on md screen, the menu might still overflow, so hiding on md and showing on lg is safer for a very wide menu,
    # OR we can just use `hidden md:flex gap-3 lg:gap-6 xl:gap-8 items-center`
    content = content.replace('<nav class="hidden lg:flex gap-3 xl:gap-8 items-center">', '<nav class="hidden md:flex gap-3 lg:gap-6 xl:gap-8 items-center">')
    # Also handle if it's already modified
    content = re.sub(r'<nav class="hidden md:flex gap-8 items-center">', '<nav class="hidden md:flex gap-3 lg:gap-6 xl:gap-8 items-center">', content)

    # 2. Add whitespace-nowrap to all nav-link classes
    def add_nowrap(match):
        cls_content = match.group(1)
        if 'whitespace-nowrap' not in cls_content:
            cls_content += ' whitespace-nowrap'
        return f'class="{cls_content}"'
    
    content = re.sub(r'class="(nav-link[^"]*)"', add_nowrap, content)

    # 3. Fix the hard line breaks in text
    content = re.sub(r'>About\s+Us</a>', '>About Us</a>', content)
    content = re.sub(r'>Meet\s+Our Team</a>', '>Meet Our Team</a>', content)
    content = re.sub(r'>Contact\s+Us</a>', '>Contact Us</a>', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Fixed nav in {f}")

print("Done.")
