from NbiaConnector import NbiaConnector
nbiaDao = NbiaConnector("johan_van_soest", "xxxx")
petal_csv = nbiaDao.getSeriesCsv("PETRA_PETAL")
nbiaDao.logout()

#write output to file
file = open('petal.csv', 'w')
file.write(petal_csv)
file.close()