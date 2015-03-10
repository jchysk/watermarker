"""watermark 

Make image out of text. Overlay onto image at low opacity. Also include date.
python watermark.py Image_to_watermark Name_to_watermark Output_image_file

"""

from PIL import Image, ImageFont, ImageDraw, ImageEnhance

FONT_SIZE = 16


def img_from_text(image, text, fileout="output.jpg"):
    im = Image.open(image)
    watermark = Image.new('RGBA', im.size, (0,0,0,0))
    draw = ImageDraw.Draw(watermark)
    font = ImageFont.truetype("FreeSans.ttf", FONT_SIZE)
    #font = ImageFont.truetype("sans-serif.ttf", 16)
    for x in range(0, im.size[0], len(text) * FONT_SIZE / 2):
        for y in range(0, im.size[1], FONT_SIZE):
            draw.text((x,y), text, font=font)
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(0.20)
    watermark.putalpha(alpha)
    Image.composite(watermark, im, watermark).save(fileout, 'JPEG')


def get_date():
    import datetime
    today = datetime.date.today().strftime("%Y-%m-%d")
    return today


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print "Not enough arguments"
    else:
        image = sys.argv[1]
        text = sys.argv[2] + " Date: " + get_date()
        fileout = "output.jpg"
        if len(sys.argv) >= 4:
            fileout = sys.argv[3]
        img = img_from_text(image, text, fileout)
