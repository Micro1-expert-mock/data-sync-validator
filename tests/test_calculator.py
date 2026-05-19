from src.calculator import calculate_growth

def test_calculate_growth_positive():
    # Expected growth is 50%, but the broken logic will return -50
    assert calculate_growth(100, 150) == 50.0
