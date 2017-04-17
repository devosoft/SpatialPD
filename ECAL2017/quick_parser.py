import glob

outfile = open("all_data.csv", "w")
file_list = glob.glob("data-*.csv") # grab all csv files that start with data-

header = ""

for filename in file_list: #loop over files
    split_name = filename[:-4] # Cut off file extension - assumes .csv
    split_name = split_name.split("/")[-1] # Cut off the rest of the filepath
    split_name = split_name.split("-") # split_name is now a list

    r = split_name[1]
    u = split_name[2]
    seed = split_name[6]

    datafile = open(filename, "r") # open file for reading
    data = datafile.readlines() # data is a list of all lines in the file 
    datafile.close()

    if header and header != data[0]: # just to be safe
        print("Warning! File headers do not match:", header, data[0])
    elif not header: # Only print header for first file
        header = data[0]
        outfile.write(header.strip() + ",r,u,seed\n")
    
    for line in data[1:]: # everything but the header
        outfile.write(",".join([line.strip(), r, u, seed]) + "\n")

outfile.close()

