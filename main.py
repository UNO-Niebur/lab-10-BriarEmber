#MapPlot.py
#Name:Devyn Conaway
#Date:4/6/2026
#Assignment:Lab 10

import csv
import matplotlib.pyplot as plt

def main(): 
    x = []
    y = []

    with open("reaction_time_data.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            x.append(row[0])
            y.append(float(row[1]))

    plt.plot(x, y)

    plt.xlabel("Trial Number")
    plt.ylabel("Reaction Time (ms)")
    plt.title("Reaction Times in Trials")

    plt.savefig("datagraph.png")

if __name__ == "__main__":
    main()