def double(func):
    def wrapper(*args, **kwargs):
        doubled_result = func(*args, **kwargs) * 2
    return wrapper

@double
def get_color_code(color):
    color_codes = {'black': '#000000', 'white': '#FFFFFF'}
    return color_codes[color]

print(get_color_code('white'))