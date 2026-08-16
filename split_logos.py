import cv2
import numpy as np

img = cv2.imread('assets/images/sponsors/sponsor_5.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Invert or threshold
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get bounding boxes and filter small noise
boxes = []
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if w > 40 and h > 40:
        boxes.append((x, y, w, h))

# Merge overlapping or close boxes
def merge_boxes(boxes, x_thresh=20, y_thresh=20):
    if not boxes: return []
    merged = []
    for box in boxes:
        x, y, w, h = box
        added = False
        for i, mbox in enumerate(merged):
            mx, my, mw, mh = mbox
            # check intersection or closeness
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

merged_boxes = merge_boxes(boxes, 30, 30)
# run again to ensure complete merge
merged_boxes = merge_boxes(merged_boxes, 30, 30)

print(f"Found {len(merged_boxes)} logos")
for i, (x, y, w, h) in enumerate(merged_boxes):
    print(f"Box {i}: x={x}, y={y}, w={w}, h={h}")

# We expect 3 logos.
# Let's sort them.
# The one with the highest Y (lowest on screen) is Dhaaga.
# The other two are top. Left is AIIITS, Right is IMFS.
if len(merged_boxes) >= 3:
    merged_boxes.sort(key=lambda b: b[1]) # Sort by Y
    top_two = merged_boxes[:2]
    bottom_one = merged_boxes[-1]
    
    top_two.sort(key=lambda b: b[0]) # Sort top two by X
    aiiits = top_two[0]
    imfs = top_two[1]
    dhaaga = bottom_one
    
    def crop_and_save(box, filename):
        x, y, w, h = box
        # add padding
        px = max(0, x - 10)
        py = max(0, y - 10)
        pw = min(img.shape[1] - px, w + 20)
        ph = min(img.shape[0] - py, h + 20)
        cropped = img[py:py+ph, px:px+pw]
        cv2.imwrite(f'assets/images/sponsors/{filename}', cropped)
        print(f"Saved {filename}")

    crop_and_save(aiiits, 'sponsor_aiiits.png')
    crop_and_save(imfs, 'sponsor_imfs.png')
    crop_and_save(dhaaga, 'sponsor_dhaaga.png')
else:
    print("Could not cleanly separate 3 logos. Please check manually.")
