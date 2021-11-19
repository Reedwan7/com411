import matplotlib.pyplot as plt
print("\n")
def read_data(file_path):
    temps = []
    with open(file_path) as file:
        for line in file:
            temps.append(float(line.strip()))
    return temps
print ("\n")
def run():







