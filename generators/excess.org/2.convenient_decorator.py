# The flow is always the same when working with generators.

# 1) Generator object is created by the caller
# 2) The caller starts the generator
# 3) Generator passes data to the caller (or signals the end of the sequence)
# 4) The caller passes data to the generator
# 5) repeat from (3)


def advanced_generator_once(original_func):
    """
    Decorator to advance a generator once immediately after it is created

    This will turn a generator function into a function that returns
    a generator immediately ready to receive data (step 4).
    """
    def actual_call(*args, **kwargs):
        gen = original_func(*args, **kwargs)
        assert next(gen) is None
        return gen
    return actual_call


# We apply our decorator to running_avg().
#   >>> running_avg = advance_generator_once(running_avg)

# Now we don't need to call .next() every time
# we create a new running average generator.
#   >>> r = running_avg()
#   >>> r.send(42)
#   >>> 42.0
