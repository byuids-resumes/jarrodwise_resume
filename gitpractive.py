#%%
import pandas as pd
import altair as alt
import numpy as np

dat = pd.read_csv('https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.csv')
# %%
dat.hp.fillna(value=dat.hp.mean(), inplace=True)
# %%
dat.dropna(subset=['car'])
# %%
source = dat.dropna(subset=['car'])

base = alt.Chart(source).mark_circle(size=20, color='red').encode(
    x=alt.X('hp', title="Horsepower"),
    y=alt.Y('mpg', title='Miles_per_Gallon')
)

line = base.mark_rule().encode(
    x=alt.X(value=355)
)

chart = base + line
# %%
