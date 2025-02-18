#%%
import warnings
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

class Model():
    """ 
    Cette classe crée la prediction à une date donnée ainsi que sa visualisation 

    :param debut: la date du debut de la prédiction 

    :type debut: Date dans le  format YYYY_MM_DD H:M:S

    :param fin: la date de la fin de la prédiction 
    
    :type fin: Date dans le  format YYYY_MM_DD H:M:S

    """
    def __init__(self,debut,fin,pred):
        self.debut=debut
        self.fin=fin
        self.pred=pred

    def mod(self,df):
        """ 
        Le modele de prédiction sur une période donnnée 

        :return: la dataframe de la prédiction ,dates de la période donnée et les valeurs correspondantes     
        
        :rtype: Data frame 
        
        """

        #df =data.Processdf(1).cleaningdf()#
        #np.asarray(df.iloc[70176:,])
        UCM = sm.tsa.UnobservedComponents(df,
                                            level='dtrend',
                                            irregular=True,
                                            stochastic_level=False,
                                            stochastic_trend=False,
                                            stochastic_freq_seasonal=[
                                                True, False, False],
                                            freq_seasonal=[{'period': 96, 'harmonics': 6},
                                                           {'period': 672,
                                                               'harmonics': 2},
                                                           {'period': 35066, 'harmonics': 1}])
        m=UCM.fit()
        self.pred=m.predict(start=self.debut,end=self.fin)
        self.pred = self.pred.to_frame()
        self.pred = self.pred - 5000
        return self.pred
    def ucmplot(self):
        """ 
        Visualisation de la consommation du jour à prédire

        :param pred: La prédiction d'une période donnée

        :type pred: data frame  

        """
        f, ax = plt.subplots(figsize=(18, 6), dpi=200)
        plt.suptitle('La consommation éléctrique  (MW) du 8 Décembre', fontsize=20)
        plt.ylabel('Consommation (MW) ')
        self.pred.plot(ax=ax, rot=90, ylabel='Consommation (MW)')
        plt.legend()
       
#%%
#start1="2022-12-08 00:00:00"
#end1="2022-12-08 23:45:00"
#df=data.Processdf(1).claeningdf()
#obj=Model(debut=start1,fin=end1,df=df)
#pred=obj.mod()

#_______ploter la pred des resources ____
#essayer d ajouter un id pour selectionner le plot qui co,nvient 
#manip de la data des resources 
# %%
