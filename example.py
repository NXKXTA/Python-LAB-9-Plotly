import plotly.express as px

# df = px.data.iris()
# print(df.head())
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
#                  size='petal_length', hover_data=['petal_width'])
# fig.show()
df = px.data.gapminder().query("year==2007")
print(df.head())
fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="gdpPercap",
                     projection="natural earth")
fig.show()
