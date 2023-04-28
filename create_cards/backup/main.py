import os
import numpy as np
from numpy import pi as pi
from PIL import Image, ImageDraw, ImageFont, ImageOps

from funcs import resize_images, get_positions, AdjustYPos, create_card, create_joker, create_back, create_full_deck
from consts import *

# resize color images
h_max_smol = resize_images(colors + ['clubs_rgb'], folder, subfolder='colors', width_scaled=True, dim=out_w)
h_max_big = resize_images(colors + ['clubs_rgb'], folder, subfolder='colors', width_scaled=True, dim=in_w, smol='big')
h_max_ace = resize_images(colors, folder, subfolder='colors', width_scaled=True, dim=ace_img_w, smol='ace')
h_max_back = resize_images(colors, folder, subfolder='colors_mit_rand', width_scaled=True, dim=back_w, suffix='mit_rand', smol='back')
resize_images(colors, folder, subfolder='hutschmuck', width_scaled=True, dim=crown_w, prefix='king')
resize_images(["queen_schraeg_klein"], folder, subfolder='hutschmuck', width_scaled=True, dim=crown_w)
resize_images(["bube"], folder, subfolder='hutschmuck', width_scaled=True, dim=crown_w)
resize_images(jokers, folder, subfolder='jokers', width_scaled=True, dim=joker_img_w, smol='joker')

for color in colors:
    for card in cards:
        create_card(color, card, h_max_smol, h_max_big)
        pass

for joker in jokers:
    create_joker(joker)

create_back(h_max_back)
create_full_deck()