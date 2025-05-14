import requests

def get_geolocation(ip_address):
    """
    Fetches geolocation information for a given IP address using the ip-api service.
    
    Args:
        ip_address (str): The IP address to look up.
    
    Returns:
        dict: A dictionary containing latitude and longitude, or an error message.
    """
    try:
        
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()

       
        if data['status'] == 'success':
            return {
                "latitude": data['lat'],
                "longitude": data['lon']
            }
        else:
            return {"error": data['message']}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("Welcome to the Geolocation Lookup Tool!")
    ip_address = input("Enter an IP address: ").strip()
    
 
    result = get_geolocation(ip_address)
    

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Latitude: {result['latitude']}, Longitude: {result['longitude']}")