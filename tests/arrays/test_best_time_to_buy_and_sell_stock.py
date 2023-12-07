import pytest
from arrays.best_time_to_buy_and_sell_stock import maxProfit  

@pytest.mark.parametrize("prices, expected_profit", [
    ([7, 1, 5, 3, 6, 4], 5),  # Scenario with a clear opportunity to buy low and sell high
    ([7, 6, 4, 3, 1], 0)      # Scenario with continuously decreasing prices, hence no profit
])
def test_max_profit(prices, expected_profit):
    assert maxProfit(prices) == expected_profit
