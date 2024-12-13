import requests
import pandas as pd

def fetch_data_from_api(api_url):
    """

    Args:
        api_url (str): The API endpoint URL.

    Returns:
        list: A list of dictionaries containing user data.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def export_data_to_csv(data, file_name):
    """

    Args:
        data (list): List of dictionaries to export.
        file_name (str): Name of the CSV file to create.
    """
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        print(f"Data exported successfully to {file_name}")
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")

if __name__ == "__main__":
    
    API_URL = "https://jsonplaceholder.typicode.com/users"
    

    user_data = fetch_data_from_api(API_URL)

    if user_data:
    
        export_data_to_csv(user_data, "users.csv")