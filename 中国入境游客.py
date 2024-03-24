import pandas as pd
visitor_data = pd.read_excel('/Users/khan/Downloads/中国入境游客.xls')

data = [(地区, 入境游客) for 地区, 入境游客 in zip(visitor_data['地区'], visitor_data['入境游客'])]

from pyecharts.charts import Map
from pyecharts import options as opts

map = Map()
map.add("入境游客", data, maptype="world")

map.set_global_opts(
    title_opts=opts.TitleOpts(title="2018年中国境外游客客源地", subtitle="单位：万人次"),
    visualmap_opts=opts.VisualMapOpts(max_=max(visitor_data['入境游客']))
)


map.render("/Users/khan/Downloads/2018年中国境外游客客源地.html")
