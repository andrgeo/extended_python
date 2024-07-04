import pandas
import csv

in_file = 'zip_codes_states.csv'
zip = 682

with open(in_file, 'r') as csvfile:
    zip_reader = pandas.read_csv(csvfile)
    df = pandas.DataFrame(zip_reader)
    idx = df[df['zip_code'] == zip].index
    zip = df.at[idx[0], "zip_code"]
    city = df.at[idx[0], "city"]
    state = df.at[idx[0], "state"]
    latitude = df.at[idx[0], "latitude"]

    print(fr'ZIP Code {zip} is in {city}, {state}, Rensselaer county, coordinates: {latitude}')