def is_rush_hour(hour):
    return 1 if hour in [5, 6, 7, 12, 13, 14, 15] else 0


def extract_period_of_day(hour):
    if hour in range(12):
        return [0,1,0]
    elif hour in range(12, 18):
        return [0,0,0]
    elif hour in range(18, 22):
        return [1,0,0]
    else:
        return [0,0,1]

def preprocess_season(season) :
    if season.lower() == 'summer' : 
        return [0, 1, 0]
    elif season.lower() == 'winter' :
        return [0, 0, 1]
    elif season.lower() == 'spring' :
        return [1, 0, 0]
    else :
        return [0,0,0]
    
def preprocess_weather(weather) :
    if weather.lower() == 'mist' : 
        return [1, 0, 0]
    elif weather.lower() == 'rainy' :
        return [0, 1, 0]
    elif weather.lower() == 'snowy' :
        return [0, 0, 1]
    else :
        return [0,0,0]

def weakday_name(day) :
    if day.lower() == 'monday' :
        return [1,0,0,0,0,0]
    elif day.lower() == 'saturday' :
        return [0,1,0,0,0,0]
    elif day.lower() == 'sunday' :
        return [0,0,1,0,0,0]
    elif day.lower() == 'thursday' :
        return [0,0,0,1,0,0]
    elif day.lower() == 'tuesday' :
        return [0,0,0,0,1,0]
    elif day.lower() == 'wednesday' :
        return [0,0,0,0,0,1]
    else :
        return [0,0,0,0,0,0]
    
    
    
## data is du=ictionary contains all input from the user
def preprocess_data(data) :
    temp = data['temperature']
    
    humidity = data['humidity']
    
    hour = data['hour']
    
    rush_hour = is_rush_hour(data['hour'])    
    
    month = data['month']
    
    season_features = preprocess_season(data['season'])
    
    weather_features = preprocess_weather(data['weather'])
    
    day_name_features = weakday_name(data['day'])
    
    period_of_day = extract_period_of_day(data['hour'])
    
    final_data = [temp, humidity, hour, rush_hour, month] + season_features + weather_features + day_name_features + period_of_day
    
    return final_data
