# Steps Involved in Data Visualization
# Step-1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step-2 set a theme 
sns.set_theme(style="ticks", color_codes=True)

# Step-3 import data set ("you can also import your own data")
kashti = sns.load_dataset("titanic")
# print(kashti)

# Step-4 plot basic graph with 1 variable (Countplot)
# p=sns.countplot(x='sex', data=kashti)
# plt.show()

# Step-5 plot basic graph with 2 variable (Countplot) 
# p=sns.countplot(x='sex', data=kashti, hue="class")
# plt.show()

# Step-6 plot basic graph with 2 variable (Countplot) with Titles 
p=sns.countplot(x='sex', data=kashti, hue="class")
p.set_title("Mera Count Plot")
plt.show()