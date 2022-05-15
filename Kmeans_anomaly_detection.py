from sklearn.cluster import KMeans
from pandas import np
from PELL_street_lighting_data import DynamicDataManager
import time
import pandas as pd


class KmeansAnomalyDetection:
    begin_time = time.time()
    data_mgr = DynamicDataManager()
    df = data_mgr.load_jsons()

    def Kmeans_anomaly(self, no_clusters):
        # begin_time = time.time()
        kmeans = KMeans(n_clusters=no_clusters, init='k-means++')
        kmeans.fit(self.df)

        # Predicting the clusters
        labels = kmeans.predict(self.df)

        # --------------------------->>>>>>>> Distance Calculation <<<<---------------------
        X_dist = kmeans.transform(self.df) ** 2
        # panda_DF = pd.DataFrame(X_dist.sum(axis=1).round(2), columns=['sqdist'])
        dist_sqr = (X_dist.sum(axis=1).round(2))
        self.df['sqr_dist'] = dist_sqr
        self.df['cluster'] = kmeans.labels_

        # print(panda_DF.head(10))

        # ---------------- Anomaly score calculation with respect to each cluster --------------

        k = [0, 1]
        for x in k:
            pd.options.mode.chained_assignment = None
            filtered_DF = self.df[(self.df['cluster'] == k.index(x))]
            # print(filtered_DF)
            # print(filtered_DF.describe())

            # calculating the mean of distance column
            filtered_DF['mean_dist'] = filtered_DF['sqr_dist'].mean()

            # Calculating the anomaly score by dividing distance column by mean_distance column
            filtered_DF['anomaly_score'] = filtered_DF['sqr_dist'] / filtered_DF['mean_dist']

            # pd.set_option('display.max_columns', None)
            # print(filtered_DF.head(20))

            # -------------------- IQR calculation -----------------#

            Q3, Q1 = np.percentile(filtered_DF['anomaly_score'], [75, 25])
            # print(Q3)
            # print(Q1)
            IQR = Q3 - Q1
            # print(IQR)

            minimumThreshold = Q1 - 1.5 * IQR
            # print(minimumThreshold)
            # print('minimum threshold = ' + str(minimumThreshold))

            maximumThreshold = Q3 + 1.5 * IQR
            # print('maximum threshold = ' + str(maximumThreshold))

            # ---------------- Anomaly filtration by using IQR values --------------------------#

            minThreshold = minimumThreshold
            maxThreshold = maximumThreshold
            filtered_anomaly = filtered_DF[
                (filtered_DF['anomaly_score'] > maxThreshold) | (filtered_DF['anomaly_score'] < minThreshold)]

            print(filtered_anomaly.shape[0])

    print('Elapsed time is %f seconds.' % (time.time() - begin_time))
