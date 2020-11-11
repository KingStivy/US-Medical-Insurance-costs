# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:31:05 2020

@author: Stefan Hincu
"""
print('Imported')
class InsuranceDataFilter:
    def __init__(self,data_frame):
        self.df = data_frame
        
        
    def  filter_age(self,age):
        """ Filters all rows matching inputed age """
        self.age = age
        self.df = self.df[self.df["age"] == self.age]
        return self.df
   
    def filter_sex(self, sex):
        """ Filters all rows matching inputed sex """
        self.sex = sex
        self.df = self.df[self.df["sex"] == self.sex]
        return self.df

    def filter_bmi_range(self,bmi1, bmi2):
        """Filters all matching row in the dataframe between first and second BMI input."""
        self.bmi1 = bmi1
        self.bmi2 = bmi2
        self.df = self.df[(self.df["bmi"] >= self.bmi1) & (self.df["bmi"] <= self.bmi2)]
        return self.df
    
    def filter_nr_children(self, nr_children):
        """ Filters all rows matching inputed number of children """
        self.nr_children = nr_children
        self.df = self.df[self.df["children"] == self.nr_children]
        return self.df
    
    def filter_smoker(self, smoker_status):
        """ Filters all rows matching inputed smoker status """
        self.smoker_status = smoker_status
        self.df = self.df[self.df["smoker"] == self.smoker_status]
        return self.df
    
    def filter_region(self, region):
        """ Filters all rows matching inputed region """
        self.region = region
        self.df = self.df[self.df["region"] == self.region]
        return self.df
    
    def filter_charge_range(self, charge_range1, charge_range2):
        """Filters all matching row in the dataframe between first and second input."""
        self.charge1 = charge_range1
        self.charge2 = charge_range2
        self.df = self.df[(self.df["charges"] >= self.charge1) & (self.df["charges"] <= self.charge2)]
        return self.df
        
    def information(self):
        """Returns the averege for numerical and counts for non_numerical current columns in the object
        Varriables that can be extracted: .avg_age, .sex_m, .sex_f, .av_bmi, .av_chil, .no_smoker, .smoker, 
        .southeast, .southwest, .northeast, .northwest, .charges
        """
        
        self.avg_age = self.df['age'].mean()
        self.sex_m = self.df['sex'][self.df["sex"] == 'male'].count()
        self.sex_f = self.df['sex'][self.df["sex"] == 'female'].count()
        self.av_bmi = self.df['bmi'].mean()
        self.av_chil = self.df['children'].mean()
        self.no_smoker = self.df['smoker'][self.df["smoker"] == 'no'].count()
        self.smoker = self.df['smoker'][self.df["smoker"] == 'yes'].count()
        self.southeast = self.df['region'][self.df["region"] == 'southeast'].count()
        self.southwest = self.df['region'][self.df["region"] == 'southwest'].count()
        self.northeast = self.df['region'][self.df["region"] == 'northeast'].count()
        self.northwest = self.df['region'][self.df["region"] == 'northwest'].count()
        self.charges = self.df['charges'].mean()
        print()
        print('Information on current data frame')
        print()
        print(f'Individuals are {self.avg_age} years old on averege, there are {self.sex_m} males and {self.sex_f} females. Having {self.av_chil} children on averege')
        print(f'Averege body mass index is {self.av_bmi}, Smokers: {self.smoker}, Non_smokers: {self.no_smoker}.')
        print(f'Regions: 1) SouthEast - {self.southeast} entries. 2) SouthWest - {self.southwest} entries. 4) NorthEast - {self.northeast} entries. 4) NorthWest - {self.northwest} entries.' ) 
        print(f'Averege insurance cost is {self.charges}$') 
        
