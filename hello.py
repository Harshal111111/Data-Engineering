import os
import re

def get_wifi_passwords():
    wifi_details = []
    wifi_directory = '/etc/NetworkManager/system-connections/'

    if not os.path.exists(wifi_directory):
        print("Wi-Fi connections directory not found!")
        return []

    profiles = os.listdir(wifi_directory)

    for profile in profiles:
        profile_path = os.path.join(wifi_directory, profile)
        try:
            # Read the profile file to extract the Wi-Fi password
            with open(profile_path, 'r') as f:
                content = f.read()

            # Extract SSID and password using regular expressions
            ssid = re.search(r'ssid=(.+)', content)
            password = re.search(r'psk=(.+)', content)

            if ssid and password:
                wifi_details.append(f'Profile: {ssid.group(1)}, Password: {password.group(1)}')
            elif ssid:
                wifi_details.append(f'Profile: {ssid.group(1)}, Password: Not found')
        except PermissionError:
            print(f"Permission denied for {profile_path}. Run the script with elevated privileges.")
            continue

    return wifi_details

for wifi in get_wifi_passwords():
    print(wifi)
