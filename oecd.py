import pandas as pd

url = (
    "https://sdmx.oecd.org/sti-public/rest/data/"
    "OECD.STI.PIE,DSD_TIVA_MAINLV@DF_MAINLV/"
    "FFD_DVA.AUS..W..A"
    "?startPeriod=2015"
    "&endPeriod=2015"
    "&dimensionAtObservation=AllDimensions"
    "&format=csvfilewithlabels"
)

df = pd.read_csv(url)
print(df.head())
print(df.columns)
