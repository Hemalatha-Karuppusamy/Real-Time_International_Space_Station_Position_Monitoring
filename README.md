# Real-Time_International_Space_Station_Position_Monitoring
This Python script fetches the current position of the International Space Station (ISS) from the "http://api.open-notify.org/iss-now.json" API and stores the data in a MongoDB database.

## Prerequisites
   ### Before using this project, you need the following:
     1. Python installed (recommended version X.X.X).
     2. Required Python libraries: requests, json, time, pymongo, and pandas.
     3. Access to a MongoDB database (MongoDB Atlas is recommended).

## Usage
     1. Set up a MongoDB database and collection where you want to store the ISS data.
     2. Update the client variable with your MongoDB connection string.
     3. Customize the database and collection names in the script (default names: 'ISS' and 'satellite').
     4. Run the script using Python.
     5. The script will fetch the ISS position 12 times with a 5-second delay between each request. The data will be stored in the specified MongoDB collection.

## Output
  ### The script generates a Pandas DataFrame with the following columns:
      1. timestamp: Timestamp of the data point.
      2. longitude: Longitude of the ISS.
      3. latitude: Latitude of the ISS.
  ### You can use this DataFrame for various data analysis and visualization tasks.
  
