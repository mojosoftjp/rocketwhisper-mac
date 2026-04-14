#!/usr/bin/env python3
"""Regenerate hero/og image with v2.1.0."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
OUT = "/Volumes/MyData/Xcode/Projects/RocketWhisperMac/website/og-image.png"

# Background gradient (dark navy → slightly lighter)
img = Image.new("RGB", (W, H), (10, 14, 30))
draw = ImageDraw.Draw(img)

# Subtle vertical gradient
top = (15, 20, 45)
bot = (8, 12, 28)
for y in range(H):
    t = y / H
    r = int(top[0] * (1 - t) + bot[0] * t)
    g = int(top[1] * (1 - t) + bot[1] * t)
    b = int(top[2] * (1 - t) + bot[2] * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Blue circular icon background
icon_cx, icon_cy, icon_r = 200, H // 2, 110
draw.ellipse(
    [icon_cx - icon_r, icon_cy - icon_r, icon_cx + icon_r, icon_cy + icon_r],
    fill=(72, 122, 255),
)

# Waveform bars inside icon (5 bars)
bar_heights = [40, 80, 120, 80, 40]
bar_w = 14
bar_gap = 10
total_w = 5 * bar_w + 4 * bar_gap
start_x = icon_cx - total_w // 2
for i, h in enumerate(bar_heights):
    x = start_x + i * (bar_w + bar_gap)
    top_y = icon_cy - h // 2
    bot_y = icon_cy + h // 2
    draw.rounded_rectangle([x, top_y, x + bar_w, bot_y], radius=6, fill="white")

# Fonts
def load_font(size, bold=False):
    paths = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

font_title = load_font(96)
font_sub = load_font(38)
font_body = load_font(32)
font_accent = load_font(32)

text_x = 360

# "RocketWhisper" title
draw.text((text_x, 180), "RocketWhisper", fill="white", font=font_title)

# "for Mac  v2.1.0"
draw.text((text_x, 290), "for Mac  v2.1.0", fill=(170, 190, 255), font=font_sub)

# Feature bullets
draw.text((text_x, 370), "Apple Intelligence native", fill=(220, 225, 240), font=font_body)
draw.text((text_x, 415), "AI speech recognition", fill=(220, 225, 240), font=font_body)
draw.text((text_x, 470), "Fully offline, one-time purchase", fill=(120, 200, 255), font=font_accent)

img.save(OUT, "PNG", optimize=True)
print(f"Wrote {OUT}")
