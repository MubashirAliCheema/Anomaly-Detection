from pandas import np
from sklearn.cluster import DBSCAN
from PELL_street_lighting_data import DynamicDataManager


class DBSCANAnomalyDetection:
    data_mgr = DynamicDataManager()
    df = data_mgr.load_jsons()

    def dbscan_anomaly(self, eps, min_samples):
        # begin_time = time.time()
        db = DBSCAN(eps=eps, min_samples=min_samples)
        db.fit(self.df)
        labels = db.labels_

        # Creating a numpy array with all values set to false by default
        core_samples_mask = np.zeros_like(labels, dtype=bool)

        # Setting core and border points (all points that are not -1) to True
        core_samples_mask[db.core_sample_indices_] = True

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)

        # end_time = time.time()
        # print('Elapsed time is %f seconds.' % (time.time() - begin_time))

        print('Estimated number of clusters: %d' % n_clusters_)
        print('Estimated number of noise points: %d' % n_noise_)

        # outlier dataframe
        outliers_DF = self.df[db.labels_ == -1]
        print(outliers_DF)
