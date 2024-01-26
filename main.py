from kidney_disease_classification import logger
from kidney_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>> {STAGE_NAME} started <<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> {STAGE_NAME} completed <<<<<')
except Exception as e:
    logger.error(f'Error in {STAGE_NAME} stage')
    raise e
