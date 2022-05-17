# Anomaly Detection in Public Street Lighting using Clustering Algorithms
### Requirement
- Data set is converted from JSON to Spark DataFrame by using **PySpark=3.2.1.**
- To implement the clustering algorithm, Spark DataFrame is converted into the Pandas DataFrame and **scikit-learn=0.24.2** is exploited.
### Running code classes in Anomaly-Detection project
Project repository contains data set folder with name “PELL_Data_with_Synthetic_Anomalies” and implementation files for algorithms K-means, DBSCAN, OPTICS, and synthetic anomaly injection.
#### How to execute K-means Model
```
Run main.py    and      uncomment
kmeans = KmeansAnomalyDetection()
kmeans.Kmeans_anomaly(no of clusters)
```
#### How to execute DBSCAN Model
```
Run main.py    and      uncomment
dbscan = DBSCANAnomalyDetection()
dbscan.dbscan_anomaly(eps_value, min_sample_value)
```
#### How to execute OPTICS Model
```
Run main.py    and      uncomment
optics = OPTICSAonamyDetection()
optics.optics_anomaly(eps_value)
```
### Artificial Anomalies
In order to evaluate the performance of cluster algorithms for anomaly detection from street lighting data, we introduced six anomalous scenarios w.r.t. street lighting domain. By following these domain specific scenarios, synthetic anomalies are automatically inserted into the original data set. This helps to determine the ability of clustering algorithms to detect anomalies by using some standard evaluation metrics.
- The file name “synthetic_anomaly_injection.py” contains the implementation for all the six scenarios to automatically insert synthetic anomalies.
#### How to execute synthetic anomaly injection algorithm
```
Run main.py    and   uncomment  whatever the scenario you want  to invoke
```
