from consts import *
from numpy import pi, sin, cos

def get_corner_text_positions():
    w_left = outer_margin + sym_w_corner//2
    w_right = card_w - outer_margin - sym_w_corner//2
    h_top = outer_margin + txt_h_corner//2
    h_bottom = card_h - outer_margin - txt_h_corner//2

    top_left = (w_left, h_top)
    top_right = (w_right, h_top)
    bottom_left = (w_left, h_bottom)
    bottom_right = (w_right, h_bottom)
    return [top_left, top_right, bottom_left, bottom_right]

def get_corner_joker_positions(dims):
    txt_w, txt_h = dims[0], dims[1]
    top_left = (outer_margin + (sym_w_corner - txt_w)//2 + txt_w//2, outer_margin + txt_h//2 - joker_h_offset)
    bottom_right = (card_w - outer_margin - (sym_w_corner - txt_w)//2 - txt_w//2, card_h - outer_margin - txt_h//2 + joker_h_offset)
    return [top_left, bottom_right]

def get_corner_symbol_positions(sym_h_max_corner):
    w_left = outer_margin + sym_w_corner//2
    w_right = card_w - outer_margin - sym_w_corner//2
    h_top = outer_margin + txt_h_corner + sym_h_max_corner//2
    h_bottom = card_h - outer_margin - txt_h_corner - sym_h_max_corner//2

    top_left = (w_left, h_top)
    top_right = (w_right, h_top)
    bottom_left = (w_left, h_bottom)
    bottom_right = (w_right, h_bottom)
    return [top_left, top_right, bottom_left, bottom_right]

def get_inner_grid_positions(sym_h_max_inside):
    center_w = card_w//2
    center_h = card_h//2

    margin_w = (card_w - 2 * outer_margin - 2 * sym_w_corner - 2 * inner_margin - sym_w_inside)//2
    margin_h = (card_h - 2 * outer_margin - 2 * inner_margin - sym_h_max_inside)//2

    pos_1 = (int(center_w),             int(center_h - 1 * margin_h))
    pos_2 = (int(center_w),             int(center_h + 1 * margin_h))
    pos_3 = (int(center_w),             int(center_h))
    pos_4 = (int(center_w - margin_w),  int(center_h - 1 * margin_h))
    pos_5 = (int(center_w + margin_w),  int(center_h - 1 * margin_h))
    pos_6 = (int(center_w - margin_w),  int(center_h + 1 * margin_h))
    pos_7 = (int(center_w + margin_w),  int(center_h + 1 * margin_h))
    pos_8 = (int(center_w - margin_w),  int(center_h))
    pos_9 = (int(center_w + margin_w),  int(center_h))
    pos_10 = (int(center_w),            int(center_h - 1/2 * margin_h))
    pos_11 = (int(center_w),            int(center_h + 1/2 * margin_h))
    pos_12 = (int(center_w - margin_w), int(center_h - 1/3 * margin_h))
    pos_13 = (int(center_w + margin_w), int(center_h - 1/3 * margin_h))
    pos_14 = (int(center_w - margin_w), int(center_h + 1/3 * margin_h))
    pos_15 = (int(center_w + margin_w), int(center_h + 1/3 * margin_h))
    pos_16 = (int(center_w),            int(center_h - 2/3 * margin_h))
    pos_17 = (int(center_w),            int(center_h + 2/3 * margin_h))

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

def get_hutschmuck_position(paling_pos, paling_w):
    return (int(paling_pos[0] - 0.4 * paling_w), int(paling_pos[1] - 0.01 * paling_w))

def get_back_main_positions(number_of_symbols):
    margin_to_center = (min(card_h, card_w) - 2 * outer_margin - sym_w_big//2)//2
    positions = []

    for idx in range(number_of_symbols):
        angle = idx / len(number_of_symbols) * 360
        x = int(card_w//2 - margin_to_center * sin(angle * pi / 180))
        y = int(card_h//2 - margin_to_center * cos(angle * pi / 180))
        positions.append(x, y)

    return positions