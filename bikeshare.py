import time
import pandas as pd
import numpy as np

#Refactor the code
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
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
	
	city = input("\nfrom which city you want to see data New York, Chicago ,or Washington?\n").lower()
	#lower to get input in any format

	while True:
	    if city in ['chicago', 'new york', 'washington']:
	        break
		else:
		    city = input('Enter Correct city: ').lower()
	         #lower is used to get input in any format

	    
	  
	

    #get user input for month (all, january, february, ... , june)
	month = input("\nEnter the name of the month January, February, March, April, May , June  or \"all\" if you do not have any preference\n").lower()
     #lower is used to get input in any format

	while True:
		if month in ["January", "February", "March", "April", "May", "June", "all"]:
			break
		else:
			month = input('Enter valid month\n').lower()


    #get user input for day of week (all, monday, tuesday, ... sunday)
	day = input("\n Select day to do filter by it  Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' to display data for all day.\n").lower()
	 #lower is used to get input in any format
	while True:
		if day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "all"]:
		    break 
		else:
			 day = input('Enter Correct day: ').lower()
              #lower is used to get input in any format
			
	#return day
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
    # to_datetime is used to convert date into date format
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #used to find index of month.
        month = months.index(month) + 1       

        df = df[df['Start Time'].dt.month == month]
        
    #filter data by day.
    if day != 'all': 
        df = df[df['Start Time'].dt.weekday_name == day.title()]
     #print 5 rows.
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    #display the most common day of week
		 if(day == 'all'):
             most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
			 print('Most common day is ' + str(most_common_day))


    #display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
	most_common_start_station = df['Start Station'].value_counts().idxmax()
	print('Most Commonly used start station is :{}'.format(most_common_start_station))

    #display most commonly used end station
	most_common_end_station  = df['End Station'].value_counts().idxmax()
	print('\nMost Commonly used end station is {}:'.format(most_common_end_station))


    #display most frequent combination of start station and end station trip
	combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}\n'.format(most_frequent_trip))

				 
				 
				 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
	#Convert number to readable time format day, hour, minutes, seconds
	total_travel_time = df['Trip Duration'].sum()
    time1 = total_travel_time
    day = time1 // (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour = time1 // 3600
    time1 %= 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1
    print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))

    #display mean travel time
	#Convert number to readable time format day, hour, minutes, seconds
	mean_travel_time = df['Trip Duration'].mean()
    time2 = mean_travel_time
    day2 = time2 // (24 * 3600)
    time_2 = time2 % (24 * 3600)
    hour2 = time2 // 3600
    time2 %= 3600
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print('\nMean travel time is {} hours {} minutes {} seconds'.format(hour2, minutes2, seconds2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
	user_types = df['User Type'].value_counts()
    print(user_types)

    #Display counts of gender

	if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(male_count)))
        print('\nNumber of female users are {}\n'.format(int(female_count)))

    #Display earliest, most recent, and most common year of birth
	if('Birth Year' in df):
			earliest_birth_year = df['Birth Year'].min()
			recent_birth_year = df['Birth Year'].max()
			common_birth_year = df['Birth Year'].mode()[0]					
			print('\n Earliest year of birth:" {}\n Most recent year of birth: {}\n Most common year of birth is : {}\n'.format(int(earliest_birth_year), int(recent_birth_year), int(common_birth_year)))

					
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

	
	
	
def show_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no.\n')
    line_number = 0

    while True:
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
        else:
            break  

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
		show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
