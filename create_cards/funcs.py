from PIL import Image
from consts import *
import os

def create_card(color, number, h_max_smol, h_max_big):
    
    color_out = Image.open(folder + color +'_smol.png')
    color_in = Image.open(folder + color +'_big.png')
    
    sym_tl = (out_margin, out_margin + out_h_txt)
    sym_tr = (card_w - out_margin - color_out.width, out_margin + out_h_txt)
    sym_bl = (out_margin, card_h - out_margin - out_h_txt - color_out.height)
    sym_br = (card_w - out_margin - color_out.width, card_h - out_margin - out_h_txt - color_out.height)

    # Calculate positions
    card_w_cen =int(card_w/2 - color_in.width/2)
    card_h_cen = int(card_h/2 - color_in.height/2)

    in_margin_h = int(card_h/2 - 200)
    in_margin_w = int(card_w/2 - 230)

    positions = get_positions(color_in)
    
    for number in cards:

        if color == 'clubs' and number == '7':
            temp_color_in = color_in
            temp_color_out = color_out
            color_out = Image.open(folder_resized + 'colors/clubs_rgb_smol.png')
            color_in = Image.open(folder_resized + 'colors/clubs_rgb_big.png')

        # Create a blank canvas for the card
        card = Image.new('RGB', (card_w, card_h), color=background)

        # Outside Symbols
        card.paste(color_out, AdjustYPos(color_out, sym_tl, h_max_smol), mask=color_out.split()[3])
        card.paste(color_out.transpose(Image.FLIP_LEFT_RIGHT), AdjustYPos(color_out, sym_tr, h_max_smol), mask=color_out.transpose(Image.FLIP_LEFT_RIGHT).split()[3])
        card.paste(color_out.rotate(180).transpose(Image.FLIP_LEFT_RIGHT), AdjustYPos(color_out, sym_bl, h_max_smol, True), mask=color_out.rotate(180).transpose(Image.FLIP_LEFT_RIGHT).split()[3])
        card.paste(color_out.rotate(180), AdjustYPos(color_out, sym_br, h_max_smol, True), mask=color_out.rotate(180).split()[3])        

        # Outside Text
        for pos in font_positions:
            txt=Image.new('RGB', (out_w, out_h_txt), color=background)
            txt_w = font.getlength(number)
            d = ImageDraw.Draw(txt)
            d.text((int(out_w / 2 - txt_w / 2), 0), number,  font=font, fill=foreground)
            if pos[1] > card_h_cen:
                w = txt.rotate(180)
            else:
                w = txt
            card.paste(w, pos)

        # Inside Symbols
        if number.isnumeric():
            for pos in positions[int(number) - 2]:
                if pos[1] > card_h_cen:
                    card.paste(color_in.rotate(180), AdjustYPos(color_in, pos, h_max_big, True), mask=color_in.rotate(180).split()[3])
                else:
                    card.paste(color_in, AdjustYPos(color_in, pos, h_max_big), mask=color_in.split()[3])
        
        elif number == 'A':
            color_ace = Image.open(folder_resized + 'colors/' + color + '_ace.png')
            card.paste(color_ace, (int(card_w/2 - color_ace.width/2), int(card_h/2 - color_ace.height/2)), mask=color_ace.split()[3])
        
        elif number == 'K':
            joker_img = Image.open(folder_resized + 'jokers/paling_r_joker.png')
            card.paste(joker_img, (int(card_w/2 - joker_img.width/2), int(card_h/2 - joker_img.height/2)), mask=joker_img.split()[3])
            crown_img = Image.open(folder_resized + 'hutschmuck/king_' + color + '_smol.png')
            card.paste(crown_img, (180, 530), mask=crown_img.split()[3])
        
        elif number == 'D':
            joker_img = Image.open(folder_resized + 'jokers/paling_g_joker.png')
            card.paste(joker_img, (int(card_w/2 - joker_img.width/2), int(card_h/2 - joker_img.height/2)), mask=joker_img.split()[3])
            crown_img = Image.open(folder_resized + 'hutschmuck/queen_schraeg_klein_smol.png')
            card.paste(crown_img, (180, 535), mask=crown_img.split()[3])
        
        elif number == 'B':
            joker_img = Image.open(folder_resized + 'jokers/paling_b_joker.png')
            card.paste(joker_img, (int(card_w/2 - joker_img.width/2), int(card_h/2 - joker_img.height/2)), mask=joker_img.split()[3])
            crown_img = Image.open(folder_resized + 'hutschmuck/bube_smol.png')
            card.paste(crown_img, (180, 525), mask=crown_img.split()[3])
        
        if color == 'clubs' and number == '7':
            color_in = temp_color_in
            color_out = temp_color_out

        # Save the final image as a file
        card.save(output + color + '_' + number + '.png')



def resize_images(colors, folder, subfolder='', width_scaled=True, dim=50, prefix='', suffix='', smol='smol'):
    max_dim = 0
    for c in colors:
        path = ''
        if len(prefix) > 0:
            path += prefix + '_'
        path += c
        if len(suffix) > 0:
            path += '_' + suffix
        if len(subfolder) > 0:
            path = subfolder + '/' + path
        path_big = folder + 'original/'+ path + '.png'
        path_small = folder_resized + path + '_' + smol + '.png'
        img = Image.open(path_big)
        
        if width_scaled:
            percent = (dim/float(img.size[0]))
            max_dim = max(max_dim, img.size[1]*percent)
        else:
            percent = (dim/float(img.size[1]))
            max_dim = max(max_dim, img.size[0]*percent)
        wsize = int((float(img.size[0])*float(percent)))
        hsize = int((float(img.size[1])*float(percent)))
        img = img.resize((wsize,hsize), Image.Resampling.LANCZOS)
        img.save(path_small)
    return max_dim

def get_positions(color):
    # Calculate positions
    card_w_cen =int(card_w/2 - color.width/2)
    card_h_cen = int(card_h/2 - color.height/2)

    in_margin_h = int(card_h/2 - 200)
    in_margin_w = int(card_w/2 - 230)
        
    pos_1 = (card_w_cen,                int(card_h_cen - 1 * in_margin_h))
    pos_2 = (card_w_cen,                int(card_h_cen + 1 * in_margin_h))
    pos_3 = (card_w_cen,                card_h_cen)
    pos_4 = (card_w_cen - in_margin_w,  int(card_h_cen - 1 * in_margin_h))
    pos_5 = (card_w_cen + in_margin_w,  int(card_h_cen - 1 * in_margin_h))
    pos_6 = (card_w_cen - in_margin_w,  int(card_h_cen + 1 * in_margin_h))
    pos_7 = (card_w_cen + in_margin_w,  int(card_h_cen + 1 * in_margin_h))
    pos_8 = (card_w_cen - in_margin_w,  card_h_cen)
    pos_9 = (card_w_cen + in_margin_w,  card_h_cen)
    pos_10 = (card_w_cen,               int(card_h_cen - 1/2 * in_margin_h))
    pos_11 = (card_w_cen,               int(card_h_cen + 1/2 * in_margin_h))
    pos_12 = (card_w_cen - in_margin_w, int(card_h_cen - 1/3 * in_margin_h))
    pos_13 = (card_w_cen + in_margin_w, int(card_h_cen - 1/3 * in_margin_h))
    pos_14 = (card_w_cen - in_margin_w, int(card_h_cen + 1/3 * in_margin_h))
    pos_15 = (card_w_cen + in_margin_w, int(card_h_cen + 1/3 * in_margin_h))
    pos_16 = (card_w_cen,               int(card_h_cen - 2/3 * in_margin_h))
    pos_17 = (card_w_cen,               int(card_h_cen + 2/3 * in_margin_h))

    positions = [
        [pos_1, pos_2], # 2
        [pos_1, pos_2, pos_3], #3
        [pos_4, pos_5, pos_6, pos_7], # 4
        [pos_3, pos_4, pos_5, pos_6, pos_7], # 5
        [pos_4, pos_5, pos_6, pos_7, pos_8, pos_9], # 6
        [pos_4, pos_5, pos_6, pos_7, pos_8, pos_9, pos_10], # 7
        [pos_4, pos_5, pos_6, pos_7, pos_8, pos_9, pos_10, pos_11], # 8
        [pos_3, pos_4, pos_5, pos_6, pos_7, pos_12, pos_13, pos_14, pos_15], # 9
        [pos_4, pos_5, pos_6, pos_7, pos_12, pos_13, pos_14, pos_15, pos_16, pos_17], # 10
    ]
    return positions

def AdjustYPos(img, pos, max_h, flip = False) -> int:
    if flip:
        return (pos[0], pos[1] - int((max_h - img.height) / 2))
    else:
        return (pos[0], pos[1] + int((max_h - img.height) / 2))
    
def create_joker(joker):
    joker_img = Image.open(folder + joker + '_joker.png').convert('RGBA')

    text = 'J\nO\nK\nE\nR'
    card = Image.new('RGB', (card_w, card_h), color=background)
    out_w_joker = font.getbbox(text)[3]
    out_h_joker = font.getbbox(text)[2]

    card_w_cen =int(card_w/2 - joker_img.width/2)
    card_h_cen = int(card_h/2 - joker_img.height/2)

    # Outside text
    for pos in [(out_margin + 15, out_margin), (card_w - out_margin - out_w_joker, card_h - out_margin  - out_h_joker)]:
        txt=Image.new('RGB', (out_w, out_h_joker), color=background)
        d = ImageDraw.Draw(txt)
        txt_w = font.getlength('J')
        d.text((int(out_w / 2 - txt_w / 2), 0), text,  font=font, fill=foreground)
        if pos[1] > card_h_cen:
            w = txt.rotate(180)
        else:
            w = txt
        card.paste(w, pos)

    # Inside symbol
    card.paste(joker_img, (int(card_w/2 - joker_img.width/2), int(card_h/2 - joker_img.height/2)), mask=joker_img.split()[3])

    card.save(output + 'joker_' + joker + '.png')

    
