
from bokeh.plotting import figure, output_file, show
import numpy as np
import statsmodels.api as sm
import pandas as pd
import numpy as np

# prepare some data
df = pd.read_csv('AirPassengers.csv')
x = df.time
y = df.AirPassengers
x = sm.add_constant(x)

output_file("result.html")

TOOLS="pan,wheel_zoom,box_zoom,reset,save"

#plot the scatter
p1 = figure(tools=TOOLS, plot_width=300, plot_height=300)
p1.scatter(df.time, y, size=4, color="red", alpha=0.5)

#construct ols regression model
model = sm.OLS(y,x)
results = model.fit()
print results.summary()

#plot the regression line
x_line = np.linspace(df.time.min(),df.time.max(),100)[:,np.newaxis]
x_line = sm.add_constant(x_line)
y_line = results.predict(x_line)

p1.line(x_line[:,1],y_line,color = "blue")
show(p1)

