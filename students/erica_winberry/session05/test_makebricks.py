from codingbat import make_bricks

# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks 
# (5 inches each). Return True if it is possible to make the goal by 
# choosing from the given bricks. 


def test_is_possible():
    assert make_bricks(3, 1, 8)
    assert make_bricks(3, 2, 10)


def test_isnot_possible():
    assert not make_bricks(3, 1, 9)
    assert not make_bricks(0, 3, 12)


# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

