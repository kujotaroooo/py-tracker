# Geolocation Lookup Tool can be modified with linux nmap

This Python script allows you to fetch the geolocation (latitude and longitude) of a given IP address using the `ip-api` service.

---

## Features

- Retrieves latitude and longitude for any valid IP address.
- Provides error handling for invalid IPs or network issues.
- Simple and easy-to-use command-line interface.

---

## Requirements

1. **Python 3**: Ensure Python 3 is installed on your system.
2. **Requests Library**: Install the `requests` library if not already installed. Use the following command:
   ```bash
   pip install requests
   ```

---

## How to Use

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory containing the `geo.py` file.
3. Run the script using Python:
   ```bash
   python geo.py
   ```
4. Enter the IP address when prompted (e.g., `8.8.8.8`).
5. The script will display the latitude and longitude of the IP address or an error message if the lookup fails.

---

## Example

### Input:
```plaintext
Enter an IP address: 8.8.8.8
```

### Output:
```plaintext
Latitude: 37.751, Longitude: -97.822
```

---

## Notes

- This script uses the free `ip-api` service, which has a rate limit of 45 requests per minute.
- For higher limits or additional features, consider using a paid geolocation API service.

---

## Disclaimer

This tool is for educational purposes only. Ensure you comply with all applicable laws and regulations when using it.
