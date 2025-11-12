import pandas as pd
import os
import csv

path = 'Thuy_crop_data(final_data)'
ann = pd.read_csv('added_annotation.csv')
classnames = pd.read_csv('class_names.csv')
#print(ann)

print(classnames)
makes = os.listdir(path)
carname = []
for make in makes:
    models = os.listdir(path + '/' + make)
    for model in models:
        carname.append(make + ' ' + model)
carnamefix = []
#print(carname)
for car in carname: 
    for row in ann.itertuples():
        #print(car)
        #print(row.model)
        if car == row.model: 
            car = car + ' ' + row.type
    carnamefix.append(car)

def sort_csv_column(input_path, output_path="sorted_output.csv"):
    """
    Read a one-column CSV file, sort the strings alphabetically,
    and write the sorted results into a new CSV file.

    Parameters:
        input_path (str): Path to the input CSV file.
        output_path (str): Path to save the sorted CSV file.
    """
    with open(input_path, mode="r", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        #header = next(reader)  # Read the header
        data = [row[0] for row in reader if row]  # Read all strings
    print(data)
    # Sort alphabetically (case-insensitive)
    data.sort(key=str.lower)

    # Write to new CSV
    with open(output_path, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        #writer.writerow(header)  # Write header back
        for item in data:
            writer.writerow([item])

    print(f"✅ Sorted CSV saved to '{output_path}'")

def list_to_csv(data_list, output_path="output.csv", column_name="Data"):
    """
    Convert a list of strings into a CSV file with one column.

    Parameters:
        data_list (list of str): List of strings to write into the CSV.
        output_path (str): Path to save the CSV file.
        column_name (str): Name of the column header.
    """
    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow([column_name])
        # Write each string as a new row
        for item in data_list:
            writer.writerow([item])
    print(f"✅ CSV file successfully saved to '{output_path}'")

#print(carnamefix)
#list_to_csv(carnamefix, "name.csv", column_name="Carmodel")
#sort_csv_column("class_names.csv", "sorted_names.csv")
with open("newannotation.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in ann.itertuples():
            list = []
            for classname in classnames.itertuples():
                fullmodel = row.model + ' ' + row.type
        #print(fullmodel + classname.make)
                if fullmodel == classname.make:
                    list.append(0)
                    list.append(0)
                    list.append(0)
                    list.append(0)
                    list.append(classname.Index + 1)
                    list.append(row.image_id + '.jpg')
            writer.writerow(list)
            
    #print(list)
            
    #print(f"✅ CSV file successfully saved to '{output_path}'")
