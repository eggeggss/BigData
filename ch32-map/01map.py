#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import pandas as pd
from mapsplotlib import mapsplot as mplt
df = pd.read_csv("data.csv")
mplt.register_api_key('your_google_api_key_here')
mplt.density_plot(df['latitude'], df['longitude'])