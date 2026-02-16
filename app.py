from flask import Flask, send_file
import os
import csv
import matplotlib


matplotlib.use('Agg')

import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from my Python app on Render 🚀"


@app.route('/climate')
def climate_chart():

    fig, (ax1, ax2) = plt.subplots(2, 1)

    years = [2000, 2005, 2010, 2015, 2020]
    temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]
    co2_emissions = [25, 30, 35, 40, 45]

    ax1.plot(years, temp_anomalies, marker="o")
    ax1.set_title('Global Temperature Anomalies')
    ax1.set_ylabel("Temperature Anomaly (°C)")
    ax1.set_xlabel("Year")
    ax1.grid(True)

    ax2.bar(years, co2_emissions)
    ax2.set_title("Global CO2 Emissions")
    ax2.set_ylabel("CO2 Emissions (billion metric tons)")
    ax2.set_xlabel("Year")
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig("climate.png")
    plt.close()

    return send_file("climate.png", mimetype='image/png')


def generate_population_dictionary_from_csv(filename):
    output = {}

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])

            if continent not in output:
                output[continent] = {'population': [], 'years': []}

            output[continent]['population'].append(population)
            output[continent]['years'].append(year)

    return output


@app.route('/population')
def population_chart():

    filename = 'data.csv'
    population_dictionary = generate_population_dictionary_from_csv(filename)

    for continent in population_dictionary:
        years = population_dictionary[continent]['years']
        population = population_dictionary[continent]['population']
        plt.plot(years, population, label=continent, marker="o")

    plt.title("Internet Population per Continent")
    plt.xlabel("Year")
    plt.ylabel("Internet Users")
    plt.grid(True)
    plt.legend()

    plt.savefig("population.png")
    plt.close()

    return send_file("population.png", mimetype='image/png')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
