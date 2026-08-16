document.addEventListener('DOMContentLoaded', async () => {
    const track = document.getElementById('marquee-track');
    if (!track) return;

    try {
        const response = await fetch('data/sponsors.json');
        if (!response.ok) throw new Error('Failed to load sponsors data');
        const sponsors = await response.json();

        // Render sponsor items
        const renderSponsors = () => {
            let html = '';
            sponsors.forEach(sponsor => {
                html += `
                    <div class="flex-shrink-0 transition-all duration-300">
                        <img src="${sponsor.logo}" alt="${sponsor.name}" class="h-16 md:h-20 w-auto object-contain sponsor-logo" 
                             onerror="this.src='data:image/svg+xml;charset=UTF-8,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'150\\' height=\\'60\\' viewBox=\\'0 0 150 60\\'%3E%3Crect fill=\\'transparent\\' width=\\'150\\' height=\\'60\\'/%3E%3Ctext fill=\\'%23ffffff\\' font-family=\\'sans-serif\\' font-size=\\'20\\' font-weight=\\'bold\\' x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' dominant-baseline=\\'middle\\'%3E${sponsor.name}%3C/text%3E%3C/svg%3E';">
                    </div>
                `;
            });
            return html;
        };

        // Populate track multiple times to ensure seamless infinite scroll
        // The CSS animation scrolls exactly half the width
        const sponsorHtml = renderSponsors();
        track.innerHTML = sponsorHtml + sponsorHtml + sponsorHtml + sponsorHtml;

    } catch (error) {
        console.error('Error in marquee:', error);
        track.innerHTML = `<p class="text-gray-500 font-space tracking-widest">SPONSOR LOGOS UNAVAILABLE</p>`;
    }
});
