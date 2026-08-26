import os

css_content = """
/* Gallery Styles */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  padding-top: 2rem;
}

.gallery-item {
  position: relative;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  background-color: var(--color-charcoal);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.gallery-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(227, 30, 36, 0.3);
  border-color: var(--color-arancio);
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease-out;
  /* Starting filter can be standard custom-grayscale if desired, but we override here for specificity */
  filter: grayscale(80%) contrast(110%);
}

.gallery-item:hover img {
  transform: scale(1.1);
  filter: grayscale(0%) contrast(100%);
}
"""

css_file = 'c:/mesaweb/css/style.css'
with open(css_file, 'a', encoding='utf-8') as f:
    f.write(css_content)

print("CSS appended to style.css")
