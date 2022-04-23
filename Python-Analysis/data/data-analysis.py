#import the libary for data analysis
import pandas as pd
import matplotlib.pyplot as plt

#title of data analysis and other functions
plt.title("Analisi contagi Covid Dicembre 2020/21")
plt.xlabel("Giorno del rilevamento")
plt.ylabel("Numero di contagiati")

#read csv file
dati2021 = pd.read_csv('DatiCovid2021.csv')
dati2020 = pd.read_csv('DatiCovid2020.csv')

#show data results
plt.plot(dati2021.data, dati2021.numero_contagi, label = "dati 2021 (nessuna restrizione)", color = 'r')
plt.plot(dati2020.data, dati2020.numero_contagi, label = "dati 2020 (con restrizioni)", color = 'b')
plt.legend(loc = "upper left")
plt.grid(True)
plt.show()
