import csv
import glob
# Full Name,First Name,Middle Name,Last Name,Match Date,Markers Tested,Genetic Distance,Big Y STR Differences,Y-DNA Haplogroup,Paternal Country of Origin,Earliest Known Ancestor,Notes
for file in glob.glob('*.csv'):
    with open(file, newline='', errors='backslashreplace',encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Full Name'], row['Earliest Known Ancestor'], row['Y-DNA Haplogroup'], row['Paternal Country of Origin'], sep=';')