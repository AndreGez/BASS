from PIL import Image, ImageDraw, ImageFont, ImageOps

out_margin = 50
card_h = 1146 #900
card_w = 769 #600

inverse = False
colors = ['bass', 'diamond', 'spades', 'heart', 'clubs']
jokers = ['scooter', 'HBz', 'The Holy Santa Barbara', 'Rammstein', 'paling', 'BMTH', 'paling_r', 'paling_g', 'paling_b']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'B', 'D', 'K', 'A']
font_str = 'BOD_CB.TTF'
font = ImageFont.truetype(font_str, 70)
font_big = ImageFont.truetype(font_str, 200)
output = 'cards/'
folder = 'resources/inverse/' if inverse else 'resources/'
folder_resized = folder + 'resized/'
background = 'black' if inverse  else 'white'
foreground = 'black' if not inverse  else 'white'

joker_img_w = int(350 / 600 * card_w)

####### OUTSIDE CARDS #######
out_w = int(55 / 600 * card_w)
out_h_txt = 70

####### INSIDE #######
in_w = int(100 / 600 * card_w)
crown_w = 60

ace_img_w = int(200 / 600 * card_w)
back_w = 180

font_positions = [
    (out_margin, out_margin),
    (card_w - out_margin - out_w, out_margin),
    (out_margin, card_h - out_margin - out_h_txt),
    (card_w - out_margin - out_w, card_h - out_margin  - out_h_txt)
]