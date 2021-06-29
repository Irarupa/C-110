import pandas as pd
import plotly.figure_factory as ff
import statistics as stat
import plotly.graph_objects as go
import random

df = pd.read_csv('medium_data.csv')

avg = df['reading_time'].tolist()

population_mean = stat.mean(avg)
population_std = stat.stdev(avg)

print('Population_mean :', population_mean)
print('Population_std :', population_std)

def  sample_30():

    data_set = []

    for i in range(0,30):
        random_index = random.randint(0,len(avg)-1)
        value = avg[random_index]
        data_set.append(value)

    mean = stat.mean(data_set)
    std = stat.stdev(data_set)
    return mean
 
sample_meanlist = []

for i in range(0,100):
    mean = sample_30()
    sample_meanlist.append(mean)

fig = ff.create_distplot([sample_meanlist],['Sample Average'])
fig.show()



 



