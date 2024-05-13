from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import time

def get_city_coordinates(city, attempt=1, max_attempts=3):
    geolocator = Nominatim(user_agent="geoapiExercise_v1")
    
    try:
        location = geolocator.geocode(city, timeout=10)
        if location:
            return (location.latitude, location.longitude)
        else:
            print(f"Could not find location for {city}")
            return None
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            print(f"Geocoder timed out, retrying... Attempt {attempt} of {max_attempts}")
            time.sleep(1)
            return get_city_coordinates(city, attempt + 1, max_attempts)
        else:
            print("Geocoder timed out after all retries")
            return None
    except GeocoderUnavailable:
        print("Geocoder service is unavailable")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def calculate_distance(city1, city2):
    coords_1 = get_city_coordinates(city1)
    coords_2 = get_city_coordinates(city2)
    
    if coords_1 and coords_2:
        distance_km = geodesic(coords_1, coords_2).kilometers
        distance_miles = geodesic(coords_1, coords_2).miles
        return distance_km, distance_miles
    else:
        return None, None

def main():
    print("Distance Calculator")
    print("Type 'exit' to quit the program at any time.\n")

    while True:
        # Ask the user for the names of two cities
        city1 = input("Enter the name of the first city: ")
        if city1.lower() == 'exit':
            break
        city2 = input("Enter the name of the second city: ")
        if city2.lower() == 'exit':
            break
        
        # Calculate the distance between the cities
        distance_km, distance_miles = calculate_distance(city1, city2)
        
        if distance_km is not None:
            print(f"The distance between {city1} and {city2} is {distance_km:.2f} km or {distance_miles:.2f} miles.\n")
        else:
            print("One or both of the cities could not be found. Please check the names and try again.\n")

if __name__ == "__main__":
    main()
