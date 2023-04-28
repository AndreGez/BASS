from PIL import Image, ImageFont, ImageDraw
from consts import *
import os
import glob

def place_image(canvas, img, pos, flipped=False, mirrored=False):
    if flipped:
        img = img.transpose(Image.ROTATE_180)
    if mirrored:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    canvas.paste(img, (pos[0] - img.width // 2, pos[1] - img.height // 2), mask=img.split()[3])

def cut_to_card_size(input_folder, output_folder, suffix):
    # for all files in input_folder
    # resize to width
    # save in output_folder
    for f in os.listdir('data/resized/' + output_folder):
        os.remove('data/resized/' + output_folder + f)
    for filename in os.listdir('data/original/' + input_folder):
        img = Image.open('data/original/' + input_folder + filename)
        if img.width > img.height:
            img = img.resize((card_w, int(img.height * card_w / img.width)), Image.ANTIALIAS)
        else:
            img = img.resize((int(img.width * card_h / img.height), card_h), Image.ANTIALIAS)
        img = img.crop((0, 0, card_w, card_h))
        img = img.convert('RGBA')
        img.save('data/resized/' + output_folder + filename.split('.')[0] + '_' + suffix + '.png')

def get_text_canvas(font_size, text, color, flipped=False, vertical=False):
    font_name = 'BOD_CB.TTF'
    font = ImageFont.truetype(font_name, font_size)
    canvas_w = font.getbbox(text)[2]
    canvas_h = font.getbbox(text)[3]
    if vertical:
        canvas_w, canvas_h = canvas_h, canvas_w
    canvas = Image.new('RGBA', (canvas_w, canvas_h), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(canvas)
    _, _, w, h = draw.textbbox((0, 0), text, font=font)
    draw.text((0, 0), text, fill=color, font=font)
    if flipped:
        canvas = canvas.transpose(Image.ROTATE_180)
    return canvas.crop((0, 0, w, h)), [canvas_w, canvas_h]

def create_canvas(w, h, color, helplines=helpline):
    img = Image.new('RGBA', (w, h), color=color)
    if helplines:
        draw = ImageDraw.Draw(img)
        # lines from outer_margin
        draw.line((outer_margin, outer_margin, outer_margin, h - outer_margin), fill='red', width=1)
        draw.line((outer_margin, outer_margin, w - outer_margin, outer_margin), fill='red', width=1)
        draw.line((w - outer_margin, outer_margin, w - outer_margin, h - outer_margin), fill='red', width=1)
        draw.line((outer_margin, h - outer_margin, w - outer_margin, h - outer_margin), fill='red', width=1)
        # lines from inner_margin + outer_margin
        sum_margins_w = inner_margin + outer_margin + sym_w_corner
        sum_margins_h = inner_margin + outer_margin
        draw.line((sum_margins_w, sum_margins_h, sum_margins_w, h - sum_margins_h), fill='red', width=1)
        draw.line((sum_margins_w, sum_margins_h, w - sum_margins_w, sum_margins_h), fill='red', width=1)
        draw.line((w - sum_margins_w, sum_margins_h, w - sum_margins_w, h - sum_margins_h), fill='red', width=1)
        draw.line((sum_margins_w, h - sum_margins_h, w - sum_margins_w, h - sum_margins_h), fill='red', width=1)

        sum_margins_w = outer_margin + sym_w_corner
        sum_margins_h = outer_margin
        draw.line((sum_margins_w, sum_margins_h, sum_margins_w, h - sum_margins_h), fill='red', width=1)
        draw.line((sum_margins_w, sum_margins_h, w - sum_margins_w, sum_margins_h), fill='red', width=1)
        draw.line((w - sum_margins_w, sum_margins_h, w - sum_margins_w, h - sum_margins_h), fill='red', width=1)
        draw.line((sum_margins_w, h - sum_margins_h, w - sum_margins_w, h - sum_margins_h), fill='red', width=1)
    return img

def resize_images(input_folder, output_folder, suffix, width):
    # for all files in input_folder
    # resize to width
    # save in output_folder
    max_height = 0
    for f in os.listdir('data/resized/' + output_folder):
        os.remove('data/resized/' + output_folder + f)
    for filename in os.listdir('data/original/' + input_folder):
        img = Image.open('data/original/' + input_folder + filename)
        percent = (width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(percent)))
        if hsize > max_height:
            max_height = hsize
        img = img.resize((width,hsize), Image.ANTIALIAS)
        img = img.convert('RGBA')
        
        img.save('data/resized/' + output_folder + filename.split('.')[0] + '_' + suffix + '.png')
    return max_height

if __name__ == '__main__':
    print("Ich laufe jetzt hund")
    canvas = create_canvas(600, 400, 'white')
    text_canvas, _ = get_text_canvas(70, 'J\nO\nK\nE\nR', 'black', vertical=True)
    text_canvas.save('test_text.png')
    place_image(canvas, text_canvas, [300, 200])
    canvas.save('test.png')
