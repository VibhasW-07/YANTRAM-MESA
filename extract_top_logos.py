import cv2

img = cv2.imread('assets/images/sponsors_grid.jpeg')
# Crop the top portion of the image to isolate the top row (e.g. top 300 pixels)
# Wait, let's crop just below the 'PREVIOUS SPONSORS' banner.
# The banner might be around y=0 to y=150.
# Let's crop y=150 to y=350
top_crop = img[150:350, :]
cv2.imwrite('assets/images/sponsors/top_crop_debug.png', top_crop)

gray = cv2.cvtColor(top_crop, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

boxes = []
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if w > 40 and h > 40:
        boxes.append((x, y, w, h))

def merge_boxes(boxes, x_thresh=30, y_thresh=30):
    if not boxes: return []
    merged = []
    for box in boxes:
        x, y, w, h = box
        added = False
        for i, mbox in enumerate(merged):
            mx, my, mw, mh = mbox
            if not (x > mx + mw + x_thresh or x + w < mx - x_thresh or y > my + mh + y_thresh or y + h < my - y_thresh):
                nx = min(x, mx)
                ny = min(y, my)
                nw = max(x+w, mx+mw) - nx
                nh = max(y+h, my+mh) - ny
                merged[i] = (nx, ny, nw, nh)
                added = True
                break
        if not added:
            merged.append(box)
    return merged

merged_boxes = merge_boxes(boxes, 40, 40)
merged_boxes = merge_boxes(merged_boxes, 40, 40)

# Sort by X
merged_boxes.sort(key=lambda b: b[0])

print(f"Found {len(merged_boxes)} logos in top row")
for i, (x, y, w, h) in enumerate(merged_boxes):
    print(f"Box {i}: x={x}, y={y}, w={w}, h={h}")
    # add padding
    px = max(0, x - 15)
    py = max(0, y - 15)
    pw = min(top_crop.shape[1] - px, w + 30)
    ph = min(top_crop.shape[0] - py, h + 30)
    cropped = top_crop[py:py+ph, px:px+pw]
    if i == 0:
        cv2.imwrite('assets/images/sponsors/sponsor_monster.png', cropped)
    elif i == 1:
        cv2.imwrite('assets/images/sponsors/sponsor_vivo.png', cropped)
    elif i == 2:
        cv2.imwrite('assets/images/sponsors/sponsor_oppo.png', cropped)
