def enclose_in_tags(opening_tag, closing_tag):  # returns a decorator
    def make_with_tags(fn):  # returns a decorated function
        def wrapper():  # the function to be decorated (modified)
            return opening_tag + fn() + closing_tag
        return wrapper
    return make_with_tags


heading_decorator = enclose_in_tags("<h>", "\<h>")
bold_decorator = enclose_in_tags("<b>", "\<b>")


def hello():
    return 'world'

print(heading_decorator(hello)())
print(bold_decorator(hello)())