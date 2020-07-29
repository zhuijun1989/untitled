import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index,column_header in enumerate(header_row):
        print(index,column_header)

    highs = []
    for row in reader:
        highs.append(row[1])
    print(highs)

    fig = plt.figure(dpi=128,figsize=(8,6))
    plt.plot(highs,c='red')

    plt.title('Daily high temperatures,July 2014',fontsize=12)
    plt.xlabel('date',fontsize= 16)
    plt.ylabel('temperature(F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()


