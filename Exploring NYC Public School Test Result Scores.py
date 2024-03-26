# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("dataset\schools.csv")

# Preview the data
schools.head()

# Start coding here...
max_math_score = 800
best_math_schools = schools[schools['average_math'] >= 0.8 * max_math_score]
best_math_schools = best_math_schools[['school_name', 'average_math']].sort_values(by='average_math', ascending=False)
print(best_math_schools.head(10))

# Calculate total SAT scores for each school
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

# Identify the top 10 performing schools based on total SAT scores
top_10_schools = schools[['school_name', 'total_SAT']].sort_values(by='total_SAT', ascending=False).head(10)

# Display the top 10 schools
print(top_10_schools)

# Assuming the previous steps have been executed successfully and we have the 'schools' DataFrame ready.
# Group by borough and calculate statistics
borough_stats = schools.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std'])

# Find the borough with the largest standard deviation
largest_std_dev_index = borough_stats['std'].idxmax()
largest_std_dev_row = borough_stats.loc[largest_std_dev_index]

# Convert the row to a DataFrame and reset the index to make it a proper DataFrame
largest_std_dev = pd.DataFrame(largest_std_dev_row).T.reset_index()

# Rename the columns for clarity
largest_std_dev.columns = ['borough', 'num_schools', 'average_SAT', 'std_SAT']

# Round all numeric values to two decimal places
largest_std_dev = largest_std_dev.round(2)

# Display the borough with the largest standard deviation
print(largest_std_dev)
