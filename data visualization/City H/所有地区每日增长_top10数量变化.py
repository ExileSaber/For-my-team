import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', 10000, 'display.max_rows', 10000)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


data_dir = 'D:/python/venv/2020year/2020 IKCEST/train_data_all'
file = 'city_H'
names = ['density.csv', 'grid_attr.csv', 'infection.csv', 'migration.csv', 'transfer.csv', 'weather.csv']
'''
infection.csv
城市中每个区域每天增长人数
'''
'''
migration.csv
城市之间的人口迁移，有一个迁移指数不知道定义
迁移指数：可能就是一个衡量城市之间迁移强度的指标

density.csv
网格人流量指数

transfer.csv
网格关联强度

grid_attr.csv
网格归属区域

weather.csv
城市天气数据
'''
Index = [
    ['data', 'hour', 'grid_x', 'grid_y', 'Population_flow_index'],
    ['grid_x', 'grid_y', 'region_id'],
    ['city', 'region_id', 'data', 'num_new_persons'],
    ['data', 'departure_city', 'arrival_city', 'migration_scale_index'],
    ['hour', 'start_grid_x', 'start_grid_y', 'end_grid_x', 'end_grid_y', 'transfer_intensity'],
    ['data', 'hour', 'temperature', 'humidity', 'wind_direction', 'wind_speed', 'wind_force', 'weather']
]

i = 2
name = names[i]
dir = data_dir + '/' + file + '/' + name
print('目前文件为{}'.format(name))
data = pd.read_csv(dir, header=0, names=Index[i])
print(data[:5])

days = data['data'].unique()
print(days)
region_id = data['region_id'].unique()
top_10 = {}

for id in region_id:
    data_ = data[data['region_id'] == id]
    x = range(data_.shape[0])
    y_ = list(data_['num_new_persons'])
    if len(top_10.keys()) < 10:
        top_10[id] = max(y_)
    else:
        if max(y_) > min(top_10.values()):
            top_10[id] = max(y_)
            m = min(top_10.keys(), key=(lambda x: top_10[x]))
            top_10.pop(m)
    plt.plot(x, y_)

x = range(len(days))
plt.xticks(x, days, rotation=90)
plt.title('H城市各区域每日增长人数')
plt.savefig(r'D:\python\venv\2020year\2020 IKCEST\data visualization\Plot\city_H\H城市各区域每日增长人数')
plt.show()
print('=================')

top_10_list = sorted(top_10.items(), key=lambda x: x[1])
print(top_10_list)

top_10_id = sorted(top_10, key=lambda x: top_10[x])
for id in top_10_id:
    data_ = data[data['region_id'] == id]
    x = range(data_.shape[0])
    y_ = list(data_['num_new_persons'])
    plt.plot(x, y_)

x = range(len(days))
plt.xticks(x, days, rotation=90)
plt.legend(top_10_id)
plt.title('H城市Top10区域每日增长人数')
plt.savefig(r'D:\python\venv\2020year\2020 IKCEST\data visualization\Plot\city_H\H城市Top10区域每日增长人数')
plt.show()


