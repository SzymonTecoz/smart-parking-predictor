import pandas as pd
import numpy as np

def generating_parking_data(n_samples = 40000):
    np.random.seed(42)

    data = {
        "hour": np.random.randint(0, 24, n_samples),
        "day_of_the_week": np.random.randint(0, 7, n_samples),
        "temperature": np.random.normal(15, 10, n_samples),
        "rain": np.random.randint(0,2, n_samples),
        "location" :np.random.choice(["city_center", "office_area", "shopping_mall", "stadium"], n_samples),
        "event_nearby": np.random.randint(0,2,n_samples)
    }

    df = pd.DataFrame(data)

    probability = 0.6

    probability -= (df["hour"].between(17, 20)) * 0.35
    probability -= (df["location"] == "city_center") * 0.2
    probability -= (df["event_nearby"] == 1) * 0.25
    probability -= (df["rain"] == 1) * 0.1

    probability = np.clip(probability, 0.05, 0.95)

    df["parking_available"] = np.random.binomial(1, probability)

    return df

if __name__ == "__main__":
    df = generating_parking_data(40000)
    df.to_csv("data/parking_data.csv", index=False)

    print("Dataset generated.")
    print(df.head())