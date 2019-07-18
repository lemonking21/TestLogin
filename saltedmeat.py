from passlib.hash import sha256_crypt
def prepare_the(meat):
    meat = sha256_crypt.hash(meat)
    return meat
def inspect_the(meat, oldmeat):
    meat2_inspect = meat
    meat = sha256_crypt.verify(meat2_inspect,oldmeat)
    return meat