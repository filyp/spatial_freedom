import re

from PySide6.QtGui import QColor, QFont

# _colors = ["hsl(184, 96%, {}%)", "hsl(64, 96%, {}%)", "hsl(136, 96%, {}%)"]
_color_non_persistent = "hsl(341, 96%, {}%)"

colemak_keys = {
    # move to neighbors
    "<A-S-n>": "move down",
    "<A-S-e>": "move up",
    "<A-S-m>": "move left",
    "<A-S-i>": "move right",
    # create a child of the current text box, down of it
    "<A-n>": "create child down",
    # create a child of the current text box, right of it
    "<A-i>": "create child right",
    # catch a child and insert it down
    "<A-C-n>": "catch child down",
    # catch a child and insert it right
    "<A-C-i>": "catch child right",
    # zooming
    "<C-j>": "zoom down",
    "<C-y>": "zoom up",
    # resizing box
    "<C-l>": "grow box",
    "<C-u>": "shrink box",
}


class Config:
    autoshrink = True
    text_width = 350
    text_max_height = text_width * 1.618
    initial_position = (500, 40)
    text_gap = 6
    starting_box_scale = 0.6

    # whether to change zoom level only on jumps to a neighbor text
    track_jumps_on_neighbor_moves = False

    # closer to 1 is slower (must be larger than 1)
    scroll_speed = 1.0005
    # invert scroll direction
    scroll_invert = True
    # speed of zooming left/right with keys (must be larger than 1)
    key_zoom_speed = 3

    # https://blog.depositphotos.com/15-cyberpunk-color-palettes-for-dystopian-designs.html
    background_color = "#000000"
    border_brightness = "15%"
    text_brightness = "80%"
    selection_brightness = "23%"
    non_persistent_hue = 341
    sign_color = QColor.fromHsl(289, 100, 18)

    leader_key = ","
    # supported single key codes, and single key codes preceded with leader key
    # (note: the order of modifiers must be M-, A-, S-, C-)
    keys = {
        # hop to any text using leap plugin
        ",h": "hop",
        # when in bookmarks window, jump to location of bookmark under cursor
        ",b": "bookmark jump",
        # zoom on the current text box
        ",z": "zoom on current text",
        # custom C-o and C-i, because normal ones create unwanted buffers
        "<C-o>": "jump back",
        "<C-i>": "jump forward",
    }
    keys.update(colemak_keys)

    # relevant for zooming and resizing with keys
    FPS = 180

    input_on_creation = "- "

    # font sizes for each indent level
    # font_sizes = [16] * 4 + [14] * 4 + [11] * 4
    # font_sizes = [15] * 4 + [14] * 4 + [11] * 4
    font_sizes = [14] * 4 + [11] * 4 + [8] * 4
    # font_sizes = [11] * 4 + [8] * 4 + [6] * 4
    # some font sizes cause indent problems:
    # note that the problems also depent on the intended indent of that font
    # the combinations above are one of the very few that work well, so it's
    # recommended to just choose one of those
    # good values for first indent lvl: 16, 15, 14, 11
    # for the second indent level: 14, 11, 8, 6
    # for the third indent level: 14, 11, 8, 6, 5

    ########################
    # don't tweak those - those are automatic calculations
    _initial_distance = (initial_position[0] ** 2 + initial_position[1] ** 2) ** 0.5

    fonts = [QFont("monospace", fs) for fs in font_sizes]
