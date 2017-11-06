# When paused at a yield statement generator objects
# can receive data by using .send() instead of .next().

# When we use yield as an expression or assign it to a variable,
# the value passed to .send() is available inside the generator.


def knock_knock():
    name = yield "Who's there?"
    yield "%s who?" % name
    yield "That's not funny at all"

# We have to switch to manually calling .next() on our generator object,
# because a for loop or function that takes an iterable
# won't be able to call .send() when we need to.

k = knock_knock()
next(k)
# >>> "Who's there?"

# At this point execution is paused at the first yield.
# The assignment to the variable name hasn't happened yet.
# But when we .send() a value execution continues:

k.send("David")
# >>>'David who?'

# In generator object we are at the second yield with "David" assigned to name.

# If we send something to a yield that isn't being used as an expression,
# the value we send will be ignored:

k.send("David the environmentalist")
# >>>"That's not funny at all"

# But execution continues the same as if we called .next()
