# Anomaly Detection in Public Street Lighting using Clustering Algorithms
### Requirement
- Data set is converted from JSON to Spark DataFrame by using PySpark=3.2.1.
- To implement the clustering algorithm, Spark DataFrame is converted into the Pandas DataFrame and scikit-learn=0.24.2 is exploited.
### Running code classes in Anomaly-Detection project
Project repository contains data set folder with name “PELL_Data_with_Synthetic_Anomalies” and implementation files for algorithms K-means, DBSCAN, OPTICS, and synthetic anomaly injection.
#### How to execute K-means Model
```
Run main.py    and      uncomment
kmeans = KmeansAnomalyDetection()
kmeans.Kmeans_anomaly(no of clusters)
```


#### How to execute K-means Model
```
Run main.py    and      uncomment
kmeans = KmeansAnomalyDetection()
kmeans.Kmeans_anomaly(no of clusters)
```
