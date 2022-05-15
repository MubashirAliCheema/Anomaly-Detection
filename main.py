from PELL_street_lighting_data import DynamicDataManager
from dbscan_anomaly_detection import DBSCANAnomalyDetection
from OPTICS_anomaly_detection import OPTICSAonamyDetection
from synthetic_anomaly_injection import SyntheticAnomalies
from Kmeans_anomaly_detection import KmeansAnomalyDetection
import pandas as pd


def main():
    
    # Anomaly detection with K-means
    # kmeans = KmeansAnomalyDetection()
    # kmeans.Kmeans_anomaly(2)

    # Anomaly detection with DBSCAN
    # dbscan = DBSCANAnomalyDetection()
    # dbscan.dbscan_anomaly(0.35, 12)

    # Anomaly detection with OPTICS
    # optics = OPTICSAonamyDetection()
    # optics.optics_anomaly(0.1)

    # Synthetic anomalies injection

    artificial_anomalies = SyntheticAnomalies()

    # call the injection process according to the pre-defined scenarios

    # S1: To handle random positive high peaks at the night time.
    S1 = artificial_anomalies.synthetic_anomalies_S1()
    show_result(S1)

    # S2: To handle random negative high peaks at the day time.
    # S2 = artificial_anomalies.synthetic_anomalies_S2()
    # show_result(S2)

    # S3: To handle random low peaks at the night time.
    # S3 = artificial_anomalies.synthetic_anomalies_S3()
    # show_result(S3)

    # S4: To handle continuous low peaks at the night.
    # S4 = artificial_anomalies.synthetic_anomalies_S4()
    # show_result(S4)

    # S5: To handle random high peaks at the day time.
    # S5 = artificial_anomalies.synthetic_anomalies_S5()
    # show_result(S5)

    # S6: To handle continuous high peaks at the day time.
    # S6 = artificial_anomalies.synthetic_anomalies_S6()
    # show_result(S6)


def show_result(filtered_df):
    pd.set_option('display.max_rows', 20000)
    print(filtered_df.head(18000))


if __name__ == "__main__":
    main()
