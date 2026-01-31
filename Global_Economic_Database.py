import os
import pandas as pd
import matplotlib.pyplot as plt
import wikipediaapi

#FUNCTIONSA
def display_menu(): #formatted menu function
    return input(("=" * 40) + "\n" + ("=" * 3)
      + "   Country Information Database   " 
      + ("=" * 3) +  "\n" + ("=" * 40) + "\n"
      + "= q ---> Retreive countr(y/ies) data   =\n"
      + "= i ---> Retrieve country information  =\n"
      + "= a ---> Add/Update country            =\n"
      + "= r ---> Remove country                =\n"
      + "= d ---> Directory                     =\n"
      + "= x ---> Exit Program                  =\n"
      + ("=" * 40) + "\nSelect an operation:\n---> ")

def readData(file,countries,metrics):
    df = pd.read_csv(file) #open and read file using pandas
    df = df.set_index("Country") #changes index to coutnry so you can index by label
    if countries == [""] and metrics != [""]: #allows user to press enter for all
        countries = df.index.to_list()
        print(df.loc[countries,metrics])
    elif countries != [""] and metrics == [""]:
        metrics = df.columns.to_list()
        print(df.loc[countries,metrics])
    elif countries != [""] and metrics != [""]:
        print(df.loc[countries,metrics])
    else:
        print(df)
    graph = input("\nWould you like a graph? (y/n)\n---> ") #optional graph based on dataframe
    if graph == "y": # print to file, add logic to save as png in paint
        df.loc[countries,metrics].plot(kind="bar")
        plt.savefig("chart.png")
        os.system("mspaint.exe chart.png")
    elif graph == "n":
        pass
    else:
        print(("=" * 40) + "\nThere was an error, Please try again.")

def wiki_search(subject):
    wiki = wikipediaapi.Wikipedia('Testing', 'en')
    page = wiki.page(subject)
    print("=" * 40)
    print (page.exists())
    print (page.summary[0:200])

def add_record(file,country,data): #do I need to specify to enter at the end?
    df = pd.read_csv(file)
    df = df.set_index("Country")
    df.loc[country] = data #add new record based on user input
    df = df.reset_index()
    df.to_csv(file, index=False) #saves data frame to original file to disc

def remove_record(file, country):
    df = pd.read_csv(file)
    df = df.set_index("Country")
    df = df.drop(country, axis = 0) #removes a row
    df = df.reset_index() # resets index to numerical index so that it doesnt cut off country label when re writing file
    df.to_csv(file, index=False) # re writes data to file from dataframe
    print(f"Removed: {country}")

def directory(file):
    df = pd.read_csv(file) 
    df = df.set_index("Country") #sets index to country label and the turns that index into a list for the directory
    countries = df.index.to_list()
    return countries

def goodbye():
    print(("=" * 40) + "\n" + ("=" * 3)
        + (" " * 12) + "Thank you," + (" " * 12)
        + ("=" * 3) + "\n" + ("=" * 3)
        + (" " * 13) + "Goodbye!" + (" " * 13)
        + ("=" * 3) + "\n" + ("=" * 40))

def string_2_int(list):
    for i in range(len(list)): #changes input type from list of strings to ints so you can update existing records
            list[i] = int(list[i])
    return list


#PROGRAM
while True:
    os.system("cls")
    banner = "=" * 40
    filename = "CountryData.csv"
    choice = display_menu()
    try: 
        if choice == "q": #KeyError
            countries = []
            metrics = []
            countries = input(banner + "\n" + ("=" * 3) 
                            + " Seperate each input with a comma ===\n" + ("=" * 3)
                            + (" " * 7) + "Select enter for all" + (" " * 7) + ("=" * 3)
                            + "\n" + banner + "\nCountries: ").split(",") #Can I use get?
            print(banner + "\n" + (" " * 16) + "Options" + (" " * 16)
                + "\n" + "\n" + "  GDP, Population, Debt, Unemployment,"
                + "\n Literacy, TradeBal Interest, Inflation \n" + banner)
            metrics = input("Metrics: ").split(",")
            #print(banner)
            readData(filename,countries,metrics)
        elif choice == "i":
            country = input(banner + "\nCountry: ")
            wiki_search(country)
        elif choice == "a":
            data = []
            addition = input(banner + "\nCountry: ")
            data = input("Data: ").split(",")
            string_2_int(data)
            if len(data) == 8:
                add_record(filename,addition,data)
            else:
                print("Can only take 8 values") 
        elif choice == "r":
            removed = input(banner + "\nEnter the country you want to remove:\n---> ") 
            remove_record(filename,removed)
        elif choice == "d":
            print(banner)
            print(directory(filename))
        elif choice == "x":
            goodbye()
            exit()
        else:
            print(banner + "\nThere was an error, Please try again.")
    except KeyError:
        print(banner + "\nThere was an error, Please try again.")

    leave = input(banner + "\nPress enter to continue: ") #maybe make this a function
    if leave == "":
        continue
    else:
        break
        
