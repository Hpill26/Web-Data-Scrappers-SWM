import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv ("BestSellers.csv")

df['Rating'] = df['Rating'].str.extract('(\d+\.\d+|\d+)').astype(float)

df['Number of Reviews'] = df['Number of Reviews'].str.replace(',', '').str.extract('(\d+)').astype(int)

df['Total Rating'] = df['Rating'] * df['Number of Reviews']

scaler = MinMaxScaler()
df['Scaled Total Rating'] = scaler.fit_transform(df[['Total Rating']])


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.barplot(x='Scaled Total Rating', y='Product Title', data=df, palette='viridis')
plt.xlabel('Scaled Total Rating')
plt.ylabel('Product Title')
plt.title('Scaled Total Ratings for Products')
plt.show()

import matplotlib.pyplot as plt

# Assuming df['Job Title'] is a categorical variable
job_title_percentages = df['Job Title'].value_counts(normalize=True) * 100

# Create a pie chart
plt.figure(figsize=(10, 10))

# Plot the pie chart
wedges, texts, autotexts = plt.pie(job_title_percentages, labels=None, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

# Add labels with a slightly larger font size and adjust layout
plt.setp(autotexts, size=13)
plt.tight_layout()

# Add a legend outside the pie chart with a larger font size
legend = plt.legend(wedges, job_title_percentages.index, title='Job Titles', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize='12')

# Set the font size for legend text
for text in legend.get_texts():
    text.set_fontsize(13)  # Adjust the font size of the legend text

# Add a title
plt.title('Job Titles Distribution')

# Show the plot
plt.show()