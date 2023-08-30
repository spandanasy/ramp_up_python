import pandas as pd
import plotly.express as px

data = pd.read_excel(r"C:\Users\Spandana SY-int-219\Desktop\PYTHON_TASK\task9.xlsx")

fig = px.treemap(data,
                 path=['Area'],
                 values='Team Members',
                 color='Color',
                 color_discrete_map={'Dark Green': 'rgb(88, 175, 78)',
                                     'One Level Below Dark Green': 'rgb(157, 209, 145)',
                                     'One Level Above Light Green': 'rgb(191, 225, 182)',
                                     'Two Level Above Light Green': 'rgb(180, 255, 153)',
                                     'White': 'rgb(255, 255, 255)',
                                     'Light Green': 'rgb(144, 238, 144)',
                                     'Two Level Below Dark Green': 'rgb(134, 230, 132)'
                                     })

fig.show()
fig.write_html('heatmap_1.html')

