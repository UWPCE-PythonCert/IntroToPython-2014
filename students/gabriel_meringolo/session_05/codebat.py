
def sleep_in(weekday, vacation):
    return not (weekday and vacation)

def cigar_party(cigars, is_weekend):
    return (is_weekend and cigars >= 40) or not is_weekend and (cigars >= 40 and cigars <= 60)