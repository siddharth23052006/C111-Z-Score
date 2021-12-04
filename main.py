import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df= pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

# fig = ff.create_distplot([data],["Math Scores"],show_hist=False)
# fig.show()

mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print("Mean of the population :",mean)
print("Standard Deviation of the population :",std_dev)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_dev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Mean of the sampling distribution :",mean)
print("Standard Deviation of the sampling distribution :",std_dev)

first_stdev_start, first_stdev_end = mean-std_dev, mean+std_dev
second_stdev_start, second_stdev_end = mean-(2*std_dev), mean+(2*std_dev)
third_stdev_start, third_stdev_end = mean-(3*std_dev), mean+(3*std_dev)

fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.2],mode='lines',name="Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 1 end"))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.2],mode='lines',name="Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 2 end"))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.2],mode='lines',name="Standard Deviation 3 start"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 3 end"))
fig.show()

#Dataset 1
df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean_of_sample_1 = statistics.mean(data)
print("Mean of sample 1 is:",mean_of_sample_1)

fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_1,mean_of_sample_1],y=[0,0.2],mode="lines",name="Mean of Sample 1"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 1 end"))
fig.show()

#Dataset 2
df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
mean_of_sample_2 = statistics.mean(data)
print("Mean of sample 2 is:",mean_of_sample_2)

fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_2,mean_of_sample_2],y=[0,0.2],mode="lines",name="Mean of Sample 2"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 2 end"))
fig.show()

#Dataset 3
df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample_3 = statistics.mean(data)
print("Mean of sample 3 is:",mean_of_sample_3)

fig = ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample_3,mean_of_sample_3],y=[0,0.2],mode="lines",name="Mean of Sample 3"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode='lines',name="Standard Deviation 3 end"))
fig.show()

z_score = (mean_of_sample_1-mean)/std_dev
print('Z score of sample 1 is', z_score)
z_score = (mean_of_sample_2-mean)/std_dev
print('Z score of sample 2 is', z_score)
z_score = (mean_of_sample_3-mean)/std_dev
print('Z score of sample 3 is', z_score)