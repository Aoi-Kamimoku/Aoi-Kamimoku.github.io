from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Grid
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pandas as pd

df = pd.read_excel('/Users/khan/Downloads/金融业数据.xls')

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(df['时间'].tolist())
    .add_yaxis("货币(M1)供应量", df['货币(M1)供应量'].tolist(), yaxis_index=0)
    .add_yaxis("准货币(M2)供应量", df['准货币(M2)供应量'].tolist(), yaxis_index=0)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国金融业数据"),
        yaxis_opts=opts.AxisOpts(
            name="亿元",
            axislabel_opts=opts.LabelOpts(formatter=JsCode("function(value){return value + ' 亿元';}"))
        ),
    )
)

line = (
    Line()
    .add_xaxis(df['时间'].tolist())
    .add_yaxis("货币(M1)供应量同比增长率", df['货币(M1)供应量同比增长率'].tolist(), yaxis_index=1)
    .add_yaxis("准货币(M2)供应量同比增长率", df['准货币(M2)供应量同比增长率'].tolist(), yaxis_index=1)
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="百分比",
            axislabel_opts=opts.LabelOpts(formatter=JsCode("function(value){return value + ' %';}")),
            position="right"
        ),
    )
)

grid = (
    Grid()
    .add(bar, grid_opts=opts.GridOpts(pos_left="5%", pos_right="20%"))
    .add(line, grid_opts=opts.GridOpts(pos_left="5%", pos_right="20%"))
)

grid.render('金融业数据_组合图表.html')

