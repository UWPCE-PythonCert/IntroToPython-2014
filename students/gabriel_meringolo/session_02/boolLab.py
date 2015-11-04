''' When squirrels get together for a party,
    they like to have cigars. A squirrel party
    is successful when the number of cigars is
    between 40 and 60, inclusive. Unless it is
    the weekend, in which case there is no upper
    bound on the number of cigars. Return True if
    the party with the given values is successful,
    or False otherwise. '''

def cigar_party(cigars, is_weekend):
    return (cigars >= 40 and (cigars <= 60 or is_weekend))


''' The squirrels in Palo Alto spend most of the day
    playing. In particular, they play if the temperature
    is between 60 and 90 (inclusive). Unless it is summer,
    then the upper limit is 100 instead of 90. Given an int
    temperature and a boolean is_summer, return True if the
    squirrels play and False otherwise. '''

def squirrel_play(temp, is_summer):
    return temp >= 60 and (temp <= 90 or (temp <= 100 and is_summer))