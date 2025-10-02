import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        data = pd.read_csv(file_path, parse_dates=['Date'])
        print("Data Lpaded Succesfully")
        return data
    except Exception as e:
        print("Error data loaded", e)
        return None
    
def plot_temperature(data, save_file=None):
    data["7-Day Average"] = data["Temperature"].rolling(window=7).mean()

    mean_temp = data["Temperature"].mean()
    std_temp = data["Temperature"].std()
    data["Anomaly"] = (data["Temperature"] > mean_temp + 2 * std_temp) | (data["Temperature"] < mean_temp - 2 * std_temp)

    plt.style.use("seaborn-v0_8-dark")
    plt.figure(figsize=(14, 7))
    plt.plot(data["Date"], data["Temperature"], label="Daily Temperature", color="blue", alpha=0.5)
    plt.plot(data["Date"], data["7-Day Average"], label="7-Day Average", color="orange", linewidth=2)
    plt.scatter(data.loc[data["Anomaly"], "Date"], data.loc[data["Anomaly"], "Temperature"], color="red", label="Anomalies", zorder=5)
    plt.title("Temperature Trends")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    if save_file:
        plt.savefig(save_file)
        print(f"Plot saved as {save_file}")
    else:
        plt.show()

def main():
    print("Welcome to the Temperature plotter!")

    file_path = input("Enter the path to the temperature data CSV file: ")
    data = load_data(file_path)
    if data is None:
        return
    
    save_choice = input("Do you want to save the plot as a file? (yes/no): ").lower()
    if save_choice == 'yes':
        file_name = input("Enter the filename to save the plot (e.g., temperature_plot.png): ")
        plot_temperature(data, save_file=file_name)
    else:
        plot_temperature(data)

if __name__ == "__main__":  
    main()