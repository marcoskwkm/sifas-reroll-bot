IDOL_TILE_X = [89, 274, 461, 648, 834, 1023, 1206]
IDOL_TILE_Y = [176, 363, 550, 736]
IDOL_TILE_XY = []
RARITY_RGB_THRESHOLD = 20

for y in IDOL_TILE_Y:
    for x in IDOL_TILE_X:
        IDOL_TILE_XY.append((x, y))

def getRarity(r, g, b):
    urRGB = [252 - r, 244 - g, 255 - b]
    srRGB = [231 - r, 153 - g, 41 - b]
    rRGB = [189 - r, 189 - g, 206 - b]

    if max(map(abs, urRGB)) < RARITY_RGB_THRESHOLD:
        return 'UR'
    elif max(map(abs, srRGB)) < RARITY_RGB_THRESHOLD:
        return 'SR'
    elif max(map(abs, rRGB)) < RARITY_RGB_THRESHOLD:
        return 'R'
    else:
        return 'unknown'
