from ..data.json_data import GETAccountID_response, position_response
from async_v20.definitions.types import Account, Position
import pandas as pd

def test_account_builds_from_dict():
    account_instance = Account(**GETAccountID_response['account'])
    assert type(account_instance) == Account
    series = account_instance.series()
    assert type(series) == pd.Series

def test_position_builds_from_dict():
    position = Position(**position_response)
    assert type(position) == Position
    series = position.series()
    assert type(series) == pd.Series