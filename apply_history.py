
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Generate the history timeline
timeline_html = """
        <!-- 3. Our History (About) Section -->
        <section id="about" class="w-full bg-nero py-24 border-t border-white/5 relative overflow-hidden">
            <div class="max-w-7xl mx-auto px-6 md:px-16">
                <h2 class="text-4xl md:text-5xl font-michroma font-normal text-white mb-20 tracking-wide text-center uppercase">
                    Our History
                </h2>
                <div class="relative w-full max-w-5xl mx-auto">
                    <!-- Mobile center line -->
                    <div class="absolute left-4 md:left-1/2 top-0 bottom-0 border-l-2 border-dashed border-gray-600 block md:hidden z-0"></div>
"""

for year in range(2016, 2026):
    is_left = (year % 2 == 0)
    line_class = "hidden md:block" if year != 2025 else "hidden"
    
    if is_left:
        timeline_html += f"""
                    <!-- {year}: Left -->
                    <div class="flex flex-col md:flex-row w-full relative group">
                        <!-- Connecting Line -->
                        <div class="absolute top-1/2 left-1/2 w-1/2 h-full border-t-2 border-r-2 border-dashed border-arancio {line_class}" style="border-top-right-radius: 20px; border-bottom-right-radius: 20px; transform: translateY(-2px); z-index: 0;"></div>
                        
                        <div class="w-full md:w-1/2 md:pr-16 relative z-10 py-8 pl-12 md:pl-0">
                            <!-- Mobile Dot -->
                            <div class="absolute top-1/2 left-4 w-4 h-4 rounded-full bg-arancio transform -translate-x-1/2 -translate-y-1/2 block md:hidden z-20 shadow-[0_0_10px_#E31E24]"></div>
                            
                            <!-- Desktop Dot -->
                            <div class="absolute top-1/2 right-0 w-4 h-4 rounded-full bg-arancio transform translate-x-1/2 -translate-y-1/2 hidden md:block z-20 shadow-[0_0_10px_#E31E24]"></div>

                            <div class="bg-charcoal border border-white/10 p-6 hover:border-arancio transition-colors shadow-lg">
                                <h3 class="text-3xl font-michroma text-arancio mb-4">{year}</h3>
                                <div class="w-full h-48 bg-black mb-4 flex items-center justify-center border border-white/5 overflow-hidden">
                                    <img src="https://placehold.co/600x400/121212/E31E24?text={year}" alt="{year}" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500">
                                </div>
                                <p class="text-gray-400 font-inter text-sm">Add your {year} content here...</p>
                            </div>
                        </div>
                        <div class="hidden md:block md:w-1/2"></div>
                    </div>
"""
    else:
        timeline_html += f"""
                    <!-- {year}: Right -->
                    <div class="flex flex-col md:flex-row w-full relative group">
                        <!-- Connecting Line -->
                        <div class="absolute top-1/2 right-1/2 w-1/2 h-full border-t-2 border-l-2 border-dashed border-arancio {line_class}" style="border-top-left-radius: 20px; border-bottom-left-radius: 20px; transform: translateY(-2px); z-index: 0;"></div>
                        
                        <div class="hidden md:block md:w-1/2"></div>
                        <div class="w-full md:w-1/2 md:pl-16 relative z-10 py-8 pl-12 md:pl-16">
                            <!-- Mobile Dot -->
                            <div class="absolute top-1/2 left-4 w-4 h-4 rounded-full bg-arancio transform -translate-x-1/2 -translate-y-1/2 block md:hidden z-20 shadow-[0_0_10px_#E31E24]"></div>

                            <!-- Desktop Dot -->
                            <div class="absolute top-1/2 left-0 w-4 h-4 rounded-full bg-arancio transform -translate-x-1/2 -translate-y-1/2 hidden md:block z-20 shadow-[0_0_10px_#E31E24]"></div>

                            <div class="bg-charcoal border border-white/10 p-6 hover:border-arancio transition-colors shadow-lg">
                                <h3 class="text-3xl font-michroma text-arancio mb-4">{year}</h3>
                                <div class="w-full h-48 bg-black mb-4 flex items-center justify-center border border-white/5 overflow-hidden">
                                    <img src="https://placehold.co/600x400/121212/E31E24?text={year}" alt="{year}" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500">
                                </div>
                                <p class="text-gray-400 font-inter text-sm">Add your {year} content here...</p>
                            </div>
                        </div>
                    </div>
"""

timeline_html += """
                </div>
            </div>
        </section>
"""

pattern = re.compile(r"<!-- 3\. Who We Are Section -->.*?<!-- 4\. Our Role Section -->", re.DOTALL)
new_html = pattern.sub(f"{timeline_html}\n        <!-- 4. Our Role Section -->", html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Updated index.html")

