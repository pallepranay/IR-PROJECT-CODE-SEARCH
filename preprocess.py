from modules import *
from loader import *


def drop_nan(data):
    data = load_data()

    data.dropna(inplace=True)
    return data
