import pandas as pd
import matplotlib.pyplot as plt 

try:
    df = pd.read_csv("./data/kpi_report.csv")

    plt.bar(df.index, df["total_sales"])
    plt.xlabel("KPI")
    plt.ylabel("Value")
    plt.title("KPI Report")
    plt.savefig("./data/kpi_report.png") 
    plt.show()

except FileNotFoundError:
    print("Error: kpi_report.csv not found. Make sure the file exists and the path is correct.")
except Exception as e:
    print(f"An error occurred: {e}")
