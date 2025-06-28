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
res = df.query(myQuery)[colsToPrint]

(
    ggplot(
        data=res,
        mapping=aes(
            x="year",
            y="Total",
        ),
    )
    + geom_bar()
)
