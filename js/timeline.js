document.addEventListener('DOMContentLoaded', async () => {
    const tabsContainer = document.getElementById('timeline-tabs');
    const contentContainer = document.getElementById('timeline-content');
    
    if (!tabsContainer || !contentContainer) return;

    try {
        const response = await fetch('data/timeline.json?v=' + new Date().getTime());
        if (!response.ok) throw new Error('Failed to load timeline data');
        const timelineData = await response.json();
        
        let activeIndex = 0;

        const renderTabs = () => {
            tabsContainer.innerHTML = '';
            timelineData.forEach((item, index) => {
                const isActive = index === activeIndex;
                const btn = document.createElement('button');
                btn.className = `flex flex-col items-center min-w-[120px] md:w-1/5 group focus:outline-none shrink-0 ${isActive ? 'opacity-100' : 'opacity-50 hover:opacity-100'} transition-opacity duration-300`;
                
                btn.innerHTML = `
                    <span class="text-xs md:text-sm font-space font-bold tracking-widest uppercase mb-4 transition-colors ${isActive ? 'text-arancio' : 'text-gray-400 group-hover:text-white'}">${item.year}</span>
                    <div class="w-4 h-4 bg-nero border-2 z-10 transition-colors ${isActive ? 'border-arancio shadow-[0_0_10px_rgba(227,30,36,0.5)] scale-125' : 'border-gray-600 group-hover:border-white group-hover:scale-110'}"></div>
                `;
                
                btn.addEventListener('click', () => {
                    activeIndex = index;
                    renderTabs();
                    renderContent();
                });
                
                tabsContainer.appendChild(btn);
            });
        };

        const renderContent = () => {
            const data = timelineData[activeIndex];
            
            // Remove animation class to re-trigger it
            contentContainer.classList.remove('timeline-card');
            void contentContainer.offsetWidth; // Trigger reflow
            contentContainer.classList.add('timeline-card');
            
            // Generate metrics HTML dynamically
            let metricsHtml = '';
            if (data.metrics) {
                metricsHtml = '<div class="grid grid-cols-2 gap-6 mb-8 pt-6 border-t border-white/10">';
                for (const [key, value] of Object.entries(data.metrics)) {
                    metricsHtml += `
                        <div>
                            <p class="text-3xl font-space font-bold text-white mb-1">${value}</p>
                            <p class="text-xs font-space tracking-widest text-arancio uppercase">${key}</p>
                        </div>
                    `;
                }
                metricsHtml += '</div>';
            }

            contentContainer.innerHTML = `
                <div class="flex flex-col lg:flex-row gap-12 w-full h-full">
                    <div class="w-full lg:w-1/2 flex flex-col justify-center">
                        <span class="text-sm font-space text-gray-500 font-bold tracking-[0.2em] uppercase mb-4">Milestone - ${data.year}</span>
                        <h3 class="text-4xl md:text-5xl font-space font-bold tracking-widest uppercase mb-6 text-white">${data.title}</h3>
                        <p class="text-gray-400 text-lg leading-relaxed font-light mb-8">${data.description}</p>
                        ${metricsHtml}
                    </div>
                    <div class="w-full lg:w-1/2 h-[400px] lg:min-h-[500px] border border-white/10 relative overflow-hidden group flex items-center justify-center bg-black/30 rounded-md">
                        <img src="${data.image}" alt="${data.title}" class="w-full h-auto max-h-full object-contain group-hover:scale-105 transition-all duration-500 ease-out" onerror="this.src='data:image/svg+xml;charset=UTF-8,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'400\\' height=\\'300\\' viewBox=\\'0 0 400 300\\'%3E%3Crect fill=\\'%23121212\\' width=\\'400\\' height=\\'300\\'/%3E%3Ctext fill=\\'%23555\\' font-family=\\'sans-serif\\' font-size=\\'18\\' font-weight=\\'bold\\' x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\'%3EIMAGE PLACEHOLDER%3C/text%3E%3C/svg%3E';">
                        <div class="absolute inset-0 border-2 border-transparent group-hover:border-arancio transition-colors duration-500 pointer-events-none z-10"></div>
                    </div>
                </div>
            `;
        };

        renderTabs();
        renderContent();
        
    } catch (error) {
        console.error('Error in timeline:', error);
        contentContainer.innerHTML = `<p class="text-red-500 font-space uppercase tracking-widest text-center w-full">Error loading timeline data.</p>`;
    }
});
