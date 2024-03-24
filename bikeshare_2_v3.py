import time
import datetime
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
    
    cities = ['chicago','new york','washington']
    city = input('Which city do you want to see data for Chicago, New York or Washington ?')
    city = city.lower()
    
    while city not in cities:
        print('Please one of these 3 cities: Chicago, New York or Washington')
        city = input('Which city do you want to see data for Chicago, New York or Washington ?')
        city = city.lower() # eliminate upper/lower case


    # get user input for month (all, january, february, ... , june)
    
    months = {'january': 1 ,'february': 2,'march': 3,'april': 4,'may': 5,'june': 6,'july': 7,'august': 8,'september': 9,'october': 10,'november': 11,'december': 12}
    month = input('Would you like to filter the data my month ? If it is yes enter which month. You can type "all" for no time filter')
    month = month.lower() # eliminate upper/lower case
    

    if month != 'all':
        while month not in months:
            print('Please enter a valid month.')
            month = input()
            month = month.lower()
            month = months[month]


    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = {'sunday': 0 ,'monday': 1,'tuesday': 2,'wednesday': 3,'thursday': 4,'friday': 5,'saturday': 6}
    day = input('Would you like to filter the data my day ? If it is yes enter which day as an integer (e.g., 1=Sunday).You can type "all" for no time filter')
    day = day.lower()
    
    
    if day != 'all':
        while day not in days:
            print('Please enter a valid day.')
            day = input()
            day = day.lower() 
            day = days[day]
            

    print('\n-'*40)
    return city,month,day



def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    if city == 'chicago':
        df = pd.read_csv("chicago.csv")
    elif city == 'new york':
        df = pd.read_csv("new_york_city.csv")
    elif city == 'washington':
        df = pd.read_csv("washington.csv")
        
        
    df["Start Month"] = pd.to_datetime(df["Start Time"]).dt.month
    df["Start Day"] = pd.to_datetime(df["Start Time"]).dt.day_of_week
    df["Start Hour"] = pd.to_datetime(df["Start Time"]).dt.hour
    

    if month == 'all':
        df_filter_month = df
    else:
        df_filter_month = df[(df["Start Month"]==month)]
        
        
    if day == 'all':
        df_filter_month_day = df_filter_month
    else:
        df_filter_month_day = df_filter_month[(df_filter_month["Start Day"]==day)]
        
        
    return df_filter_month_day



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df_month = df["Start Month"].mode()[0]
    print('The most common month >> ', df_month)

    # display the most common day of week
    df_day = df["Start Day"].mode()[0]
    print('The most common day >> ',df_day)
    
    # display the most common start hour
    df_hour = df["Start Hour"].mode()[0]
    print('The most common hour >> ',df_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    df_start_st = df["Start Station"].mode()[0]
    print('The most commonly used start station >> ', df_start_st)

    # display most commonly used end station
    df_start_st = df["End Station"].mode()[0]
    print('The most commonly used end station >> ',df_start_st)

    # display most frequent combination of start station and end station trip
    df["Start End st"] = df["Start Station"]+'-'+ df["End Station"]
    df_start_end_mod  = df["Start End st"].mode()[0]
    print('The most frequent combination of start station and end station trip >>',df_start_end_mod)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df["Trip Duration"].sum()
    print('Total travel time >> ',total_travel)
    
    
    # display mean travel time
    mean_travel = df["Trip Duration"].mean()
    print('Mean travel time >> ',mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n-'*40)


def user_stats(city,df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df_count_usertype = df['User Type'].value_counts()
    print('Counts of user types >>')
    print(df_count_usertype)

    if city != 'washington':
        # Display counts of gender
        df_count_gender = df['Gender'].value_counts()
        print('Counts of gender >>')
        print(df_count_gender)
    
        # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common  = df['Birth Year'].mode()[0]
        
        
        print('Earliest Year >>',earliest)
        print('Most Recent Year >>', most_recent)
        print('Most Common Year >>', most_common)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n-'*40)

def view_data(df):


    view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n").lower()
    start_loc = 0
    
   
    
    if start_loc < len(df) :
        while view_data == 'yes':
            view_df = df.iloc[start_loc:start_loc+5]
            print(view_df)
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city,df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
 	main()
