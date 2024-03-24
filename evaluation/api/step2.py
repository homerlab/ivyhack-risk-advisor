import json

#make api call based on the extracted_info.txt file content:

# Load the content of the file
with open('/Users/ayandas/Desktop/VS_Code_Projects/ivyhacks-backend/evaluation/Data/extracted_info.txt') as file:
    content = file.read()

# Remove triple backticks if present
content_cleaned = content.replace('```json', '').replace('```', '').strip()  # otherwise json will not be properly formatted

# Parse the cleaned JSON content
#try:
data = json.loads(content_cleaned)
print(data)

    # Extract the value of "stock_ticker"
stock_ticker = data["stock_ticker"]
start_date = data["start_date"]
end_date = data["end_date"]
investment_amount = data["investment_amount"]

 # able to successfully retrieve the relevant information
print(f"Stock ticker: {stock_ticker}")  
print("Start Date: ", start_date)
print("End Date: ", end_date)
print( "Investment Amount: ", investment_amount)


# make the neccessary api call:
# https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc&limit=120&apiKey=kpfx5ixgOD4mMMy8cRrR_vYAJgWOKWk8


'''
TODO: Retrieve the data from the series of API calls and save it onto the Data directory, that way, we will have more data to work with
- Integrate the changes with Garv's code
- Ensure that proper file pathing is being used

'''
    # Use the extracted value as needed
    # For example, to make an API call

#except json.JSONDecodeError as e:
    #print(f"Failed to decode JSON: {e}")
    

