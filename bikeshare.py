import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi! Almothana Is here Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Please type the name of the city you want :")
    print("Chicago")
    print("New York")
    print("Washington")

    print(" ")

    city = input()
    city = city.lower()
    #handling errors iv city
    while True:
        if city == "chicago":
            return 'chicago'
        elif city == "new york":
            return 'new york city'
        elif  city == "washington":
            return 'washington'
        else:
          print("Please type the name of the city you want :")
          city = input()
          city = city.lower()
    return city
def get_month():
    # get user input for month (all, january, february, ... , june)
    print("Please type the month you want :")
    print("Please choose a month: January, February, March, April, May, or June? if you want no filter type all")
    print(" ")
    #handling month input
    month = input()
    month = month.lower()
    months_list = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        if month in months_list or month == 'all':
            return month
    #handling errors
        else:
          print("Please choose a month: January, February, March, April, May, or June? if you want no filter type all")
          print(" ")
          month = input().lower()

def get_day():
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print("Please type the name or the numper of the city you want :")
    print(" ")
    print("Please choose a day:'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', or all")
    #handilng input
    days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input()
    day = day.lower()

    while True:
        if day in days_list or day == 'all':
            print('Please wait '*5)
            return day
    #handilng errors
        else:
          print(" ")
          print("Please choose a day:'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', or all")
          day = input().lower()



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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the date column to datetime to make the code faster
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]
    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def display_raw_data(df):

    #drop columns that i created before from visualization
    df = df.drop(['month', 'day_of_week', 'hour'], axis = 1)
    row_data = 0
    display_data = input("\nDo you like to see rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()
    while True:
        if display_data == 'yes':
            print(df[row_data: row_data + 5])
            row_data = row_data + 5
            display_data = input("\n Do you like to see more of it? Please write 'yes' or 'no' \n").lower()
        if display_data == 'no':
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    try:
       popular_month = df['month'].mode()[0]
       print('Most Popular Start month:', popular_month)
    except:
       print('Sorry I Can\'t answer this')

    # find the most popular day
    try:
       popular_day = df['day_of_week'].mode()[0]
       print('Most Popular Start day_of_week:', popular_day)
    except:
       print('Sorry I Can\'t answer this')
    # find the most popular hour
    try:
       popular_hour = df['hour'].mode()[0]
       print('Most Popular Start Hour:', popular_hour)
    except:
        print('Sorry I Can\'t answer this')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('the most popular_start_station: ', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('the most popular_end_station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    freq_combination_stations = (df['Start Station'] + '  to  ' + df['End Station']).mode()[0]
    print('the most freq_combination_stations: starts from:', freq_combination_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_duration =df['Trip Duration'].sum()
    print('total travel time:', total_duration//(24*3600),'days')

    # display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print('average travel time:', avg_duration//60, 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    # print value counts for each user type
    print("User Types:")
    print(" ")
    print(user_types)
    print('-'*20)
    print("Gender:")
    print(" ")
    # Display counts of gender and handling errors
    try:
       gender = df['Gender'].value_counts()
       print(" ")
       print(gender)
    except:
       print("Sorry I Can\'t answer this ")
    print('-'*20)
    print(" ")
    print("Birth year:")
    print(" ")
    # Display earliest, most recent, and most common year of birth and handling errors
    try:
       earliest_birth_year = int(df['Birth Year'].min())
       latest_birth_year = int(df['Birth Year'].max())
       most_frequent_birth_year = int(df['Birth Year'].mode()[0])
       print('the oldest user birth year:',earliest_birth_year)
       print('the youngest user birth year:',latest_birth_year)
       print('the most frequent birth year:',most_frequent_birth_year)
       print("\nThis took %s seconds." % (time.time() - start_time))
    except:
       print("Sorry I Can\'t answer this ")
    print('-'*40)


def main():
    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
