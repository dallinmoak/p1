import pandas as pd
import numpy as np
from lets_plot import *

LetsPlot.setup_html(isolated_frame=True)

df = pd.read_csv(
    "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
)
# for practice imma try to render a table that shows total use of "Dallin in the US for all years"
colsToPrint = ["name", "year", "Total"]
targetName = "Dallin"
myQuery = f'name == "{targetName}"'
myNamePlotData = df.query(myQuery)[colsToPrint]

myNamePlot = ggplot(
    data=myNamePlotData,
    mapping=aes(
        x="year",
        y="Total",
    ),
) + geom_bar(stat="identity")

brittanyPlotData = df.query('name == "Brittany"')[colsToPrint]

brittanyPlotData["age"] = 2025 - brittanyPlotData["year"]

brittanyPlot = ggplot(
    data=brittanyPlotData,
    mapping=aes(
        x="age",
        y="Total",
    ),
) + geom_bar(stat="identity")
