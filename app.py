from src.Student_performance_indicator.logger import logging
from src.Student_performance_indicator.exception import CustomEception
import sys
from src.Student_performance_indicator.components.data_ingestion import DataIngestion
from src.Student_performance_indicator.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom exception")
        raise CustomEception(e,sys)
