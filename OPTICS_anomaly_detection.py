from pyclbr import Class
from sklearn.cluster import OPTICS
from pandas import np
from PELL_street_lighting_data import DynamicDataManager


class OPTICSAonamyDetection:
    data_mgr = DynamicDataManager()
    df = data_mgr.load_jsons()

    def optics_anomaly(self, eps):
        model = OPTICS(eps=eps, cluster_method='dbscan', metric='minkowski')
        model.fit(self.df)
        labels = model.labels_
        no_clusters = len(np.unique(labels))
        no_noise = list(labels).count(-1)

        print('Estimated number of clusters: %d' % no_clusters)
        print('Estimated number of noise points: %d' % no_noise)

        outliers_DF = self.df[labels == -1]
        print(outliers_DF)




