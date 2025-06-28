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

q3Data = df.query(
    'name in ["Mary", "Martha", "Peter", "Paul"] and 1920 <= year <= 2000'
)[["year", "name", "Total"]].rename(columns={"name": "Name"})

q3DataPlot = ggplot(
    data=q3Data,
    mapping=aes(x="year", y="Total", color="Name"),
) + geom_line(stat="identity")

q3DataAlt = q3Data.copy()


def compute_relative(row):
    baseFrequency = df.query(f'name == "{row["Name"]}" and year == 1920')[
        "Total"
    ].values[0]
    return row["Total"] / baseFrequency


q3DataAlt["Relative"] = q3DataAlt.apply(compute_relative, axis=1)

q3DataPlotAlt = ggplot(
    data=q3DataAlt,
    mapping=aes(x="year", y="Relative", color="Name"),
) + geom_line(stat="identity")
