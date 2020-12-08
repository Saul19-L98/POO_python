# Este error de from ocurre debido a que se debe seleccionar el ambiente virtual de pip para poder ser ejecutado correctamen, ya sea seleccionarlo en vscode con ctrl + shift + p o en la terminal de comandos.
from bokeh.plotting import figure, output_file, show

x = [1,2,3,4,5]
y = [4,6,2,4,3]

p = figure(
    title = 'Simple Example',
    x_axis_label = 'x Axis',
    y_axis_label = 'Y Axis'
)

p.line(x,y, legend_label='Test', line_width = 2)

show(p)