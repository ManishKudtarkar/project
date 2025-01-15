import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.normal(size=(100, 3))
columns = ["Feature A", "Feature B", "Feature C"]
sns.set_theme(style="darkgrid")

# Create pairplot
sns.pairplot(sns.load_dataset("iris"), hue="species")
plt.show()
