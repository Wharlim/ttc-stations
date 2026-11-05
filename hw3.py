def main():
    totals = [] # this should be mt not zero 
    infile = open("stations-2017.csv")
    print(infile)
    header = infile.readline()
    for line in infile:
        line = line.removesuffix("\n")
        row = line.split(",")
        total = int(row[4])
        totals.append(total)
    to_platform_riders = []

    infile = open("stations-2017.csv") # needs to open file again
    header = infile.readline()
    for line in infile: 
        line = line.removesuffix("\n")
        row = line.split(",")
        to_platform = float(row[2]) # must do float cast instead of int cast
        to_platform_riders.append(to_platform)
    infile.close()

    print("Stations:", len(totals))
    print("Three largest totals:",sorted (totals[-3:]) ) # should just be [-3:]
    print("Average total:", sum(totals) / len(totals))
    print("Average to platform:", sum(to_platform_riders) / len(to_platform_riders))
    

if __name__ == "__main__":
    main()
