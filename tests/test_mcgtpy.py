# Import methods from our Modules
from mcgtpy.my_stats import print_stats
from mcgtpy.helper_functions import columns_janitor
from mcgtpy.database import load_nba_box_score_data

# Print stats (we don't need this necessarily ...)
print_stats()

# Tests to make sure columns_janitor() is on point
def test_1():
    input = ['  MYleS  __    _', '  _ chRistian______ George___', '____ tHomas ']
    actual = columns_janitor(input)
    expected = ['myles', 'christian_george', 'thomas']
    assert actual == expected

def test_2():
    input = ['Hey', "Hello"]
    actual = columns_janitor(input)
    expected = ["hey", "hello"]
    assert actual == expected

def test_3():
    input = ['HEY    __  ', "     A   ___  b ___ C "]
    actual = columns_janitor(input)
    expected = ["hey", "a_b_c"]
    assert actual == expected

def test_4():
    input = ['__myles___  ___', '__CHRISTIAN   gEORGE  ', '  __ THomAS _  _   ']
    actual = columns_janitor(input)
    expected = ['myles', 'christian_george', 'thomas']
    assert actual == expected

def test_5():
    input = load_nba_box_score_data()
    actual = input.shape[0]
    expected = 133831
    assert actual == expected

def test_6():
    input = ["time.of.day", "temperature.1", "temperature.30", "car.count"]
    actual = columns_janitor(input)
    expected = ["time_of_day", "temperature_1", "temperature_30", "car_count", ]
    assert actual == expected