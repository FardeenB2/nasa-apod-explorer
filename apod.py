import requests # requests lets us make HTTP calls to external APIs (like fetching a webpage but in code)
import os   ## os lets us read system-level things like they were environment variables
from dotenv import load_dotenv  # load_dotenv is the function we need from the dotenv library to read our .env file

# actually reads the .env file and loads its contents into our current environment memory.
load_dotenv()

# os.getenv looks up the variable named "NASA_API_KEY" from the .env file we just LOADED.
API_KEY = os.getenv("NASA_API_KEY")
URL = "https://api.nasa.gov/planetary/apod"
# this is the endpoint URL for the APOD API — the address we send our request to. Found on the NASA API documentation page for APOD: https://api.nasa.gov


#apod stands for Astronomy Picture of the Day, which is a service provided by NASA that features
#a different photograph of our universe each day, 
#along with a brief explanation written by a professional astronomer.
#The API allows developers to access this content programmatically.


def get_todays_apod():
    
    params = {"api_key": API_KEY}       # params is a dictionary — NASA's API needs our API key sent along with every request
    response = requests.get(URL, params=params)     # requests.get sends an HTTP GET request to the URL with our API key attached
    data = response.json()   # the API sends back raw JSON text and saves it into response. json() converts that into a Python dictionary we can work with
    
    # Now we can access the different pieces of information about today's APOD using the keys in the data dictionary.
    print("Title:", data["title"])
    print("Date:", data["date"])
    print("Image URL:", data["url"])     # the url key contains the image URL we could paste in a browser to see the actual photo
    print("Explanation:", data["explanation"][:300], "...")     # explanation is a long string — [:300] slices just the first 300 characters so it doesn't flood the terminal

#the original JSON structure looked like this:
'''
{
  "copyright": "Lorenzo Busilacchi",
  "date": "2026-04-25",
  "explanation": "This seaside sunset offered a surreal experience, captured in a sea and skyscape from the west coast of Sardinia, Italy, planet Earth. The Daliesque scene is a composition of sequential exposures made with a camera and long telephoto lens. The Sun is not melting, though. Its shifting and fluid appearance as it nears the horizon is caused as refraction along the line of sight changes and creates distorted images or mirages of the reddened solar disk. The changes in atmospheric refraction correspond to atmospheric layers with sharply different temperatures and densities. Another famous but fleeting effect of atmospheric refraction produced by a long sight-line to the setting (or rising) Sun is often called the green flash.",
  "hdurl": "https://apod.nasa.gov/apod/image/2604/sequenzasunsetnebida.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "The Persistence of Sunlight",
  "url": "https://apod.nasa.gov/apod/image/2604/sequenzasunsetnebida1024.jpg"
}
'''


get_todays_apod()