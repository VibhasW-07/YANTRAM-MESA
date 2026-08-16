document.addEventListener('DOMContentLoaded', async () => {
    const swiperWrapper = document.getElementById('swiper-wrapper');
    const contentContainer = document.getElementById('team-content');
    
    if (!swiperWrapper || !contentContainer) return;

    try {
        const response = await fetch('data/legacy.json');
        if (!response.ok) throw new Error('Failed to load legacy data');
        const legacyData = await response.json();
        
        const years = Object.keys(legacyData).sort((a, b) => b.localeCompare(a)); // sort descending

        // Function to render a mini person card for the swiper slide
        const renderMiniCard = (person) => `
            <div class="flex flex-col items-center group">
                <div class="w-28 h-28 md:w-40 md:h-40 rounded-2xl overflow-hidden mb-4 border border-white/20 shadow-lg group-hover:border-arancio group-hover:-translate-y-2 transition-all duration-300">
                    <img src="${person.image}" alt="${person.name}" class="w-full h-full object-cover object-center scale-110 group-hover:scale-125 transition-all duration-500"
                         onerror="this.src='data:image/svg+xml;charset=UTF-8,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'200\\' height=\\'200\\' viewBox=\\'0 0 200 200\\'%3E%3Crect fill=\\'%23121212\\' width=\\'200\\' height=\\'200\\'/%3E%3Ctext fill=\\'%23555\\' font-family=\\'sans-serif\\' font-size=\\'12\\' font-weight=\\'bold\\' x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\'%3EIMAGE%3C/text%3E%3C/svg%3E';">
                </div>
                <h4 class="text-white font-space font-bold text-[11px] md:text-sm uppercase text-center group-hover:text-arancio transition-colors">${person.name}</h4>
                <p class="text-gray-400 font-inter text-[9px] md:text-xs uppercase text-center">${person.role}</p>
            </div>
        `;

        // Render Slides
        let slidesHtml = '';
        years.forEach((year) => {
            const data = legacyData[year];
            const coreHtml = data.core ? data.core.map(renderMiniCard).join('') : '';
            
            slidesHtml += `
                <div class="swiper-slide w-[320px] sm:w-[450px] md:w-[600px] h-[450px] md:h-[550px] bg-gradient-to-br from-charcoal to-nero rounded-3xl border border-white/20 p-8 flex flex-col items-center justify-center select-none shadow-[0_20px_50px_rgba(0,0,0,0.7)] relative overflow-hidden">
                    
                    <!-- Decorative Background Elements -->
                    <div class="absolute top-0 right-0 w-48 h-48 bg-arancio/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
                    <div class="absolute bottom-0 left-0 w-48 h-48 bg-white/5 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>
                    
                    <div class="z-10 text-center mb-8 md:mb-12">
                        <h3 class="text-4xl md:text-6xl font-michroma text-white mb-2 tracking-widest drop-shadow-lg">${year}</h3>
                        <div class="h-[2px] w-16 bg-arancio mx-auto mb-2"></div>
                        <p class="text-gray-400 font-space tracking-widest uppercase text-[10px] md:text-xs">Yearbook Collection</p>
                    </div>
                    
                    <div class="w-full flex justify-center gap-6 md:gap-12 z-10">
                        ${coreHtml}
                    </div>
                </div>
            `;
        });
        
        swiperWrapper.innerHTML = slidesHtml;

        // Custom CSS for Swiper cards effect ensuring proper container dimensions
        const style = document.createElement('style');
        style.innerHTML = `
            .swiper-slide { transition: border-color 0.3s; }
        `;
        document.head.appendChild(style);

        // Initialize Swiper with Cards Effect
        const swiper = new Swiper('.mySwiper', {
            effect: 'cards',
            grabCursor: true,
            cardsEffect: {
                slideShadows: true,
                perSlideOffset: 12, // Offset of the cards in the stack
                perSlideRotate: 4,  // Rotation of the cards
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });

        // Function to render expanded content (Department Heads)
        const renderExpandedContent = (year) => {
            const data = legacyData[year];
            if (!data || !data.departments || data.departments.length === 0) {
                contentContainer.classList.add('hidden');
                contentContainer.classList.remove('opacity-100');
                return;
            }

            const renderPersonCard = (person) => `
                <div class="w-36 md:w-40 lg:w-44 group border border-white/10 bg-charcoal p-4 md:p-6 flex flex-col items-center text-center transition-all duration-300 hover:border-arancio overflow-hidden relative rounded-xl">
                    <div class="w-20 h-20 md:w-24 md:h-24 rounded-xl overflow-hidden mb-4 border border-white/20">
                        <img src="${person.image}" alt="${person.name}" loading="lazy" class="w-full h-full object-cover object-center scale-110 group-hover:scale-125 transition-all duration-500" 
                             onerror="this.src='data:image/svg+xml;charset=UTF-8,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'200\\' height=\\'200\\' viewBox=\\'0 0 200 200\\'%3E%3Crect fill=\\'%23121212\\' width=\\'200\\' height=\\'200\\'/%3E%3Ctext fill=\\'%23555\\' font-family=\\'sans-serif\\' font-size=\\'12\\' font-weight=\\'bold\\' x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\'%3EIMAGE%3C/text%3E%3C/svg\\'%3E';">
                    </div>
                    <h4 class="text-xs md:text-sm font-space font-bold tracking-widest text-white uppercase mb-1 group-hover:text-arancio transition-colors leading-tight">${person.name}</h4>
                    <p class="text-[9px] md:text-[10px] font-inter tracking-widest text-gray-400 uppercase leading-tight">${person.role}</p>
                </div>
            `;

            let html = `
                <div class="border-t border-white/10 pt-4">
                    <h3 class="text-sm font-space text-gray-400 font-bold tracking-[0.2em] uppercase mb-8 border-l-2 border-gray-400 pl-4 inline-block">Department Heads (${year})</h3>
                    <div class="flex flex-col gap-4 md:gap-6 w-full">
            `;
            
            // Explicitly handle the 6-5-2 pattern if there are exactly 13 items
            if (data.departments.length === 13) {
                const row1 = data.departments.slice(0, 6);
                const row2 = data.departments.slice(6, 11);
                const row3 = data.departments.slice(11, 13);
                
                html += `<div class="flex flex-wrap justify-center gap-4 md:gap-6">${row1.map(renderPersonCard).join('')}</div>`;
                html += `<div class="flex flex-wrap justify-center gap-4 md:gap-6">${row2.map(renderPersonCard).join('')}</div>`;
                html += `<div class="flex flex-wrap justify-center gap-4 md:gap-6">${row3.map(renderPersonCard).join('')}</div>`;
            } else {
                html += `<div class="flex flex-wrap justify-center gap-4 md:gap-6">${data.departments.map(renderPersonCard).join('')}</div>`;
            }
            
            html += `
                    </div>
                </div>
            `;
            
            contentContainer.innerHTML = html;
            contentContainer.classList.remove('hidden');
            
            // Trigger fade in
            setTimeout(() => {
                contentContainer.classList.add('opacity-100');
                contentContainer.classList.remove('opacity-0');
            }, 50);
        };

        // Handle slide change to update expanded content
        swiper.on('slideChange', () => {
            const activeIndex = swiper.activeIndex;
            const activeYear = years[activeIndex];
            
            // Fade out current content
            contentContainer.classList.add('opacity-0');
            contentContainer.classList.remove('opacity-100');
            
            // Wait for fade out, then render new
            setTimeout(() => {
                renderExpandedContent(activeYear);
            }, 300);
        });

        // Initial render
        renderExpandedContent(years[0]);
        
    } catch (error) {
        console.error('Error in hall of fame:', error);
        contentContainer.innerHTML = `<p class="text-red-500 font-space uppercase tracking-widest text-center w-full">Error loading legacy data.</p>`;
        contentContainer.classList.remove('hidden', 'opacity-0');
    }
});
