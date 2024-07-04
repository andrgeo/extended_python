import pandas
import csv

in_file = 'zip_codes_states.csv'
zip = 682

def read_f ():
    with open(in_file, 'r') as csvfile:
        zip_reader = pandas.read_csv(csvfile)
        df = pandas.DataFrame(zip_reader)
        column_names = df.columns.tolist()
        idx = df[df['zip_code'] == zip].index
        zip = df.at[idx[0], "zip_code"]
        city = df.at[idx[0], "city"]
        state = df.at[idx[0], "state"]
        latitude = df.at[idx[0], "latitude"]
        longitude = df.at[idx[0], "longitude"]
        county = df.at[idx[0], "county"]

def loc():
    inp_loc = int(input("Enter a ZIP Code to lookup => "))

    return message

def zip():
    inp_city = input("Enter a city name to lookup => ")
    inp_state = input("Enter the state name to lookup => ")

    return message

def dist():
    first_zip = input("Enter the first ZIP Code => ")
    second_zip = input("Enter the second ZIP Code => ")

def end():
    pass