'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''
def p_tag(func):
    def wrapper_p_tag(text):
        return f"<p>{func(text)}</p>"
    return wrapper_p_tag
    

@p_tag
def get_text(blurb):
    return "wrapped in p\'s"