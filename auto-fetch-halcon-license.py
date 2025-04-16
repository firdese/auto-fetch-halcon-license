from datetime import datetime
import os
import requests

current_month = datetime.now().month
current_year = datetime.now().year
print(current_month)
halcon_root = os.environ['HALCONROOT']
license_directory = os.path.join(halcon_root, 'license')
license_files = os.listdir(license_directory)

for i in range(len(license_files)):
    curr_license_file = license_files[i]
    year_month_file_end = f"{current_year}_{current_month:02}.dat"
    if (curr_license_file.endswith(year_month_file_end)):
        print("Valid license exists! Program terminating..")
        exit()

url = f"https://raw.githubusercontent.com/lovelyyoshino/Halcon_licenses/master/{current_year}.{current_month:02}/license_support_halcon22.11_steady-dl_{current_year}_{current_month:02}.dat"
output_file_name = f"license_support_halcon22.11_steady-dl_{current_year}_{current_month:02}.dat"
output_full_path = os.path.join(license_directory, output_file_name)
response = requests.get(url)

if response.status_code == 200:
    with open(output_full_path, "wb") as f:
        f.write(response.content)
    print("File downloaded successfully!")
else:
    print(f"Failed to download. Status code: {response.status_code}")

input("Press any key to exit...")
