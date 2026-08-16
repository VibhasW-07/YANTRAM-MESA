
html = ""
for year in range(2016, 2026):
    is_left = (year % 2 == 0) # 2016 is left, 2017 is right
    
    if is_left:
        html += f"""
                    <!-- {year}: Left -->
                    <div class="flex flex-row w-full relative group">
                        <!-- Connecting Line -->
                        <div class="absolute top-1/2 left-1/2 w-1/2 h-full border-t-2 border-r-2 border-dashed border-arancio hidden md:block" style="border-top-right-radius: 20px; border-bottom-right-radius: 20px; transform: translateY(-2px);"></div>
                        
                        <div class="w-full md:w-1/2 md:pr-16 relative z-10 py-8">
                            <div class="bg-charcoal border border-white/10 p-6 hover:border-arancio transition-colors">
                                <h3 class="text-3xl font-michroma text-arancio mb-4">{year}</h3>
                                <div class="w-full h-48 bg-black mb-4 flex items-center justify-center border border-white/5 overflow-hidden">
                                    <img src="https://placehold.co/600x400/121212/E31E24?text={year}" alt="{year}" class="w-full h-full object-cover custom-grayscale">
                                </div>
                                <p class="text-gray-400 font-inter text-sm">Add your {year} content here...</p>
                            </div>
                            <!-- Dot -->
                            <div class="absolute top-1/2 right-0 w-4 h-4 rounded-full bg-arancio transform translate-x-1/2 -translate-y-1/2 hidden md:block shadow-[0_0_10px_#E31E24]"></div>
                        </div>
                        <div class="hidden md:block md:w-1/2"></div>
                    </div>
"""
    else:
        html += f"""
                    <!-- {year}: Right -->
                    <div class="flex flex-row w-full relative group">
                        <!-- Connecting Line -->
                        <div class="absolute top-1/2 right-1/2 w-1/2 h-full border-t-2 border-l-2 border-dashed border-arancio hidden md:block" style="border-top-left-radius: 20px; border-bottom-left-radius: 20px; transform: translateY(-2px);"></div>
                        
                        <div class="hidden md:block md:w-1/2"></div>
                        <div class="w-full md:w-1/2 md:pl-16 relative z-10 py-8">
                            <div class="bg-charcoal border border-white/10 p-6 hover:border-arancio transition-colors">
                                <h3 class="text-3xl font-michroma text-arancio mb-4">{year}</h3>
                                <div class="w-full h-48 bg-black mb-4 flex items-center justify-center border border-white/5 overflow-hidden">
                                    <img src="https://placehold.co/600x400/121212/E31E24?text={year}" alt="{year}" class="w-full h-full object-cover custom-grayscale">
                                </div>
                                <p class="text-gray-400 font-inter text-sm">Add your {year} content here...</p>
                            </div>
                            <!-- Dot -->
                            <div class="absolute top-1/2 left-0 w-4 h-4 rounded-full bg-arancio transform -translate-x-1/2 -translate-y-1/2 hidden md:block shadow-[0_0_10px_#E31E24]"></div>
                        </div>
                    </div>
"""

print(html)

