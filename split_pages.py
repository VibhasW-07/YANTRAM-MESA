
import re
import shutil

# 1. Read current index.html (which contains the zigzag timeline)
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 2. Extract the timeline section
timeline_match = re.search(r"(<!-- 3\. Our History \(About\) Section -->.*?)(<!-- 4\. Our Role Section -->)", html, re.DOTALL)
timeline_html = timeline_match.group(1).strip() if timeline_match else ""

# 3. Build about.html
# We want to keep the <head>, <header>, the timeline, and the <footer>
# Let us replace the entire <main>...</main> with just <main> timeline_html </main>
main_pattern = re.compile(r"<main>.*?</main>", re.DOTALL)
about_html = main_pattern.sub(f"<main>\n{timeline_html}\n    </main>", html)

# Fix header link in about.html and index.html
# Home link should point to index.html
about_html = about_html.replace("href=\"#hero\"", "href=\"index.html\"")
about_html = about_html.replace("href=\"#about\"", "href=\"#\"") # already on about

# In about.html, timeline is at top, so add padding so header does not overlap
about_html = about_html.replace("class=\"w-full bg-nero py-24", "class=\"w-full bg-nero pt-40 pb-24 min-h-screen")

with open("about.html", "w", encoding="utf-8") as f:
    f.write(about_html)


# 4. Restore index.html
original_who_are_we = """
        <!-- 3. Who We Are Section -->
        <section id="about" class="w-full flex flex-col lg:flex-row min-h-[700px] border-t border-white/5">
            <!-- Left Side Image -->
            <div class="w-full lg:w-1/2 relative min-h-[400px] lg:min-h-full">
                <img src="assets/images/whoweare.JPG" alt="Who We Are"
                    class="absolute inset-0 w-full h-full object-cover">
            </div>

            <!-- Right Side Content -->
            <div class="w-full lg:w-1/2 flex items-center bg-nero">
                <div class="p-10 md:p-16 lg:p-24 max-w-2xl">
                    <h2 class="text-4xl md:text-5xl font-michroma font-normal text-white mb-8 tracking-wide">
                        Who are We?
                    </h2>

                    <div
                        class="space-y-6 text-gray-300 font-inter font-light leading-relaxed text-base md:text-lg mb-12">
                        <p>
                            Mechanical Engineering Students Association (MESA) of Bharati Vidyapeeth College of
                            Engineering, Navi Mumbai organizes one of the Biggest AutoExpo event in Mumbai and MMR.
                        </p>
                        <p>
                            AutoExpo is an annual event where automobile enthusiasts from all over Maharashtra gather in
                            our college to showcase their Highly Performanced and visual tuned cars, Super-bikes above
                            600cc, Modified and Customized Prototypes.
                        </p>
                        <p>
                            In AutoExpo riders show-off their riding and driving skills by doing stunts like
                            Powerdrifting, Wheelie, Stoppie, Burnouts, etc.
                        </p>
                        <p>
                            Every year More than 400 bikers and 80+ cars participate in our event. Every year we
                            successfully bring-in a footfall of 3000+ of college students and every year the crowd keep
                            on increasing.
                        </p>
                    </div>

                    <a href="#sponsors" class="inline-flex items-center group transition-colors">
                        <div
                            class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center border border-white/10 group-hover:bg-white/10 group-hover:border-arancio transition-all mr-4">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="h-4 w-4 text-white group-hover:text-arancio transition-colors" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M9 5l7 7-7 7" />
                            </svg>
                        </div>
                        <span
                            class="text-white font-space font-bold tracking-widest text-xs uppercase group-hover:text-arancio transition-colors">
                            About Us
                        </span>
                    </a>
                </div>
            </div>
        </section>
"""

# Restore the original Who We Are section
new_index_html = html.replace(timeline_html, original_who_are_we)

# Update nav link in index.html to point to about.html
# Current: <a href="#about"\n                    class="nav-link text-sm font-semibold tracking-widest hover:text-arancio transition-colors uppercase">About\n                    Us</a>
new_index_html = new_index_html.replace("href=\"#about\"\n                    class=\"nav-link text-sm font-semibold tracking-widest hover:text-arancio transition-colors uppercase\">About\n                    Us</a>", 
"href=\"about.html\"\n                    class=\"nav-link text-sm font-semibold tracking-widest hover:text-arancio transition-colors uppercase\">About\n                    Us</a>")

# There is also the "Explore Auto Expo" button linking to #about on the hero page.
# Leave it as #about since it will now scroll to the Who We Are section, which is good.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_index_html)

print("Split complete!")

