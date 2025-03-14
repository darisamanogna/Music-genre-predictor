import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
df_tracks=pd.read_csv('spotify.csv')
# The first rows of dataset
df_tracks.head()

# null values
pd.isnull(df_tracks).sum()

df_tracks.info()

# least popular songs
sorted_df=df_tracks.sort_values('popularity',ascending=True).head(10)
sorted_df

df_tracks.describe().transpose()

# Top 10 most popular songs
most_popular=df_tracks.query('popularity>90',inplace=False).sort_values('popularity',ascending=False)
most_popular[:10]

# correlation map
corr_df=df_tracks.drop(["key","mode","explicit"],axis=1).corr(method="pearson",numeric_only=True)
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g",vmin=-1,vmax=1,center=0,cmap="inferno",linewidths=1,linecolor="Black")
heatmap.set_title("Correlation Map")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)
plt.show()

plt.figure(figsize=(20,16))
sns.regplot(data=df_tracks,y="loudness",x="energy",color="c").set(title="Loudness vs energy correlation")
plt.show()

plt.figure(figsize=(70, 66))
regplot = sns.regplot(data=df_tracks, y="popularity", x="acousticness", color="g")
regplot.set(title="popularity vs Acousticness Correlation")
# regplot.set_title("popularity vs Acousticness Correlation", fontsize=70)  
regplot.set_xlabel("Acousticness", fontsize=60)
regplot.set_ylabel("Popularity", fontsize=60)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
plt.show()


plt.figure(figsize=(90,86))
sns.set_palette("rocket")
sns.barplot(x='track_genre', y='duration_ms', data=df_tracks)
plt.title("Duration of the Songs in Different Genres", fontsize=90)
plt.xlabel("Track Genre", fontsize=70)
plt.ylabel("Duration in ms", fontsize=70)
plt.xticks(rotation=45, fontsize=40)
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plot style
sns.set(style="whitegrid")

# Plot histograms for numerical features
df_tracks.hist(bins=30, figsize=(20, 15))
plt.suptitle('Feature Distributions')
plt.show()

# Plot boxplots to detect outliers
plt.figure(figsize=(20, 15))
sns.boxplot(data=df_tracks, orient='h')
plt.title('Box Plots for Numerical Features')
plt.show()


numerical_features = ['danceability', 'energy', 'loudness', 'tempo', 'duration_ms', 'popularity']
for feature in numerical_features:
    plt.figure(figsize=(10, 6))
    feature_counts, bin_edges = np.histogram(df_tracks[feature], bins=30)
    plt.bar(bin_edges[:-1], feature_counts, width=np.diff(bin_edges), color='b', edgecolor='black')
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()


categorical_features = ['key', 'mode', 'time_signature']
for feature in categorical_features:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=df_tracks[feature], hue=df_tracks[feature], order=df_tracks[feature].value_counts().index, palette='viridis', legend=False)
    plt.title(f'Count Plot of {feature}')
    plt.show()



for feature in numerical_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df_tracks[feature], color='green')
    plt.title(f'Box Plot of {feature}')
    plt.show()


# import numpy as np
# from collections import Counter

# class KNN:
#     def __init__(self, k=3, distance_metric='euclidean'):
#         self.k = k
#         self.distance_metric = distance_metric

#     def set_params(self, k=None, distance_metric=None):
#         if k is not None:
#             self.k = k
#         if distance_metric is not None:
#             self.distance_metric = distance_metric

#     def get_params(self):
#         return {'k': self.k, 'distance_metric': self.distance_metric}

#     def fit(self, X, y):
#         self.X_train = X
#         self.y_train = y

#     def predict(self, X):
#         return np.array([self._predict(x) for x in X])

#     def _predict(self, x):
#         distances = self._compute_distances(x)
#         k_indices = np.argsort(distances)[:self.k]
#         k_nearest_labels = [self.y_train[i] for i in k_indices]
#         return Counter(k_nearest_labels).most_common(1)[0][0]

#     def _compute_distances(self, x):
#         if self.distance_metric == 'euclidean':
#             return np.linalg.norm(self.X_train - x, axis=1)
#         elif self.distance_metric == 'manhattan':
#             return np.sum(np.abs(self.X_train - x), axis=1)
#         else:
#             raise ValueError("Unsupported distance metric")


# class Metrics:
#     def __init__(self, y_true, y_pred):
#         self.y_true = y_true
#         self.y_pred = y_pred
#         self.classes = np.unique(y_true)

#     def accuracy(self):
#         return np.mean(self.y_true == self.y_pred)

#     def precision(self, average='macro'):
#         precision = {}
#         for c in self.classes:
#             true_positive = np.sum((self.y_true == c) & (self.y_pred == c))
#             false_positive = np.sum((self.y_true != c) & (self.y_pred == c))
#             precision[c] = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
        
#         if average == 'macro':
#             return np.mean(list(precision.values()))
#         elif average == 'micro':
#             true_positive = np.sum(self.y_true == self.y_pred)
#             false_positive = np.sum(self.y_pred != self.y_true)
#             return true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0

#     def recall(self, average='macro'):
#         recall = {}
#         for c in self.classes:
#             true_positive = np.sum((self.y_true == c) & (self.y_pred == c))
#             false_negative = np.sum((self.y_true == c) & (self.y_pred != c))
#             recall[c] = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
        
#         if average == 'macro':
#             return np.mean(list(recall.values()))
#         elif average == 'micro':
#             true_positive = np.sum(self.y_true == self.y_pred)
#             false_negative = np.sum(self.y_true != self.y_pred)
#             return true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0

#     def f1_score(self, average='macro'):
#         precision = self.precision(average=average)
#         recall = self.recall(average=average)
#         return 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0


import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3, distance_metric='euclidean'):
        self.k = k
        self.distance_metric = distance_metric

    def set_params(self, k=None, distance_metric=None):
        """Modify k and distance metric."""
        if k is not None:
            self.k = k
        if distance_metric is not None:
            self.distance_metric = distance_metric

    def get_params(self):
        """Return current k and distance metric."""
        return {'k': self.k, 'distance_metric': self.distance_metric}

    def fit(self, X, y):
        """Fit the model by storing the training data."""
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """Predict the label for each data point in X."""
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        """Helper method to predict the label for a single data point."""
        distances = self._compute_distances(x)
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        return Counter(k_nearest_labels).most_common(1)[0][0]

    def _compute_distances(self, x):
        """Compute distances between x and all training data."""
        if self.distance_metric == 'euclidean':
            return np.linalg.norm(self.X_train - x, axis=1)
        elif self.distance_metric == 'manhattan':
            return np.sum(np.abs(self.X_train - x), axis=1)
        else:
            raise ValueError("Unsupported distance metric")


class Metrics:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
        self.classes = np.unique(y_true)

    def accuracy(self):
        """Calculate the accuracy of predictions."""
        return np.mean(self.y_true == self.y_pred)

    def precision(self, average='macro'):
        """Calculate precision."""
        precision = {}
        for c in self.classes:
            true_positive = np.sum((self.y_true == c) & (self.y_pred == c))
            false_positive = np.sum((self.y_true != c) & (self.y_pred == c))
            precision[c] = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
        
        if average == 'macro':
            return np.mean(list(precision.values()))
        elif average == 'micro':
            true_positive = np.sum(self.y_true == self.y_pred)
            false_positive = np.sum(self.y_pred != self.y_true)
            return true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0

    def recall(self, average='macro'):
        """Calculate recall."""
        recall = {}
        for c in self.classes:
            true_positive = np.sum((self.y_true == c) & (self.y_pred == c))
            false_negative = np.sum((self.y_true == c) & (self.y_pred != c))
            recall[c] = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
        
        if average == 'macro':
            return np.mean(list(recall.values()))
        elif average == 'micro':
            true_positive = np.sum(self.y_true == self.y_pred)
            false_negative = np.sum(self.y_true != self.y_pred)
            return true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0

    def f1_score(self, average='macro'):
        """Calculate F1-score."""
        precision = self.precision(average=average)
        recall = self.recall(average=average)
        return 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0


def train_test_split(X, y, test_size=0.2):
    """Split data into training and test sets."""
    num_test = int(len(X) * test_size)
    indices = np.arange(len(X))
    np.random.shuffle(indices)
    test_indices = indices[:num_test]
    train_indices = indices[num_test:]
    
    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]

    return X_train, X_test, y_train, y_test


# Define numerical features and target variable
numerical_features = ['danceability', 'energy', 'loudness', 'tempo', 'duration_ms', 'popularity']
X = df_tracks[numerical_features].values  # Convert to numpy array

# Manually scale the features
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
X_scaled = (X - mean) / std

# Define target variable
y = df_tracks['track_genre'].values

# Train-test split
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2)

# Initialize and train KNN model
knn = KNN(k=50, distance_metric='euclidean')
knn.fit(X_train, y_train)

# Predict on the validation set
y_pred = knn.predict(X_val)

# Calculate metrics
metrics = Metrics(y_val, y_pred)
print("Accuracy:", metrics.accuracy())
print("Precision (Macro):", metrics.precision(average='macro'))
print("Recall (Macro):", metrics.recall(average='macro'))
print("F1 Score (Macro):", metrics.f1_score(average='macro'))
print("Precision (Micro):", metrics.precision(average='micro'))
print("Recall (Micro):", metrics.recall(average='micro'))
print("F1 Score (Micro):", metrics.f1_score(average='micro'))
# Predict on validation set
y_pred = knn.predict(X_val)

# Evaluate the model using custom metrics
metrics = Metrics(y_true=y_val, y_pred=y_pred)
accuracy = metrics.accuracy()
precision = metrics.precision(average='macro')
recall = metrics.recall(average='macro')
f1 = metrics.f1_score(average='macro')

# Print the evaluation metrics
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")


