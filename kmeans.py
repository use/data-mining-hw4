import csv
import math
import random
from dataclasses import dataclass
from typing import List

@dataclass
class ClusterResults:
    clusters: List[List[List[float]]]
    centroids: List[List[float]]
    iterations: int

def item_distance(a: List[float], b: List[float]) -> float:
    # euclidian distance
    return math.sqrt(sum([(a[i] - b[i])**2 for i in range(len(a))]))

def find_centroid(items: List[List[float]]) -> List[float]:
    # take the average of each column
    return [mean([item[i] for item in items]) for i in range(len(items[0]))]

def mean(items: List[float]) -> float:
    return sum(items) / len(items)

def find_clusters(items: List[List[float]], k: int):
    centroids = None
    old_clusters = [[] for x in range(k)]

    iterations = 0
    while True:
        iterations += 1
        new_clusters = [[] for x in range(k)]

        if not centroids:
            # select k objects at random for the first centroids
            centroids = random.sample(items, k)

        # assign objects to clusters based on closest centroid
        for item in items:
            lowest_distance = None
            selected_index = None

            # find closest centroid to this object
            for index, centroid in enumerate(centroids):
                distance = item_distance(item, centroid)
                if lowest_distance is None or distance < lowest_distance:
                    lowest_distance = distance
                    selected_index = index
            new_clusters[selected_index].append(item)

        if new_clusters == old_clusters:
            return ClusterResults(
                clusters = new_clusters,
                iterations = iterations,
                centroids = centroids,
            )

        centroids = [find_centroid(cluster) for cluster in new_clusters]
        old_clusters = new_clusters

if __name__ == '__main__':
    items = []
    with open('synthetic_control_data.txt', newline='') as itemfile:
        for line in itemfile:
            items.append([float(item) for item in line.split()])

    # create the clusters multiple times to compare
    for i in range(1):
        results = find_clusters(items, 6)
        print(
            'sorted cluster sizes:',
            sorted([len(cluster) for cluster in results.clusters], reverse=True),
            f"(required {results.iterations} iterations)"
        )

        # only save the results of the first attempt
        if i == 0:
            for index, cluster in enumerate(results.clusters):
                with open(f"cluster-{index+1}.csv", 'w', newline='') as outfile:
                    writer = csv.writer(outfile)
                    for item in cluster:
                        writer.writerow(item)
