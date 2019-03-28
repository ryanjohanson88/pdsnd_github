<<<<<<< HEAD
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    while True:
        city = input('\nWould you like to see data for Chicago, New York City,
        or Washington?\n').lower()

        if city in CITY_DATA:
            break

        else:
            print('\nSorry that\'s not a valid city!')

    # get user input for month (all, january, february, ... , june)

    months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')


    while True:
        month = input('\nWould you like to see data for January, February, March,
         April, May, June, or  All to see all data?\n').lower()

        if month in months:
                          break
        else:
            print('\nSorry that\'s not a valid month!')

    # get user input for day of week (all, monday, tuesday, ... sunday)

    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')

    while True:
        day = input('\nWould you like to see data for Monday, Tuesday, Wednesday,
         Thursday, Friday, Saturday, Sunday, or All to see all data?\n').lower()

        if day in days:
                        break

        else:
            print('\nSorry that\'s not a valid day!')

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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month

    df['day of week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']


        # filter by month to create the new dataframe

        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day of week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month

    df['month'] = df['Start Time'].dt.month

    common_month = df['month'].mode()[0]

    print('\nMost popular month of travel: ', common_month)


    # display the most common day of week

    df['day'] = df['Start Time'].dt.day

    common_day = df['day'].mode()[0]

    print('\nMost popular day of the week: ', common_day)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]

    print('\nMost popular starting hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]

    print('\nMost popular starting station: ', common_start_station)

    # display most commonly used end station

    common_end_station = df['End Station'].mode()[0]

    print('\nMost Popular Ending Station: ', common_end_station)

    # display most frequent combination of start station and end station trip

    common_trip = df[['Start Station', 'End Station']].mode().loc[0]

    print('\nMost popular starting and ending station (round trip):
    {} and {}'.format(common_trip[0], common_trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_trip = df['Trip Duration'].sum()

    print('\nTotal travel time: ', total_trip)

    # display mean travel time

    average_trip = df['Trip Duration'].mean()

    print('\nAverage travel time: ', average_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()

    print('\nTotal user types: ', user_types)

    # Display counts of gender

    gender_count = df['Gender'].value_counts()

    print('\nTotal gender count: ', gender_count)

    # Display earliest, most recent, and most common year of birth

    earliest_birth = df['Birth Year'].min()
    earliest_birth = int(earliest_birth)


    recent_birth = df['Birth Year'].max()
    recent_birth = int(recent_birth)

    common_birth = df['Birth Year'].mode()[0]
    common_birth = int(common_birth)

    print('\nThe earliest birth year is {} \nThe most recent birth year is {}\n The most common birth year is {}'.format(earliest_birth, recent_birth, common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():


    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)

        more_lines = input('\nWould you like to see the next 5 lines of data? Enter yes or no\n')
        if more_lines.lower() != 'yes':
            break

        station_stats(df)

        more_lines = input('\nWould you like to see the next 5 lines of data? Enter yes or no\n')
        if more_lines.lower() != 'yes':
            break

        trip_duration_stats(df)

        more_lines = input('\nWould you like to see the next 5 lines of data? Enter yes or no\n')
        if more_lines.lower() != 'yes':
            break

        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
||||||| parent of 8fc8509... Tighten spacing for def get_filters
=======
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    while True:
        city = input('\nWould you like to see data for Chicago, New York City,
        or Washington?\n').lower()

        if city in CITY_DATA:
            break

        else:
            print('\nSorry that\'s not a valid city!')

    # get user input for month (all, january, february, ... , june)

    months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')


    while True:
        month = input('\nWould you like to see data for January, February, March,
         April, May, June, or  All to see all data?\n').lower()

        if month in months:
                          break
        else:
            print('\nSorry that\'s not a valid month!')

    # get user input for day of week (all, monday, tuesday, ... sunday)

    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')

    while True:
        day = input('\nWould you like to see data for Monday, Tuesday, Wednesday,
         Thursday, Friday, Saturday, Sunday, or All to see all data?\n').lower()

        if day in days:
                        break

        else:
            print('\nSorry that\'s not a valid day!')

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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month

    df['day of week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']


        # filter by month to create the new dataframe

        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day of week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month

    df['month'] = df['Start Time'].dt.month

    common_month = df['month'].mode()[0]

    print('\nMost popular month of travel: ', common_month)


    # display the most common day of week

    df['day'] = df['Start Time'].dt.day

    common_day = df['day'].mode()[0]

    print('\nMost popular day of the week: ', common_day)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]

    print('\nMost popular starting hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]

    print('\nMost popular starting station: ', common_start_station)

    # display most commonly used end station

    common_end_station = df['End Station'].mode()[0]

    print('\nMost Popular Ending Station: ', common_end_station)

    # display most frequent combination of start station and end station trip

    common_trip = df[['Start Station', 'End Station']].mode().loc[0]

    print('\nMost popular starting and ending station (round trip):
    {} and {}'.format(common_trip[0], common_trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_trip = df['Trip Duration'].sum()

    print('\nTotal travel time: ', total_trip)

    # display mean travel time

    average_trip = df['Trip Duration'].mean()

    print('\nAverage travel time: ', average_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()

    print('\nTotal user types: ', user_types)

    # Display counts of gender

    gender_count = df['Gender'].value_counts()

    print('\nTotal gender count: ', gender_count)

    # Display earliest, most recent, and most common year of birth

    earliest_birth = df['Birth Year'].min()
    earliest_birth = int(earliest_birth)


    recent_birth = df['Birth Year'].max()
    recent_birth = int(recent_birth)

    common_birth = df['Birth Year'].mode()[0]
    common_birth = int(common_birth)

    print('\nThe earliest birth year is {} \nThe most recent birth year is {}\n The most common birth year is {}'.format(earliest_birth, recent_birth, common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():


    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)

        more_lines = input('\nWould you like to see the next 5 lines of data? Enter yes or no\n')
        if more_lines.lower() != 'yes':
            break

        station_stats(df)

        more_lines = input('\nWould you like to see the next 5 lines of data? Enter yes or no\n')
        if more_lines.lower() != 'yes':
            break

        trip_duration_stats(df)

        more_lines = input('\nWould you like to see the next 5 lines of data? Enter yes or no\n')
        if more_lines.lower() != 'yes':
            break

        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
>>>>>>> 8fc8509... Tighten spacing for def get_filters
