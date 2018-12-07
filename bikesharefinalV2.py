import time
import pandas as pd
import numpy as np

# Dictionray for cities
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Dict for months
MONTH_DATA = { 'january': 1,
              'february': 2,
              'march': 3,
              'april': 4,
              'may': 5,
              'june': 6}

#Dict for days of the week
DAY_DATA = { 'monday': 0,
              'tuesday': 1,
              'wednesday': 2,
              'thursday': 3,
              'friday': 4,
              'saturday': 5,
              'sunday': 6}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    #asks for user input in order to determine the city dataset
    def city_choice():
        city = input("Please choose the city you want to inquire about by entering Chicago, New York City or Washington \n\n").lower()
        if city == "chicago" or city == "new york city" or city == "washington":
            print("You have chosen: " + city + " We will now explore the data for the city of your choice \n")
            return city
        else:
            print("The city you have chosen is not available. \n Please chose again.\n\n")
            return city_choice()


    # TO DO: get user input for month (all, january, february, ... , june)

    #asks the user for input to determine the month used in the analysis. The month is then compared to the dict to get the month number
    def month_choice():
        month = input("Please choose the month you want to inquire about by entering the month's name or type in all. \n\n").lower()
        if month == "january" or month == "february" or month == "march" or month == "april" or month == "may" or month == "june":
            print("You have chosen: " + month + " We will now explore the data for the month of your choice \n")
            month = MONTH_DATA[month.lower()]
            return month
        elif month == "all":
            print("You have chosen: " + month + " We will now explore the data for the month of your choice \n")
            return month
        else:
            print("The month you have chosen is not available. \n Please chose again.\n\n")
            return month_choice()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    #asks the user for input about the day and then compares raw input to the day dict to determine the quantitative equivalent
    def day_choice():
        day = input("Please choose the day you want to inquire about by entering the day's name or typing all. \n\n").lower()
        if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday" or day == "sunday":
            print("You have chosen: " + day + " We will now explore the data for the month of your choice \n")
            day = DAY_DATA[day.lower()]
            return day
        elif day == "all":
            print("You have chosen: " + day + " We will now explore the data for the day of your choice \n")
            return day
        else:
            print("The day you have chosen is not available. \n Please chose again.\n\n")
            return day_choice()

    city = city_choice()
    month = month_choice()
    day = day_choice()

    print('-'*40)
    return city, month, day

#loads the data from previous choices into the dataframe and creates additional columns for easier calculations depending on user input
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.dayofweek
    df['month'] = df['Start Time'].dt.month
    if month != "all":
        df = df[df['month'] == month]
    if day != "all":
        df = df[df['day'] == day]
    return df

#prints out time statistics from the df established earlier by user inputs
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['month'] = df['Start Time'].dt.month
    most_common_month_num = df['month'].mode()[0]
    most_common_month = MONTHS[most_common_month_num - 1]
    print("The number of the most popular month is " + str(most_common_month))

    # TO DO: display the most common day of week
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    popular_day = df['day'].mode()[0]
    print("The most popular start day is " + weekdays[int(popular_day)])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular start hour is " + str(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#prints out stations statistics from the df established earlier by user inputs
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station_start = df['Start Station'].mode()[0]
    print("The most popular start station is: " + popular_station_start)
    print("too few datapoints to calculate the most common station")

    # TO DO: display most commonly used end station
    popular_station_end = df['End Station'].mode()[0]
    print("The most popular end station is: " + popular_station_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['startstop'] = df['Start Station'].str.cat(df['End Station'], sep=' and ')
    bothstations = df['startstop'].mode()[0]
    print("The most frequent combination of the start and end station are: " + bothstations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#prints out trip duration statistics from the df established earlier by user inputs
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_min = total_travel_time/60
    total_travel_time_hr = total_travel_time/60/60
    total_travel_time_days = total_travel_time_hr/24
    print("The total travel time for the period selected is " + str(total_travel_time_min) + " minutes, or " + str(total_travel_time_hr) + " hours, or " +          str(total_travel_time_days) + " days." )

    # TO DO: display mean travel time
    trip_duration_sec = df['Trip Duration'].mean()
    trip_duration_min = trip_duration_sec/60
    print("The average trip duration is " +str(trip_duration_sec) + " Seconds or " + str(trip_duration_min) + " minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#prints out user statistics from the df established earlier by user inputs
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\n The bikesharing system has the following user split: \n")
    print(user_types)

    #TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print("\n The bikesharing system has the following gender split: \n")
        print(gender_types)
    except:
        print("Unfortunateley gender data is not available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
        try:
            birth_max = int(df['Birth Year'].max())
            birth_min = int(df['Birth Year'].min())
            birth_mode = int(df['Birth Year'].mode())
            print("The most recent birth year of the system user is: {}.".format(birth_max))
            print("The earliest birth year of the system user is: {}.".format(birth_min))
            print("The most common birth year of the system user is: {}.".format(birth_mode))
        except:
            print("Unfortunateley birth data is not available for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#prompts the user if he wants to see the raw data at the end of the program
def raw_data(df):
    print("Here is the header for each column of the data you filtered for. \n\n ")
    print(df.head())

    answer = input(" \n\n Would you like to see the raw data for which you filtered? Enter Yes or no. \n\n").lower()
    if answer == "yes":
        print(df)
    elif answer == "no":
        print("Great, thanks for taking part!")
    else:
        raw_data(df)

#Main function that runs the previous fuctions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
