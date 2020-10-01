import numpy as np
import pandas as pd


def RSI(df, min_periods = 14):
    difference = df.diff(1)
    difference_up = difference.where(difference > 0, 0.0)
    difference_down = difference.where(difference < 0, 0.0)
    exponentialMovingAverage_up = difference_up.ewm(alpha=1/min_periods, min_periods=min_periods, adjust=False).mean()
    exponentialMovingAverage_down = difference_down.ewm(alpha=1/min_periods, min_periods=min_periods, adjust=False).mean()
    relative_strength = exponentialMovingAverage_up / exponentialMovingAverage_down
    return pd.Series(np.where(exponentialMovingAverage_down == 0, 100, 100-(100/(1+relative_strength))), index=df.index)