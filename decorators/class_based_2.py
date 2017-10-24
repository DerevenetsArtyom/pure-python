class function_wrapper:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __call__(self, *args, **kwargs):
        return self.wrapped(*args, **kwargs)


@function_wrapper
def function():
    pass

