# Author: Lucia Floan
# Date: March 7, 2025
# Title: US_Population

# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    # Now have the user enter a year. 
    while True:
        year = int(input('Enter a year (or 0 to stop): '))
        if year == 0:
            break
            
        state = input ('Enter the state name: ')
        population = int(input('Enter the population: '))
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
        all_entered_values.append([year, state, population])

    year_to_sum = int(input('Enter the year of the population to sum: '))
    sum_population_for_year(all_entered_values, year_to_sum)

def sum_population_for_year(all_entered_values, year_to_sum):
    total_population = 0
    for data in all_entered_values:
        if data[0] == year_to_sum:
            total_population += data[2]
    print(f'Total population for {year_to_sum}: {total_population}')
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()
