from weather import Weather

weather = Weather("Paris")
weather.set_weather(27,"Sunny")
weather.display_weather()

import csv
from customer import Customer

with open('customers.csv', 'r') as customers_file:
    customers = csv.reader(customers_file)
    
    for customer in customers:
       id = customer[0]
       first_name = customer[2]
       last_name = customer[3]
       email = customer[9]
       print(f"Customer #{id}, {first_name} {last_name}, {email}")

       customer_object = Customer(customer[0], customer[2], customer[3], customer[9])
       print(customer_object.description())

import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2,1)

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

ax1.plot(years, temp_anomalies, color='r', alpha=0.5, marker="o", linestyle="-")
ax1.set_title('Global Temperature Anomalies')
ax1.set_ylabel("Temperature Anomaly (in C)")
ax1.set_xlabel("Year")
ax1.set_xticks(years)
ax1.grid(True)

ax2.bar(years, co2_emissions, color='g', alpha=0.5)
ax2.set_title("Global CO2 Emissions")
ax2.set_ylabel('co2_emissions (billions of metric tons)')
ax2.set_xlabel("Year")
ax2.set_xticks(years)
ax2.grid(True)

plt.tight_layout()
plt.savefig("output.png", dpi=300)
plt.show()


import csv
import matplotlib.pyplot as plt

def generate_population_dictionary_from_csv(filename):
  """ 
  generate population diction from csv data

  return a dictionary follow this structure:
  {
  "Africa": { population: [100, 200, 300], years: [1990, 2000, 2010]},
  "Asia": { population:[100, 200, 300], years: [1990, 2000, 2012]}
  }
  """
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

def generate_population_plots_from_dictionary(population_dictionary):
  
  for continent in population_dictionary:
    years = population_dictionary[continent]['years']
    population = population_dictionary[continent]['population']
    plt.plot(years, population, label=continent, marker="o", alpha=0.5)

  plt.title("Internet Population per continent")
  plt.xlabel("Year")
  plt.ylabel("Internet users")
  plt.grid(True)
  plt.legend()
  plt.show()
  
filename = 'data.csv'

population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)
