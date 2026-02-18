from flask import Flask, send_file
import os
import io

import matplotlib
matplotlib.use("Agg")   

import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")

def climate_chart():

    years = [2000, 2005, 2010, 2015, 2020]
    temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]
    co2_emissions = [25, 30, 35, 40, 45]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

    ax1.plot(years, temp_anomalies, marker="o")
    ax1.set_title("Global Temperature Anomalies")
    ax1.set_ylabel("Temperature (°C)")
    ax1.grid(True)

    ax2.bar(years, co2_emissions)
    ax2.set_title("Global CO2 Emissions")
    ax2.set_ylabel("CO2 (billion tons)")
    ax2.grid(True)

    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close(fig)

    return send_file(img, mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
