import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(countries):
    df_list = []
    for country in countries:
        file_path = f"./data/{country.lower().replace(' ', '_')}_clean.csv"
        df = pd.read_csv(file_path)
        print(df.columns)
        df["Country"] = country
        df_list.append(df)
    return pd.concat(df_list, ignore_index=True)

def plot_ghi_boxplot(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Country", y="GHI", ax=ax)
    ax.set_title("GHI Distribution by Country")
    return fig

# def top_regions_table(df):
#     return df.groupby(["Country", "Region"])["GHI"].mean().reset_index().sort_values(by="GHI", ascending=False).head(10)