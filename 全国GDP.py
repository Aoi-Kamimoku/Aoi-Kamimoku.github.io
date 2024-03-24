from pyecharts.charts import Map
from pyecharts import options as opts
import pandas as pd
gdp_data = pd.read_excel('/Users/khan/Downloads/全国GDP.xls')
gdp_map = Map()

gdp_map.add("GDP", [list(z) for z in zip(gdp_data['地区'].tolist(), gdp_data['GDP'].tolist())], "china")

gdp_map.set_global_opts(
    title_opts=opts.TitleOpts(title="2022年全国各省GDP地图", subtitle="单位：亿元"),
    visualmap_opts=opts.VisualMapOpts(max_=max(gdp_data['GDP']), is_piecewise=True)
)

gdp_map.render('/Users/khan/Downloads/2022年全国各省GDP地图.html')
