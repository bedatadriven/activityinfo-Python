from cuid import CuidGenerator

cuid = CuidGenerator()


def generate_id():
    return cuid.cuid()


def cuid_counter():
    """Return value of counter in CUID generator

    Used for testing purposes only. Note that a call to the 'counter' property of CuidGenerator will increase the
    counter value by 1.
    """
    return cuid.counter
