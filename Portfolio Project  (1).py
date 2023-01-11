#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


data = pd.read_csv("t20-world-cup-22.csv")

data.head()


# In[5]:


data.dropna()


# In[4]:


df_winner = data[['winner']]
df_winner = df_winner.dropna()
df_winner


# In[5]:


import plotly.express as px
figure = px.bar(df_winner,
                x = 'winner',
                title="Number of Matches Won by teams in t20 World Cup 2022", color="winner")
figure.show()


# In[70]:


won_by = data["won by"].value_counts()
won_by

colors_list = ['gold', 'yellowgreen']
won_by.plot(kind='pie',figsize=(15,6),
                      autopct ='%1.1f%%',
                         shadow = True,
                         labels = won_by,
                         colors = colors_list,
                         pctdistance = 1.2,
                         )
plt.title('Won by Runs/Wickets', y=1.2)
plt.axis('equal')
plt.legend(labels = won_by.index,loc ='upper left')
plt.show()


# In[71]:


toss_decision = data["toss decision"].value_counts()
toss_decision


# In[72]:


colors_list = ['pink', 'lightgreen']
toss_decision.plot(kind='pie',figsize=(15,6),
                      autopct ='%1.1f%%',
                         shadow = True,
                         labels = toss_decision,
                         colors = colors_list,
                         pctdistance = 1.2,
                         )
plt.title('Toss Decisions in T20 World Cup', y=1.2)
plt.axis('equal')
plt.legend(labels = toss_decision.index,loc ='upper left')
plt.show()


# In[6]:


figure = px.bar(data, 
                x=data["top scorer"], 
                y = data["highest score"], 
                color = data["highest score"],
                title="Top Scorers in t20 World Cup 2022")
figure.show()


# In[7]:


figure = px.bar(data,
                 x= data["player of the match"],
title = "Player of the Match Awards in t20 World Cup 2022", color= "player of the match")
figure.show()


# In[8]:


figure = px.bar(data, x= data["best bowler"],title = "Best Bowlers in t20 2022")
figure.show()


# In[9]:


plot = go.Figure(data=[go.Bar(
    name = 'first innings score',
    x = data["venue"],
    y = data["first innings score"]
   ),
                       go.Bar(
    name = 'second innings score',
    x = data["venue"],
    y = data["second innings score"]
   )
])
plot.update_layout(title = "Best stadiums to Bat first or chase")
plot.show()


# In[10]:


fig = go.Figure(data=[go.Bar(
    name = 'first innings wickets',
    x = data["venue"],
    y = data["first innings wickets"]
   ),
                       go.Bar(
    name = 'second innings wickets',
    x = data["venue"],
    y = data["second innings wickets"]
   )
])
fig.update_layout(title = "Best stadiums to Bowl first or defend")
fig.show()


# In[ ]:




