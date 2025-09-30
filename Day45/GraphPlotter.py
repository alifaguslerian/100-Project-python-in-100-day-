import matplotlib.pyplot as plt
import pandas as pd

def plot_graph():
    print("Welcome to the graph potter")
    print("chose a graph type: ")
    print("1. Line Graph")
    print("2. bar chart")
    print("3. scatter plot")

    choice = input("Enter your choice (1/2/3): ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Please select 1, 2, or 3.")
        return
    
    print("Choose data input method:")
    print("1. enter data manually")
    print("2. read from a CSV file")
    data_choice = input("Enter your choice (1/2): ")

    if data_choice == "1":
        x = list(map(float, input("Enter x values separated by commas: ").split()))
        y = list(map(float, input("Enter y values separated by commas: ").split()))
    elif data_choice == "2":
        file_path = input("Enter the CSV file path: ")
        try:
            data = pd.read_csv(file_path)
            x = data.iloc[:, 0]
            y = data.iloc[:, 1]
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return
        
    else:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    if choice == "1":
        plt.plot(x, y, label="line graph", marker='o')
    elif choice == "2":    
        plt.bar(x, y, color="skyblue")
    elif choice == "3":
        plt.scatter(x, y, color="green")

    plt.title("graph plotter")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)

    save_choice = input("Do you want to save the graph? (y/n): ").lower()
    if save_choice == 'y':
        save_path = input("Enter the file name to save (with .png extension): ")
        plt.savefig(save_path)
        print(f"Graph saved as {save_path}")
    else:
        plt.show()

if __name__ == "__main__":
    plot_graph()

