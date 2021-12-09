import pandas as pd
from matplotlib import pyplot as plt
import threading as th
import numpy as np
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager


class Estadistico:

  def __init__(self):
    pass

  def mediaMovilNueva(n, historico):
    mm10 = historico.iloc[:,4].rolling(n, min_periods=1).mean()
    return mm10
  
 