import os, glob, csv

def load_sensor_data():
    sensor_date = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))

    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')