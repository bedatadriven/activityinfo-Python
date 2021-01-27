from cuid import CuidGenerator


def generate_id():
    cuid = CuidGenerator()
    return cuid.cuid()
