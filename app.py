from flask import Flask, send_file
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def climate_chart():

    fig, (ax1, ax2) = plt.subplots(2, 1)

    years = [2000, 2005, 2010, 2015, 2020]
    temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]
    co2_emissions = [25, 30, 35, 40, 45]

    # 折线图
    ax1.plot(years, temp_anomalies, marker="o")
    ax1.set_title('Global Temperature Anomalies')
    ax1.set_ylabel("Temperature Anomaly (°C)")
    ax1.set_xlabel("Year")
    ax1.grid(True)

    # 柱状图
    ax2.bar(years, co2_emissions)
    ax2.set_title("Global CO2 Emissions")
    ax2.set_ylabel("CO2 Emissions (billion metric tons)")
    ax2.set_xlabel("Year")
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig("output.png")
    plt.close()

    return send_file("output.png", mimetype='image/png')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)




