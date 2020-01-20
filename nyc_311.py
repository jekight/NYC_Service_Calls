#import required libraries
import pandas as pd
import matplotlib.pyplot as plt


#set pandas dataframe display parameters
pd.set_option('display.width',5000)
pd.set_option('display.max_columns',60)
#set plot size for better viewing within the notebook
plt.rcParams['figure.figsize']=(15,7)

#Basic Data Analysis of 311 NYC Service Request Dataset

#import the 311 NYC service request dataset
complaints = pd.read_csv("311_Service_Requests_for_2009.csv", low_memory=False)

#view top 5 records
complaints.head()

#view first 5 complaint type using slicing technique
complaints['Complaint Type'][:5]

#view complaint type and city together
complaints[['Complaint Type','City']]

#view first 10 complaint type along with city
complaints[['Complaint Type','City']][0:10]

#view the data most complaint type
complaints['Complaint Type'].value_counts()

#Visual The Complaint Type

#create Complaint type count object to visualize complaint type data
complaint_count = complaints['Complaint Type'].value_counts()

#view top 10 complaint types
complaint_count[0:10]

#plot the top 10 complaint types
complaint_count[0:10].plot(kind='bar')
