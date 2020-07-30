'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''
def tag_it(func):
    def wrapper_tag_it(text, tag_name):
        return f"<{tag_name}>{func(text, tag_name)}</{tag_name}>"
    return wrapper_tag_it
    

@tag_it
def get_text(blurb, tag):
    return blurb

print(get_text("now is the time", "h1"))