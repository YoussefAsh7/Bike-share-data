import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

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
      city = input("Which city would you like to filter by? New York City, Chicago or Washington?\n").strip().lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("wrong answer please choose from (new york city, chicago, washington)")
        continue
      else:
        break

    # get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").strip().lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("wrong answer please choose from (january, february, march, april, may, june) or all if you do not have any preference")
        continue
      else:
        break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nWhich day would you like to filter by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("wrong answer please choose from (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday) or all if you do not have any preference")
        continue
      else:
        break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the day list to get the corresponding int
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df["month"].mode()[0]
    print("the most common month: ", most_common_month)

    # display the most common day of week
    most_common_day = df["day_of_week"].mode()[0]
    print("the most common day: ", most_common_day)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df["hour"].mode()[0]
    print('Most Frequent Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station: ", most_start_station)

    # display most commonly used end station
    most_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station: ", most_end_station)

    # display most frequent combination of start station and end station trip
    print('Most Commonly used combination of start station and end station trip:', most_start_station, " & ", most_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', format(total_travel_time / 3600, ".5"), " hours")

    # display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', format(Mean_Travel_Time / 60, ".5"), " minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df["User Type"].value_counts()
    print("counts of user types: \n", counts_of_user_types)

    # Display counts of gender
    try:
        counts_of_gender = df["Gender"].value_counts()
        print("\ncounts of Gender: \n", counts_of_gender)
    except:
        print("\nNo data available for this city")
    # Display earliest, most recent, and most common year of birth
    try:
        most_common_year_of_birth = df["Birth Year"].mode()[0]
        print("\nThe most common year of birth: ", most_common_year_of_birth)
        The_earliset_year_of_birth = df["Birth Year"].min()
        print("\nThe earliest year of birth: ", The_earliset_year_of_birth)
        The_most_recent_year_of_birth = df["Birth Year"].max()
        print("\nThe most recent year of birth: ", The_most_recent_year_of_birth)
    except:
        print("No data available for this city")

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
