from PELL_street_lighting_data import DynamicDataManager
from dbscan_anomaly_detection import DBSCANAnomalyDetection
from OPTICS_anomaly_detection import OPTICSAonamyDetection
from synthetic_anomaly_injection import SyntheticAnomalies


def main():
    # data_mgr = DynamicDataManager()
    # df = data_mgr.load_jsons()

    # Anomaly detection with DBSCAN
    # dbscan = DBSCANAnomalyDetection()
    # dbscan.dbscan_anomaly(0.35, 12)

    # Anomaly detection with OPTICS
    # optics = OPTICSAonamyDetection()
    # optics.optics_anomaly(0.1)

    # Synthetic anomalies injection

    artificial_anomalies = SyntheticAnomalies()
    list_of_anomalies = [220, 230, 250, 240, 270]
    artificial_anomalies.synthetic_anomalies(list_of_anomalies)


if __name__ == "__main__":
    main()
