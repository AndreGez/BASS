from positions import *
from image_handling import *
from consts import *
import numpy as np

def create_cards(sym_h_max, sym_inner_h_max, sym_aces_h_max):
    folder = 'data/resized/colors/'
    folder_inner = 'data/resized/colors_inner/'
    folder_aces = 'data/resized/colors_aces/'
    corner_text_positions = get_corner_text_positions()
    corner_symbol_positions = get_corner_symbol_positions(sym_h_max)
    inner_grid_positions = get_inner_grid_positions(sym_inner_h_max)
    for color in colors:
        for card in cards:
            canvas = create_canvas(card_w, card_h, background)
            for idx, pos in enumerate(corner_text_positions):
                text_canvas, _ = get_text_canvas(font_size_corner, card, 'black')
                # gespiegelt 2 und 3, gedreht 3, 4
                place_image(canvas, text_canvas, pos, idx in [2, 3])
            for idx, pos in enumerate(corner_symbol_positions):
                if card == '7' and color == 'clubs':
                    sym = Image.open(folder + color + '_rgb_smol' + '.png')
                else:
                    sym = Image.open(folder + color + '_smol' + '.png')
                place_image(canvas, sym, pos, idx in [2, 3], idx in [1, 2])
            if card.isnumeric():
                if card == '7' and color == 'clubs':
                    sym = Image.open(folder_inner + color + '_rgb_inner' + '.png')
                else:
                    sym = Image.open(folder_inner + color + '_inner' + '.png')
                for pos in inner_grid_positions[int(card) - 2]:
                    place_image(canvas, sym, pos, pos[1]>card_h//2)
            elif card == 'A':
                sym = Image.open(folder_aces + color + '_aces' + '.png')
                place_image(canvas, sym, (card_w//2, card_h//2))
            elif card == 'K':
                paling = Image.open('data/resized/gladde/paling_r_2_smol.png')
                paling_hat = Image.open('data/resized/hutschmuck/king_' + color + '_smol.png')
                place_image(canvas, paling, (card_w//2, card_h//2))
                hut_pos = get_hutschmuck_position((card_w//2, card_h//2), paling.width)
                place_image(canvas, paling_hat, hut_pos)
            elif card == 'D':
                paling = Image.open('data/resized/gladde/paling_g_2_smol.png')
                paling_hat = Image.open('data/resized/hutschmuck/queen_schraeg_klein_smol.png')
                place_image(canvas, paling, (card_w//2, card_h//2))
                hut_pos = get_hutschmuck_position((card_w//2, card_h//2), paling.width)
                place_image(canvas, paling_hat, hut_pos)
            elif card == 'B':
                paling = Image.open('data/resized/gladde/paling_b_2_smol.png')
                paling_hat = Image.open('data/resized/hutschmuck/bube_smol.png')
                place_image(canvas, paling, (card_w//2, card_h//2))
                hut_pos = get_hutschmuck_position((card_w//2, card_h//2), paling.width)
                place_image(canvas, paling_hat, hut_pos)
            canvas.save(output_folder + color + '_' + card + '.png')

def create_jokers():
    for filename in os.listdir('data/resized/jokers'):
        canvas = create_canvas(card_w, card_h, background)
        joker = Image.open('data/resized/jokers/' + filename)
        place_image(canvas, joker, (card_w//2, card_h//2))
        txt_cvs, dims = get_text_canvas(font_size_corner, 'J\nO\nK\nE\nR', 'black', flipped=False, vertical=True)
        positions = get_corner_joker_positions(dims)
        for idx, pos in enumerate(positions):
            place_image(canvas, txt_cvs, pos, idx == 1)
        canvas.save(output_folder + 'joker_' + filename)

def create_back():
    canvas = create_canvas(card_w, card_h, (30, 30, 42))
    back = Image.open('data/resized/logo/bass_back_smol.png')
    background = Image.open('data/resized/background/background_cut.png')
    place_image(canvas, background, (card_w//2, card_h//2))
    place_image(canvas, back, (card_w//2, card_h//2))
    canvas.save(output_folder + 'back.png')


def create_overview():
    h = 0
    w = 0
    margin = 100
    files = os.listdir(output_folder);
    files.sort(reverse=True)
    num_items = len(files)
    height, width = np.ceil(np.sqrt(num_items)), np.ceil(np.sqrt(num_items))
    canvas = create_canvas(int(width * (card_w + margin) - margin), int(height * (card_h + margin) - margin), foreground, False)
    for i, filename in enumerate(files):
        img = Image.open(output_folder + filename)
        place_image(canvas, img, (card_w // 2 + w * (card_w + margin), card_h // 2 + h * (card_h + margin)))
        w += 1
        if w >= width:
            w = 0
            h += 1
    canvas.save(output_folder + 'overview.png')


if __name__ == '__main__':
    sym_h_max = resize_images('colors/', 'colors/', 'smol', sym_w_corner)
    sym_inner_h_max = resize_images('colors/', 'colors_inner/', 'inner', sym_w_inside)
    sym_aces_h_max = resize_images('colors/', 'colors_aces/', 'aces', sym_w_big)
    resize_images('gladde/', 'gladde/', 'smol', card_w - 2 * (outer_margin + sym_w_corner))
    resize_images('hutschmuck/', 'hutschmuck/', 'smol', hutschmuck_w)
    resize_images('jokers/', 'jokers/', 'smol', card_w - 2 * (outer_margin + sym_w_corner))
    resize_images('logo/', 'logo/', 'smol', card_w)
    cut_to_card_size('background/', 'background/', 'cut')
    for f in os.listdir(output_folder):
        os.remove(output_folder + f)
    create_cards(sym_h_max, sym_inner_h_max, sym_aces_h_max)
    create_jokers()
    create_back()
    create_overview()