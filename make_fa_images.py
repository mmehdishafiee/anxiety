#!/usr/bin/env python3
"""
Generate Persian-localized PNG sprites for the anxiety game.
Replaces English text with Persian text using PIL + arabic_reshaper + bidi.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(ROOT, "styles", "fonts")

# Load Vazirmatn at requested size
def font(size, bold=False):
    name = "Vazirmatn-Bold.woff2" if bold else "Vazirmatn-Regular.woff2"
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        # fallback
        path = os.path.join(FONT_DIR, "Vazirmatn-Regular.woff2")
    return ImageFont.truetype(path, size)

def fa(text):
    """Shape and bidi-reorder Persian text for rendering."""
    return get_display(arabic_reshaper.reshape(text))

def center_text(img, y, text, size, color="#fff", bold=False):
    """Draw centered Persian text at given y."""
    draw = ImageDraw.Draw(img)
    f = font(size, bold)
    t = fa(text)
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, y), t, font=f, fill=color)
    return img

# ── 1. intro_logo.png ─────────────────────────────────────────────────────────
def make_intro_logo():
    src = os.path.join(ROOT, "sprites", "intro", "intro_logo.png")
    img = Image.open(src).convert("RGBA")
    # Image is a sprite sheet; find the main panel with text.
    # We'll clear the text area and re-draw.
    # Original: logo area roughly center of a 720x405 or similar sprite.
    # Simpler: create a fresh transparent image and just overlay Persian title.
    # We keep original art and paint Persian text on top of English text region.
    # English "Adventures With Anxiety!" text occupies top ~15%.
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    # Cover old title text region with black bar (approx top 20%)
    bar_h = int(img.height * 0.22)
    draw.rectangle([(0,0), (img.width, bar_h)], fill=(0,0,0,255))
    # Draw Persian title centered
    title_f = font(44, bold=True)
    t = fa("ماجراهای اضطراب!")
    bbox = draw.textbbox((0,0), t, font=title_f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, bar_h//2 - (bbox[3]-bbox[1])//2), t,
              font=title_f, fill="#ff4040")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("intro_logo.png done")

# ── 2. fear_captions.png ─────────────────────────────────────────────────────
def make_fear_captions():
    src = os.path.join(ROOT, "sprites", "ui", "fear_captions.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    # Three captions in a row; cover each and re-draw Persian
    labels = ["آسیب", "تنهایی", "بدی"]
    col_w = img.width // 3
    for i, label in enumerate(labels):
        x = i * col_w
        draw.rectangle([(x, 0), (x+col_w, img.height)], fill=(0,0,0,180))
        t = fa(label)
        f = font(22, bold=True)
        bbox = draw.textbbox((0,0), t, font=f)
        w = bbox[2]-bbox[0]
        draw.text((x + col_w/2 - w/2, img.height/2 - (bbox[3]-bbox[1])//2), t,
                  font=f, fill="#fff")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("fear_captions.png done")

# ── 3. youwin.png ─────────────────────────────────────────────────────────────
def make_youwin():
    src = os.path.join(ROOT, "sprites", "intermission", "youwin.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.35)
    draw.rectangle([(0, img.height//2 - bar_h//2), (img.width, img.height//2 + bar_h//2)],
                   fill=(0,0,0,220))
    f = font(40, bold=True)
    t = fa("برنده شدی!")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#fff")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("youwin.png done")

# ── 4. starring.png ───────────────────────────────────────────────────────────
def make_starring():
    src = os.path.join(ROOT, "sprites", "credits", "starring.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.30)
    draw.rectangle([(0, img.height//2 - bar_h//2), (img.width, img.height//2 + bar_h//2)],
                   fill=(0,0,0,220))
    f = font(36, bold=True)
    t = fa("با بازیِ")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#fff")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("starring.png done")

# ── 5. thanks.png ─────────────────────────────────────────────────────────────
def make_thanks():
    src = os.path.join(ROOT, "sprites", "credits", "thanks.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.30)
    draw.rectangle([(0, img.height//2 - bar_h//2), (img.width, img.height//2 + bar_h//2)],
                   fill=(0,0,0,220))
    f = font(36, bold=True)
    t = fa("تشکر از بازی!")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#ff4040")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("thanks.png done")

# ── 6. end_message.png ────────────────────────────────────────────────────────
def make_end_message():
    src = os.path.join(ROOT, "sprites", "credits", "end_message.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.40)
    draw.rectangle([(0, img.height//2 - bar_h//2), (img.width, img.height//2 + bar_h//2)],
                   fill=(0,0,0,220))
    f = font(30, bold=True)
    t = fa("پایان")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#fff")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("end_message.png done")

# ── 7. preloader.png ─────────────────────────────────────────────────────────
def make_preloader():
    src = os.path.join(ROOT, "sprites", "ui", "preloader.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.25)
    draw.rectangle([(0, img.height - bar_h), (img.width, img.height)], fill=(0,0,0,220))
    f = font(28, bold=True)
    t = fa("در حال بارگذاری...")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height - bar_h//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#fff")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("preloader.png done")

# ── 8. cc0.png ────────────────────────────────────────────────────────────────
def make_cc0():
    src = os.path.join(ROOT, "sprites", "about", "cc0.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.40)
    draw.rectangle([(0, img.height - bar_h), (img.width, img.height)], fill=(0,0,0,220))
    f = font(20, bold=True)
    t = fa("مالکیت عمومی (CC0)")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height - bar_h//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#aaa")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("cc0.png done")

# ── 9. replay.png ─────────────────────────────────────────────────────────────
def make_replay():
    src = os.path.join(ROOT, "sprites", "about", "replay.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.30)
    draw.rectangle([(0, 0), (img.width, bar_h)], fill=(0,0,0,220))
    f = font(24, bold=True)
    t = fa("بازپخش")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, bar_h//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#fff")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("replay.png done")

# ── 10. callback.png ──────────────────────────────────────────────────────────
def make_callback():
    src = os.path.join(ROOT, "sprites", "act4", "callback.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.28)
    draw.rectangle([(0, img.height - bar_h), (img.width, img.height)], fill=(0,0,0,220))
    f = font(24, bold=True)
    t = fa("فراخوان قبلی")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height - bar_h//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#ff4040")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("callback.png done")

# ── 11. screens.png ───────────────────────────────────────────────────────────
def make_screens():
    src = os.path.join(ROOT, "sprites", "credits", "screens.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.30)
    draw.rectangle([(0, img.height//2 - bar_h//2), (img.width, img.height//2 + bar_h//2)],
                   fill=(0,0,0,220))
    f = font(32, bold=True)
    t = fa("تیتراج پایانی")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#fff")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("screens.png done")

# ── 12. thumb.png ─────────────────────────────────────────────────────────────
def make_thumb():
    src = os.path.join(ROOT, "sharing", "thumb.png")
    img = Image.open(src).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    bar_h = int(img.height * 0.25)
    draw.rectangle([(0, img.height - bar_h), (img.width, img.height)], fill=(0,0,0,200))
    f = font(60, bold=True)
    t = fa("ماجراهای اضطراب!")
    bbox = draw.textbbox((0,0), t, font=f)
    w = bbox[2]-bbox[0]
    draw.text((img.width/2 - w/2, img.height - bar_h//2 - (bbox[3]-bbox[1])//2), t,
              font=f, fill="#ff4040")
    out = Image.alpha_composite(img, overlay)
    out.save(src)
    print("thumb.png done")

if __name__ == "__main__":
    try:
        make_intro_logo()
        make_fear_captions()
        make_youwin()
        make_starring()
        make_thanks()
        make_end_message()
        make_preloader()
        make_cc0()
        make_replay()
        make_callback()
        make_screens()
        make_thumb()
        print("\nAll images generated.")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise
