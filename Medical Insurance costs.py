""" Medical insurance costs. Code project. """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



us_insurance_df = pd.read_csv(r"X:\Git HUB\US-Medical-Insurance-costs\insurance.csv") 

"""Tasks:
    1) Find out the average age of the patients in the dataset.
    2) Analyze where a majority of the individuals are from.
    3) Averege costs between smokers vs. non-smokers.
    4) Male female isurace costs on averege
    5) Figure out what the average age is for someone who has at least one child in this dataset.
    6) How number of children correlates with smoking for males and females
    7) Split the data for male/ female and see price difference for each changing atribute (BMI - below and above averege, smoker/non-smokers, children/no children)
    """
    
    
# 1) Find out the average age of the patients in the dataset.    
avg_age = us_insurance_df['age'].mean()


# 2) Analyze where a majority of the individuals are from.

region_count = us_insurance_df['region'].value_counts()
##### We see the exact values for each region

order = us_insurance_df['region'].value_counts().index
plt.title('Location analisys')
sns.countplot( data = us_insurance_df, x= 'region', order=order)
plt.xlabel('Regions')
plt.ylabel('Number of entries')
plt.show()


# 3) Corelation of smoking indvalues with other

smokers_av_all = us_insurance_df.groupby('smoker').mean()
print(smokers_av_all)
##### Here we see that the only corelation of the smoking factor are charges.And a verry small one in ages



sns.lmplot(x="age", y="charges", hue="smoker", data = us_insurance_df)
plt.title('Smokers vs insurance cost')
plt.xlabel('Ages')
plt.ylabel('Insurance cost')
plt.show()


# 4) Male female isurace costs on averege
#Taking a look at all the means grouped by gender
gender_av_all = us_insurance_df.groupby('sex').mean()
print(gender_av_all)
#As we can see there is a light difference in insurance costs

sns.barplot(x="sex", y="charges", data = us_insurance_df)
plt.title('Sex vs insurance cost')
plt.xlabel('Ages')
plt.ylabel('Insurance cost')
plt.show()

# 5) What is the average age is for someone who has at least one child in this dataset.

min_one_child = us_insurance_df[us_insurance_df['children']>0]
avg_age_min_one = min_one_child['age'].mean()

### Here there is no corelation between age and number of children as the values are almost eaxactly the same.


# 6)How number of children correlates influences insurance costs

sns.barplot(x="children", y="charges", data = us_insurance_df)
plt.title('Number of chldren vs insurance cost')
plt.xlabel('Number of children')
plt.ylabel('Insurance cost')
plt.show()

#### As we can see the number of children does not influence the insurance cost as there is no trend. 

# 7) Create a new Class to filter for our DataFrame to retrieve exact data. ### InsuranceDataFilter.py

from InsuranceDataFilter import InsuranceDataFilter 



 

