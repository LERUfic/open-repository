import numpy as np
import pandas as pd

def TSI(df, low=13, high=25):
    pc = df.shift(1)
    double_smoothed_pc = pc.ewm(span=low, min_periods=low, adjust=False).mean().ewm(span=high, min_periods=high, adjust=False).mean()
    double_smoothed_absolute_pc = abs(pc).ewm(span=low, min_periods=low, adjust=False).mean().ewm(span=high, min_periods=high, adjust=False).mean()
    tsi = (double_smoothed_pc / double_smoothed_absolute_pc) * 100
    return pd.Series(tsi, name="TSI")
