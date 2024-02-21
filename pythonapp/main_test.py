import main

def test_get_avergage_amount():
  value = main.get_avergage_amount([60.5, 10.0])
  assert value == 35.25

def test_get_total_balance():
  value = main.get_total_balance([60.5, 10.0], [-10.3, -20.46])
  assert value == 39.74

def test_format_month_tx():
  value = main.format_month_tx({'July': 2, 'August': 2})
  assert value == 'Number of transactions in July : 2\nNumber of transactions in August : 2'
