def running_avg():
    """
    Coroutine that accepts numbers and yields their running average

    This type of generator is driven by input to .send()
    However, the code inside a generator must execute up to the first
    yield expression before it can accept any value from the caller.
    That means that the caller always has to call .next() (or .send(None))
    once after creating a generator object before sending it data.

    So let's call .next() to advance the program counter to the
    first yield expression, then start passing values we would like averaged
    """
    total = float((yield))
    count = 1
    while True:
        i = yield total / count
        count += 1
        total += i

