import math

def strikethrough_text(text):
    return ''.join([char + '\u0336' for char in str(text)])


def rating_to_stars(rating, max_stars=5):
    full_stars = int(rating)
    half_star = math.ceil(rating) > full_stars and (rating - full_stars >= 0.5)
    empty_stars = max_stars - full_stars - (1 if half_star else 0)

    stars_string = '⭐' * full_stars
    if half_star:
        stars_string += '⭐️' # half-star emoji, or use a different one if preferred
    stars_string += '☆' * empty_stars
    return stars_string
