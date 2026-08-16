document.addEventListener('DOMContentLoaded', async () => {
    const grid = document.getElementById('sponsors-grid');
    if (!grid) return;

    try {
        const response = await fetch('data/sponsors.json');
        if (!response.ok) throw new Error('Failed to load sponsors data');
        const sponsors = await response.json();

        let html = '';
        sponsors.forEach(sponsor => {
            html += `
                <div class="flex flex-col items-center justify-center bg-charcoal p-8 rounded-xl border border-white/5 hover:border-arancio transition-colors shadow-lg group">
                    <img src="${sponsor.logo}" alt="${sponsor.name}" class="h-20 md:h-24 w-auto object-contain mb-6 opacity-80 group-hover:opacity-100 transition-all group-hover:scale-105" 
                         onerror="this.src='data:image/svg+xml;charset=UTF-8,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'150\\' height=\\'60\\' viewBox=\\'0 0 150 60\\'%3E%3Crect fill=\\'transparent\\' width=\\'150\\' height=\\'60\\'/%3E%3Ctext fill=\\'%23ffffff\\' font-family=\\'sans-serif\\' font-size=\\'14\\' font-weight=\\'bold\\' x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' dominant-baseline=\\'middle\\'%3E${sponsor.name}%3C/text%3E%3C/svg%3E';">
                    <h3 class="text-white font-space tracking-widest text-xs md:text-sm uppercase text-center">${sponsor.name}</h3>
                </div>
            `;
        });
        grid.innerHTML = html;

    } catch (error) {
        console.error('Error in sponsors page:', error);
        grid.innerHTML = `<p class="text-gray-500 font-space tracking-widest col-span-full text-center">SPONSORS UNAVAILABLE</p>`;
    }
});
