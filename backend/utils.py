import re

ALPHABET_MALGACHE = "abdefghijklmnoprstvyz"
MOT_INTERDIT_PATTERN = re.compile(r'^(?:nk)|nb|mk|dt|bp|sz', re.IGNORECASE)
ALPHABET_PATTERN = re.compile(f'^[{ALPHABET_MALGACHE}]+$', re.IGNORECASE)
DOUBLES_INTERDITS = re.compile(r'(.)\1', re.IGNORECASE)

def mot_valide(mot):
    """Vérifie qu'un mot est orthographiquement valide en malgache."""
    if not mot:
        return False
    if not ALPHABET_PATTERN.match(mot):
        return False
    if MOT_INTERDIT_PATTERN.search(mot):
        return False
    # if DOUBLES_INTERDITS.search(mot):
        # return False
    return True

