import glob
import re

html_files = glob.glob('c:/mesaweb/*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Decrease Bharati logo size and spacing
    content = content.replace(
        'class="h-20 md:h-28 w-auto object-contain opacity-90 hover:opacity-100 transition-opacity ml-4 md:ml-8 border-l border-white/20 pl-4 md:pl-8"',
        'class="h-12 md:h-16 w-auto object-contain opacity-90 hover:opacity-100 transition-opacity ml-3 md:ml-6 border-l border-white/20 pl-3 md:pl-6"'
    )
    # Just in case it was already partially modified or has extra spaces
    content = re.sub(
        r'class="h-20 md:h-28[^"]*"',
        'class="h-12 md:h-16 w-auto object-contain opacity-90 hover:opacity-100 transition-opacity ml-3 md:ml-6 border-l border-white/20 pl-3 md:pl-6"',
        content
    )
    
    # Decrease text size of nav links from text-sm to text-xs (and lg:text-sm)
    content = content.replace('class="nav-link text-sm', 'class="nav-link text-xs lg:text-sm')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Done adjusting nav sizing.")
