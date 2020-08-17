import glob
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class HappyAnalysis:

    def __init__(self,df2015,df2016,df2017,df2018,df2019,path,dfc):
        self.path =path
        self.dfc =dfc
        self.df2015= df2015
        self.df2016= df2016
        self.df2017= df2017
        self.df2018= df2018
        self.df2019= df2019

    def cleanFunction(self):
        #cleaning df2015
        df1=self.df2015.drop(['Region','Standard Error','Dystopia Residual'],axis=1)
        df1.rename(
            columns={'Health (Life Expectancy)':'Life Expectancy','Family': 'Social Support', 'Economy (GDP per Capita)': 'GDP per Capita',
                     'Trust (Government Corruption)':'Perceptions of corruption'}
            , inplace=True)
        df1['Year'] ='2015'
        df1 = df1[['Country','Happiness Rank','Happiness Score','GDP per Capita','Social Support',
                   'Life Expectancy','Freedom','Perceptions of corruption','Generosity','Year']]
        df1.to_csv('/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1/2015new.csv', index=False)
        df2=self.df2016.drop(['Region','Lower Confidence Interval','Upper Confidence Interval','Dystopia Residual'],axis=1)
        df2.rename(columns={'Economy (GDP per Capita)': 'GDP per Capita','Health (Life Expectancy)':'Life Expectancy','Family': 'Social Support',
                            'Trust (Government Corruption)':'Perceptions of corruption'}
                   ,inplace=True)
        df2['Year'] = '2016'
        df2 = df2[
            ['Country', 'Happiness Rank', 'Happiness Score', 'GDP per Capita', 'Social Support', 'Life Expectancy',
             'Freedom', 'Perceptions of corruption', 'Generosity', 'Year']]
        df2.to_csv('/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1/2016new.csv', index=False)
        df3=self.df2017.drop(['Whisker.high','Whisker.low','Dystopia.Residual'],axis=1)
        df3.rename(columns={'Happiness.Rank':'Happiness Rank','Happiness.Score':'Happiness Score','Economy..GDP.per.Capita.':'GDP per Capita',
                            'Family':'Social Support','Health..Life.Expectancy.':'Life Expectancy','Trust..Government.Corruption.':'Perceptions of corruption'}
                   ,inplace=True)
        df3['Year'] = '2017'
        df3 = df3[
            ['Country', 'Happiness Rank', 'Happiness Score', 'GDP per Capita', 'Social Support', 'Life Expectancy',
             'Freedom', 'Perceptions of corruption', 'Generosity', 'Year']]
        df3.to_csv('/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1/2017new.csv', index=False)
        self.df2018.rename(
            columns={'GDP per capita':'GDP per Capita','Overall rank': 'Happiness Rank', 'Country or region': 'Country', 'Score': 'Happiness Score',
                     'Healthy life expectancy': 'Life Expectancy', 'Freedom to make life choices': 'Freedom','Social support':'Social Support'},
            inplace=True)
        self.df2018['Year']= '2018'
        self.df2018.to_csv('/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1/2018new.csv', index=False)

        self.df2019.rename(
            columns={'GDP per capita':'GDP per Capita','Overall rank': 'Happiness Rank', 'Country or region': 'Country', 'Score': 'Happiness Score',
                     'Healthy life expectancy': 'Life Expectancy', 'Freedom to make life choices': 'Freedom','Social support':'Social Support'},
            inplace=True)
        self.df2019['Year'] = '2019'
        self.df2019.to_csv('/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1/2019new.csv', index=False)



    def mergeFunction(self):
        filenames = glob.glob(self.path + "/*.csv")
        dfs = []
        for filename in filenames:
            dfs.append(pd.read_csv(filename))
        ConsolidatedDF = pd.concat(dfs, ignore_index=True)
        ConsolidatedDF.round(
            {'Happiness Score': 2, 'GDP per Capita': 2, 'Social Support': 2, 'Life Expectancy': 2, 'Freedom': 2,
             'Perceptions of corruption': 2, 'Generosity': 2})
        ConsolidatedDF.to_csv('/Users/aakash/PycharmProjects/WorldHappiness/CombinedData.csv', index=False)

    def eda(self):
        print(self.dfc.info())
        # #Understanding the relation between different columns using pairplot
        # sns.pairplot(self.dfc,hue='Year',palette='magma')
        # # plt.show()
        # plt.savefig('/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1/Pairplot.pdf')
        #
        # #This will show the countries most present in the dataset
        data_country = self.dfc['Country'].value_counts()
        data_rvalues = data_country.values
        data_country1 =  data_country.index
        plt.figure(figsize=(30, 30))
        sns.barplot(x=data_country1, y=data_rvalues, palette='magma')
        plt.xticks(rotation=90)
        plt.xlabel('Country')
        plt.ylabel('Values')
        plt.title('Country v/s Values')
        # plt.show()
        # plt.savefig('/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1/CountryvsValue.pdf')

        #Most Happy Country
        # plt.figure(figsize=(10, 10))
        # sns.barplot(x=data_country1, y=data_rvalues, palette=sns.cubehelix_palette(len(data_country1)))
        # plt.xlabel('Countries')
        # plt.ylabel('Values')
        # plt.xticks(rotation=90)
        # plt.title('Most Common Region of Happy')
        # plt.show()

        plt.figure(figsize=(10, 10))
        plt.scatter(self.dfc['GDP per Capita'], self.dfc['Freedom'], s=(self.dfc['Happiness Score'] ** 3), alpha=0.5)
        plt.grid(True)

        plt.xlabel("Economy")
        plt.ylabel("Freedom")

        plt.suptitle("Health Economy graph with sizes as Happiness score and colors as Region", fontsize=18)

        plt.show()
        plt.savefig('/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1/EcoFree.pdf')
if __name__ == "__main__":
    e= HappyAnalysis(df2015= pd.read_csv(r'/Users/aakash/PycharmProjects/WorldHappiness/Input/2015.csv'),
                     df2016= pd.read_csv(r'/Users/aakash/PycharmProjects/WorldHappiness/Input/2016.csv'),
                     df2017= pd.read_csv(r'/Users/aakash/PycharmProjects/WorldHappiness/Input/2017.csv'),
                     df2018= pd.read_csv(r'/Users/aakash/PycharmProjects/WorldHappiness/Input/2018.csv'),
                     df2019= pd.read_csv(r'/Users/aakash/PycharmProjects/WorldHappiness/Input/2019.csv')
                     ,path='/Users/aakash/PycharmProjects/WorldHappiness/Output.v.1'
                     ,dfc=pd.read_csv('/Users/aakash/PycharmProjects/WorldHappiness/CombinedData.csv'))
    # e.mergeFunction()
    # e.cleanFunction()
    e.eda()
