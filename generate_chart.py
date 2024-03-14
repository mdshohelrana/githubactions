import matplotlib.pyplot as plt

# Pie chart data
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [15, 30, 45, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.1, 0, 0, 0)  # Explode the 1st slice (Apples)

# Create pie chart
plt.figure(figsize=(10,7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Fruit Pie Chart')
plt.savefig('fruit_pie_chart.png')  # Save the pie chart as an image file
print("Pie chart saved as 'fruit_pie_chart.png'.")