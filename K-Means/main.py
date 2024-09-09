import csv
import os
import random
import math
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

def clear_screen():
    """
    Clears the console screen to each iteration of the clustering process.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def read_csv(file):
    """
    Reads numerical data and labels from a CSV file, assuming the last column contains the labels.

    Parameters:
    - file (str): Path to the CSV file to be read.

    Returns:
    - data (list of lists): Extracted numerical data where each sublist contains the numerical part of the row converted to floats.
    - labels (list): A list of the labels corresponding to each data point, extracted from the last column.

    The function skips rows that do not contain the expected format or are missing data
    """
    data, labels = [], []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row:  # Checks if the row is not empty
                data.append(list(map(float, row[:-1])))  # Converts all but the last column to floats
                labels.append(row[-1])  # The last column is treated as a label
    return data, labels

def mean_centroids(data, assignment, k):
    """
    Calculates the centroids of clusters based on the current assignment of data points to clusters.
    A centroid is computed as the mean of all points assigned to that cluster.

    Parameters:
    - data (list of lists): The dataset where each sublist is a point in multidimensional space.
    - assignment (list): Current cluster assignments of each data point.
    - k (int): Number of clusters.

    Returns:
    - centroids (list of lists): Calculated centroids of the clusters.

    If a cluster has no points assigned, a new centroid for it is randomly initialized within the data bounds.
    """
    centroids = []
    for i in range(k):
        cluster_points = [data[j] for j in range(len(data)) if assignment[j] == i]
        if cluster_points:
            centroids.append([sum(col) / len(col) for col in zip(*cluster_points)])  # Calculate mean of each dimension
        else:
            # Randomly initialize centroid if no points are assigned to the cluster
            centroids.append([random.uniform(min(d), max(d)) for d in zip(*data)])
    return centroids

def euclidean_distance(p1, p2):
    """
    Calculates the Euclidean distance between two points in multidimensional space.
    Assign data points to the nearest cluster based on their distance to centroids.
    Parameters:
    - p1, p2 (lists): Coordinates of the two points.

    Returns:
    - (float): The Euclidean distance between the two points.
    """
    return math.sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(p1, p2)))

def assign_to_centroids(data, centroids):
    """
    Assigns each data point in the dataset to the nearest centroid based on Euclidean distance.

    Parameters:
    - data (list of lists): The dataset.
    - centroids (list of lists): Current centroids of the clusters.

    Returns:
    - assignment (list): Index of the closest centroid for each data point.
    """
    assignment = []
    for i in range(len(data)):
        distances = [euclidean_distance(data[i], centroid) for centroid in centroids]
        assignment.append(distances.index(min(distances)))  # Assign to the nearest centroid
    return assignment

def sum_of_squares(data, centroids, assignment):
    """
    Calculates the total sum of squared distances from each data point to its assigned centroid.
    Monitoring changes in this sum across iterations allows the algorithm to determine when to stop if improvements become negligible.

    Parameters:
    - data (list of lists): The dataset.
    - centroids (list of lists): Current centroids.
    - assignment (list): Index of the assigned centroid for each data point.

    Returns:
    - (float): Sum of squared distances, used as a measure of cluster cohesion.
    """
    total = 0
    for i in range(len(data)):
        total += euclidean_distance(data[i], centroids[assignment[i]]) ** 2
    return total

def calculate_cluster_purity(data, assignment, labels, k):
    """
    Calculates the purity of each cluster, which measures the most frequent label's dominance in each cluster.

    Parameters:
    - data (list of lists): The dataset.
    - assignment (list): Index of the assigned centroid for each data point.
    - labels (list): Labels of each data point.
    - k (int): Number of clusters.

    Returns:
    - cluster_purities (dict): Purity percentage for each cluster.
    """
    cluster_purities = {}
    for i in range(k):
        cluster_labels = [labels[j] for j in range(len(data)) if assignment[j] == i]
        label_counts = {}
        for label in cluster_labels:
            label_counts[label] = label_counts.get(label, 0) + 1
        total_points = len(cluster_labels)
        cluster_purities[i] = {label: (count / total_points) * 100 for label, count in label_counts.items()}
    return cluster_purities

def k_means(data, labels, k):
    """
    Implements the K-means clustering algorithm with data points, labels for calculating purity, and a specified number of clusters.
    Stopping Condition: The loop continues until centroids do not change between iterations or the sum of squared distances within clusters
    does not improve significantly.
    
    Parameters:
    - data (list of lists): The dataset.
    - labels (list): Labels for each data point.
    - k (int): Desired number of clusters.

    Continuously updates cluster assignments and centroids until there is minimal change in centroids,
    indicating convergence, or until the sum of squared distances within clusters does not improve significantly.
    """
    assignment = [random.randint(0, k - 1) for _ in range(len(data))]  # Initial random assignment
    centroids = mean_centroids(data, assignment, k)
    prev_sum = math.inf
    no_improvement_count = 0
    iteration = 1
    while no_improvement_count < 2:
        assignment = assign_to_centroids(data, centroids)
        new_centroids = mean_centroids(data, assignment, k)

        if new_centroids == centroids:  # Check for changes in centroids
            break
        centroids = new_centroids

        current_sum = sum_of_squares(data, centroids, assignment)
        if prev_sum == current_sum:  # Check if there's no improvement in the clustering quality
            no_improvement_count += 1
        else:
            no_improvement_count = 0
        prev_sum = current_sum

        print(f"\033[1;93mIteration {iteration}:\033[0m")
        print("\033[1;93mClusters:\033[0m")
        for i in range(k):
            cluster_points = [data[j] for j in range(len(data)) if assignment[j] == i]
            print(f"\033[1;96mCluster {i + 1}: {cluster_points}\033[0m")

        # Calculate and display the purity of each cluster
        cluster_purities = calculate_cluster_purity(data, assignment, labels, k)
        for cluster, purity in cluster_purities.items():
            print(f"\033[1;96mCluster {cluster + 1} purity: {purity}\033[0m")

        print(f"\033[1;93mSum of squared distances within clusters: {current_sum}\n\033[0m")
        iteration += 1

if __name__ == '__main__':
    csv_file = "iris_kmeans.txt"
    data, labels = read_csv(csv_file)
    while True:
        try:
            k = int(input("\033[1;35mEnter The Number Of Clusters (k): \033[0m"))
            if k <= 0:
                print("\033[1;31mError: Number of clusters must be positive.\033[0m")
                continue
            k_means(data, labels, k)

            X, _ = make_blobs(n_samples=len(data), centers=k, random_state=0)
            kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
            centroids_sklearn = kmeans.cluster_centers_

            plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
            plt.scatter(centroids_sklearn[:, 0], centroids_sklearn[:, 1], marker='X', color='red', s=200)
            plt.title('K-Means Clustering')
            plt.xlabel('Feature 1')
            plt.ylabel('Feature 2')
            plt.show()

            if k == 1:
                print("\033[1;32mExiting Program...\033[0m")
                exit(0)
            else:
                while True:
                    action = input("\033[1;35mDo you want to calculate again? (yes/no): \033[0m").strip().lower()
                    if action == 'no':
                        print("\033[1;32mExiting Program...\033[0m")
                        exit(0)
                    elif action == 'yes':
                        clear_screen()
                        break
                    else:
                        print("\033[1;31mError: Please enter 'yes' or 'no'.\033[0m")
        except KeyboardInterrupt:
            print("\033[1;32m\nExiting Program...\033[0m")
            break