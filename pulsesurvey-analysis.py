#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


# In[34]:


# Add Survey Dataset
surveydata = pd.read_csv('pulse-survey.csv')

# Add Survey Datasets by Area (download individually in Leapsome)
survey_data_commercial = pd.read_csv('survey-data-commercial.csv')
survey_data_operations = pd.read_csv('survey-data-operations.csv')
survey_data_tech = pd.read_csv('survey-data-tech.csv')
survey_data_product = pd.read_csv('survey-data-product.csv')


# In[35]:


#print(surveydata)


# # Filter by Question

# In[40]:


# Select a question
question = 'I would recommend Latana as a great place to work'

# Question list
# I would recommend Latana as a great place to work
# I feel I am given enough freedom to decide how to do my work
# I know how my work supports the goals of Latana
# My job at Latana enables me to learn and develop new skills
# My work gives me the opportunity to do what I do best every day
# I can count on my co-workers to help out when needed
# If I do good work, I know that it will be recognized
# I get enough feedback on how well I'm doing my job
# I find my workload manageable
# I am able to maintain a good work-life balance while working remotely
# Latana does a good job at fostering a diverse and inclusive environment.
# I see myself still working at Latana in one years’ time
# At Latana employee health and well-being are a priority
# My team is able to collaborate effectively while working remotely


# In[41]:


# Filter survey data by question
filtered_question = surveydata[surveydata.Question == question]
distribution = filtered_question['Score'].values

# Filter survey data by area and question

# Commercial
filtered_question_commercial = survey_data_commercial[survey_data_commercial.Question == question]
filtered_commercial = filtered_question_commercial['Score'].values

# Operations
filtered_question_operations = survey_data_operations[survey_data_operations.Question == question]
filtered_operations = filtered_question_operations['Score'].values

# Tech
filtered_question_tech = survey_data_tech[survey_data_tech.Question == question]
filtered_tech = filtered_question_tech['Score'].values

# Product
filtered_question_product = survey_data_product[survey_data_product.Question == question]
filtered_product = filtered_question_product['Score'].values


# In[47]:


# Plot Distribution
# Calculates mean, median on all data and data of areas
# Benchmark must be manually added

plt.figure(figsize=(16, 8))
ax = plt.subplot()
plt.hist(distribution, bins=11)  
plt.ylabel('Count')
plt.xlabel('Survey Responses, (0 = not at all, 10 = absolutely)')
plt.title('Distribution: ' + question)

q1 = np.mean(distribution)
q2 = np.median(distribution)
bench = 8.2

commercial_mean = np.mean(filtered_commercial)
operations_mean = np.mean(filtered_operations)
tech_mean = np.mean(filtered_tech)
product_mean = np.mean(filtered_product)

plt.axvline(x=q1, label="Mean", c = 'black', linestyle='--')
plt.axvline(x=q2, label="Median", c = 'gray', linestyle='--')
plt.axvline(x=bench, label="Benchmark", c = 'red', linestyle='--')

# Display the mean per area
#plt.axvline(x=commercial_mean, label="Commercial avg.", c = '#bf76b8ff')
#plt.axvline(x=operations_mean, label="Operations avg.", c = '#48ab6eff')
#plt.axvline(x=tech_mean, label="Tech avg.", c = '#59cdd4ff')
#plt.axvline(x=product_mean, label="Product avg.", c = '#ffa64cff')

y_ticks = np.arange(0, 20, 2)
plt.yticks(y_ticks)
plt.legend()

plt.show()

print('mean is: ' + str(q1))
print('median is: ' + str(q2))


# In[45]:


# Graph Boxplot

plt.figure(figsize=(16, 8))
ax = plt.subplot()

# Data
box = plt.boxplot([filtered_commercial, filtered_operations, filtered_tech, filtered_product], patch_artist=True)

# Colour 
colors = ['#bf76b8ff', '#48ab6eff', '#59cdd4ff', '#ffa64cff']
 
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# N count
n_commercial = len(filtered_commercial)
n_operations = len(filtered_operations)
n_tech = len(filtered_tech)
n_product = len(filtered_product)

# Labels
labels = ['Commercial '+ 'n='+str(n_commercial), 'Operations '+ 'n='+str(n_operations), 'Tech '+ 'n='+str(n_tech), 'Product '+ 'n='+str(n_product)]

x = [1, 2, 3, 4]
plt.ylabel('Survey Responses (0 = not at all, 10 = absolutely)')
plt.xlabel('Areas')
plt.xticks(x, labels)

plt.title('Boxplot: ' + question)

