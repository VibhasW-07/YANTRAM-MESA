document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('button[aria-label="Toggle Menu"]');
    const nav = document.querySelector('nav');
    
    if (mobileMenuBtn && nav) {
        mobileMenuBtn.addEventListener('click', () => {
            nav.classList.toggle('hidden');
            nav.classList.toggle('absolute');
            nav.classList.toggle('top-20');
            nav.classList.toggle('left-0');
            nav.classList.toggle('w-full');
            nav.classList.toggle('bg-nero');
            nav.classList.toggle('flex');
            nav.classList.toggle('flex-col');
            nav.classList.toggle('z-[100]');
            nav.classList.toggle('p-6');
            nav.classList.toggle('border-b');
            nav.classList.toggle('border-white/10');
        });
    }

    // Sticky Navbar Styling on Scroll
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.remove('bg-transparent', 'border-transparent');
            navbar.classList.add('bg-nero/95', 'backdrop-blur-md', 'border-white/10', 'shadow-lg', 'shadow-arancio/5');
        } else {
            navbar.classList.remove('bg-nero/95', 'backdrop-blur-md', 'border-white/10', 'shadow-lg', 'shadow-arancio/5');
            navbar.classList.add('bg-transparent', 'border-transparent');
        }
    });

    // Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Close mobile menu if open
                if (!nav.classList.contains('hidden') && window.innerWidth < 768) {
                    mobileMenuBtn.click();
                }
                
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
