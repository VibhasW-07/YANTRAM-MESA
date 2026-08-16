import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

# Extract Meet Our Team Section
team_section_match = re.search(r'(<!-- 5\. Meet Our Team Section -->\n.*?)</section>\n\n        <!-- 6\. Sponsor Marquee -->', index_content, re.DOTALL)
team_section = team_section_match.group(1) + '</section>\n'

# Create team.html based on about.html
about_main_match = re.search(r'(<main>.*?</main>)', about_content, re.DOTALL)
team_main = '<main>\n' + team_section + '    </main>'

team_content = about_content.replace(about_main_match.group(1), team_main)

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(team_content)

# Remove Meet Our Team Section from index.html
index_content = index_content.replace(team_section_match.group(0), '<!-- 6. Sponsor Marquee -->')

# Update links in all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href="#hall-of-fame" with href="team.html"
    content = content.replace('href="#hall-of-fame"', 'href="team.html"')
    # Also if any has href="index.html#hall-of-fame"
    content = content.replace('href="index.html#hall-of-fame"', 'href="team.html"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
