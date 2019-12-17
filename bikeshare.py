import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'C:/Users/Philipp/Desktop/Udacity/Python/Projekt/chicago.csv',
              'new york city': 'C:/Users/Philipp/Desktop/Udacity/Python/Projekt/new_york_city.csv',
              'washington': 'C:/Users/Philipp/Desktop/Udacity/Python/Projekt/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = str()
    
    while city not in cities:
        city = input("Tell me which of the following cities you would like to explore. \
                     \nChoose between chicago, new york city or washington: ")
        city = city.lower()
        if city not in cities:
            print('Oh, something went wrong. Please type the city names as displayed')

    # get user input for month (all, january, february, ... , june)
    
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = str()
    
    while month not in months:
        month = input(("Tell me which of the following months you would like to explore." \
                       "\nChoose between all, january, february, march, april, may and june: "))
        month = month.lower()
        if month not in months:
            print('Oh, something went wrong. Please type the month names or all as displayed')
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = str()
    
    while day not in days:
        day = input('Tell me which of the following days you would like to explore.' \
                   '\nChoose between all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ')
        day = day.title()
        if day not in days:
            print('Oh, something went wrong. Please type the day names or all as displayed')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # display the most common month
    if month == 'all':
        # extract month from the Start Time column to create a month column
        df ['month'] = df['Start Time'].dt.month_name()
    
        popular_month = df['month'].mode()[0]
        print('Most Frequent Month:', popular_month)   
    
    # display the most common day of week   
    if day == 'All':    
        # extract day from the Start Time column to create a day column
        df ['day'] = df['Start Time'].dt.day_name()
        popular_day = df['day'].mode()[0]
        print('Most Frequent Day:', popular_day)
              
    # find the most common hour (from 0 to 23)
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most populat Start Station: ',popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most populat End Station: ',popular_end)

    # display most frequent combination of start station and end station trip
    df['Start to End Station'] = df['Start Station'] + ' to ' + df['End Station']
    popular_start_end = df['Start to End Station'].mode()[0]
    print('Most popular combination of start station and end station:')
    print(popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_ttime = df['Trip Duration'].sum()
    print('Total travel time: ', total_ttime)

    # display mean travel time
    mean_ttime = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_ttime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:')
    print(user_types)
    print()

    # Display counts of gender
    if city == 'chicago' or city == 'new york city':
        gender = df['Gender'].value_counts()
        print('Counts of gender:')
        print(gender)
        print()

        # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_birth = df['Birth Year'].mean()
        print('Year of Birth:')
        print('Earliest: ', earliest)
        print('Most recent: ', recent)
        print('Most common: ', common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()