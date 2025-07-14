import requests
import os

def download_csv_from_google_sheets():
    # Google Sheets CSV export URL
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTCFxQy8ns6GYh9432Qny68rDtHftRrZDyCCN4KU1Q9vaI5gCNTCwABPTijGZpq-xrASIKn9h7Cq_Gx/pub?gid=0&single=true&output=csv"
    
    # Output filename
    filename = "觀察清單.csv"
    
    try:
        # Download the CSV data
        print("Downloading CSV from Google Sheets...")
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Save the content to a CSV file
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        print(f"✅ Successfully downloaded and saved as '{filename}'")
        print(f"📁 File size: {len(response.content)} bytes")
        
        # Check if file exists and show its absolute path
        if os.path.exists(filename):
            abs_path = os.path.abspath(filename)
            print(f"📍 File location: {abs_path}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading the file: {e}")
    except IOError as e:
        print(f"❌ Error saving the file: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    download_csv_from_google_sheets()