import pytest
from src.range_function import ranges

def test_point():
    assert ranges([[3,0] - [0,4.5]]) == [0,0]



### scenario 1 point
#    - Parameters:  [3,0 - 0,4.5]
#    - Result: [0,0] "Coinciding number"