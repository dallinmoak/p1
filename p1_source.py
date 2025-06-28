import pandas as pd
import numpy as np
from lets_plot import *
from lets_plot import ggsize

LetsPlot.setup_html(isolated_frame=True)

df = pd.read_csv(
    "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
)
# for practice imma try to render a table that shows total use of "Dallin in the US for all years"
cols_to_print = ["name", "year", "Total"]
target_name = "Dallin"
my_query = f'name == "{target_name}"'
my_name_plot_data = df.query(my_query)[cols_to_print]

my_name_plot = (
    ggplot(
        data=my_name_plot_data,
        mapping=aes(
            x="year",
            y="Total",
        ),
    )
    + geom_bar(stat="identity")
    + scale_x_continuous(format="d")
)

brittany_plot_data = df.query('name == "Brittany"')[cols_to_print]

brittany_plot_data["age"] = 2025 - brittany_plot_data["year"]

brittany_plot = (
    ggplot(
        data=brittany_plot_data,
        mapping=aes(
            x="age",
            y="Total",
        ),
    )
    + geom_bar(stat="identity")
    + scale_x_continuous(format="d")
)

q3_data = df.query(
    'name in ["Mary", "Martha", "Peter", "Paul"] and 1920 <= year <= 2000'
)[["year", "name", "Total"]].rename(columns={"name": "Name"})

q3_data_plot = (
    ggplot(
        data=q3_data,
        mapping=aes(x="year", y="Total", color="Name"),
    )
    + geom_line(stat="identity")
    + scale_x_continuous(format="d")
)

q3_data_alt = q3_data.copy()


def compute_relative(row):
    base_frequency = df.query(f'name == "{row["Name"]}" and year == 1920')[
        "Total"
    ].values[0]
    return row["Total"] / base_frequency


q3_data_alt["Relative"] = q3_data_alt.apply(compute_relative, axis=1)

q3_data_plot_alt = (
    ggplot(
        data=q3_data_alt,
        mapping=aes(x="year", y="Relative", color="Name"),
    )
    + geom_line(stat="identity")
    + scale_x_continuous(format="d")
)

movie_name = r"(^|.+[\s-])Neo($|[\s-].+)"

movie_name_data = df[df["name"].str.contains(movie_name, case=False)][cols_to_print]

movie_name_plot = (
    ggplot(
        data=movie_name_data,
        mapping=aes(
            x="year",
            y="Total",
        ),
    )
    + geom_bar(stat="identity")
    + scale_x_continuous(format="d")
)

elliot_data = df.query('name == "Elliot"')[cols_to_print]
elliot_data["year"] = elliot_data["year"].astype(float)

elliot_plot = (
    ggplot(
        data=elliot_data,
        mapping=aes(x="year", y="Total", color="name"),
    )
    + geom_line(stat="identity")
    + labs(color="name")
    + ggtitle("Elliot... What?")
    + geom_vline(xintercept=1982, color="blue", linetype="dashed")
    + geom_vline(xintercept=1985, color="blue", linetype="dashed")
    + geom_vline(xintercept=2002, color="blue", linetype="dashed")
    + scale_x_continuous(limits=[1950, 2025])
    + ggsize(width=700, height=400)
    + scale_x_continuous(format="d")
)
