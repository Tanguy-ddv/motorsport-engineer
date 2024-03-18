"""Mathematical functions used by the game"""
def affine2(x, min_, max_, sep_x, sep_y):
    """
    The affine2 function is defined as followed:

    if 0 <= x <= sep_x, return x following an affine function between (0, min_) and (sep_x, sep_y)
    if sep_x < x <=1, return x following an affine function between (sep_x, sep_y) and (1, max_)
    else, returns an error. 
    """
    if not 1 >= x >= 0:
        raise ValueError("x must be between 0 and 1, got ", x)
    if not 1 > sep_x > 0:
        raise ValueError("sep must be between 0 and 1, got ", sep_x)
    if x <= sep_x:
        return min_ + (sep_y - min_)/sep_x*x
    else:
        return (max_ - sep_y)/(1-sep_x)*x + sep_y - (max_ - sep_y)/(1-sep_x)*sep_x