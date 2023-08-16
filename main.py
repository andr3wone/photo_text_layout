from PIL import Image, ImageDraw, ImageFont
import random
import os

for root, dirs, files in os.walk("./photo"):
    for file in files:
        im = Image.open(f"./photo/{file}")
        n1 = ' '.join(file.split(" ")[0:-1])
        n2 = str(file.split(" ")[-1].strip(".JPG"))

        bg = Image.new('RGBA', (im.width, int(im.height/10)), (0, 0, 0, 150))
        im.paste(bg, (0, 0), bg)
        draw_text = ImageDraw.Draw(im)
        font = ImageFont.truetype('./arial.ttf', size=24)
        draw_text.multiline_text(
            (20, 10),
            f'{n1}\n{n2} {random.randint(10, 14)}:{random.randint(10, 59)}',
            font=font,
            fill=('#FFFFFF')
            )
        im.save(f"./out/{file.strip('.JPG')}.PNG")
