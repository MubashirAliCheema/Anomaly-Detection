from pyspark.sql import *
import pyspark.sql.functions as psf
import pandas as pd



class DynamicDataManager:

    def load_jsons(self):
        spark = SparkSession.builder \
            .master("local[1]") \
            .appName("DBSCANAnomalyDetection") \
            .getOrCreate()

        dataFrameJSON = spark.read \
            .option("timestampFormat", "yyyy/MM/dd HH:mm:ss") \
            .json("PELL_Data_Fake_Anomaly")

        df1 = dataFrameJSON.select(
            dataFrameJSON["UrbanDataset"]["specification"]["name"].alias("name"),
            # dataFrameJSON["UrbanDataset"]["context"]["timestamp"].alias("timestamp"),
            psf.explode(dataFrameJSON["UrbanDataset"]["values"]["line"]).alias("data"))

        df2 = df1.select(
            # df1["timestamp"],
            df1["data"]["period"]["start_ts"].alias("start_time"),
            df1["data"]["period"]["end_ts"].alias("end_time"),
            psf.map_from_entries(df1["data"]["property"]).alias("prop"))

        df3 = df2.withColumn("ActiveEnergy", df2["prop"]["ActiveEnergy"].cast("double")) \
            .withColumn("ActivePowerPhase1", df2["prop"]["ActivePowerPhase1"].cast("double")) \
            .withColumn("ActivePowerPhase2", df2["prop"]["ActivePowerPhase2"].cast("double")) \
            .withColumn("ActivePowerPhase3", df2["prop"]["ActivePowerPhase3"].cast("double")) \
            .drop(df2["prop"])
        # df3.printSchema()
        # df3.show(5, truncate=False)
        # print(df3.count())

        panda_DF = df3.select("start_time", "ActiveEnergy").toPandas()
        panda_DF['start_time'] = pd.to_datetime(panda_DF['start_time'], format='%Y-%m-%d %H:%M:%S')
        panda_DF['dayORnight'] = panda_DF['start_time'].apply(
            lambda x: '0' if int(x.strftime('%H')) > 20 or int(x.strftime('%H')) < 6 else '1')
        # panda_DF['Time'] = panda_DF['Time'].astype(str).astype(int)
        panda_DF.set_index('start_time', drop=True, inplace=True)
        print(panda_DF.head())

        return panda_DF
