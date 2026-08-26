import os
import glob
import re

gallery_html = """
        <!-- 6. Gallery Section -->
        <section id="gallery" class="w-full py-20 px-6 md:px-12 lg:px-24 bg-nero relative z-0 border-t border-white/5">
            <div class="max-w-7xl mx-auto relative z-10">
                <div class="mb-12 text-center md:text-left">
                    <h2 class="text-4xl md:text-5xl font-michroma font-bold text-white tracking-wide uppercase drop-shadow-lg">
                        Gallery
                    </h2>
                    <p class="text-gray-400 font-inter mt-4 text-lg">Top-tier car models and event moments.</p>
                </div>
                
                <div class="gallery-grid">
                    <!-- Image 1 -->
                    <div class="gallery-item group">
                        <img src="https://images.unsplash.com/photo-1542282088-fe8426682b8f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Car Expo">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6 pointer-events-none">
                            <span class="text-white font-space font-bold tracking-widest text-sm uppercase">Car Expo</span>
                        </div>
                    </div>
                    <!-- Image 2 -->
                    <div class="gallery-item group">
                        <img src="https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Car Model 1">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6 pointer-events-none">
                            <span class="text-white font-space font-bold tracking-widest text-sm uppercase">Formula SAE</span>
                        </div>
                    </div>
                    <!-- Image 3 -->
                    <div class="gallery-item group sm:col-span-2 lg:col-span-1">
                        <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Tech Expo">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6 pointer-events-none">
                            <span class="text-white font-space font-bold tracking-widest text-sm uppercase">Auto Fest</span>
                        </div>
                    </div>
                    <!-- Image 4 -->
                    <div class="gallery-item group lg:col-span-2">
                        <img src="https://images.unsplash.com/photo-1503376762365-33ee163eb079?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Event Action">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6 pointer-events-none">
                            <span class="text-white font-space font-bold tracking-widest text-sm uppercase">Speed Dynamics</span>
                        </div>
                    </div>
                    <!-- Image 5 -->
                    <div class="gallery-item group">
                        <img src="https://images.unsplash.com/photo-1525609004556-c46dce31c4b3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Team Moment">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6 pointer-events-none">
                            <span class="text-white font-space font-bold tracking-widest text-sm uppercase">Track Day</span>
                        </div>
                    </div>
                    <!-- Image 6 -->
                    <div class="gallery-item group">
                        <img src="https://images.unsplash.com/photo-1583121274602-3e2820c69888?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Showcase">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6 pointer-events-none">
                            <span class="text-white font-space font-bold tracking-widest text-sm uppercase">Showcase</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

html_files = glob.glob('c:/mesaweb/*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if gallery already exists in nav
    if '>Gallery</a>' not in content:
        # We need to insert it right after the Events link
        # The events link looks like: <a href="events.html" ... >Events</a>
        # We will use regex to find it
        
        # Determine the link target based on file
        if os.path.basename(f) == 'events.html':
            gallery_href = '#gallery'
        else:
            gallery_href = 'events.html#gallery'
            
        gallery_link = f'\n                <a href="{gallery_href}"\n                    class="nav-link text-sm font-semibold tracking-widest hover:text-arancio transition-colors uppercase">Gallery</a>'
        
        # Replace 
        content = re.sub(r'(<a[^>]*>Events</a>)', r'\1' + gallery_link, content)
        
        # If it's events.html, append the gallery section before the footer
        if os.path.basename(f) == 'events.html':
            if 'id="gallery"' not in content:
                content = content.replace('<footer id="contact"', gallery_html + '\n    <footer id="contact"')
                
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")

print("Done.")
