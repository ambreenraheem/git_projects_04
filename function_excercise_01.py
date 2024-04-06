population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}
def add():# Function to add country and population
    country=input("Enter country name to add:") # Get country name
    country=country.lower() # Convert to lowercase
    #check i country already exists
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    # get population for country
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()
    # function to remove a country
def remove():
    country = input("Enter country name to remove:")
    country = country.lower() # convert the lowercase
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country] # delete the country
    print_all() #print updated list
    # function to query population of a country
def query():
    country = input("Enter country name to query:")
    country = country.lower() # convert to lowercase
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore") #print population
    # function to print population
def print_all():
        #loop through population dictionary
    for country, p in population.items():
        #print country and its population
        print(f"{country}==>{p}")
    # function to handle user input    
def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add': # if add operation
        add() # call add function
    elif op.lower() == 'remove': # if remove function
        remove() # call remove function
    elif op.lower() == 'query': #if query function
        query() # call query function
    elif op.lower() == 'print': #if print operation
        print_all() # call print_all function

if __name__ == '__main__':
    main()