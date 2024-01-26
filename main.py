from kidney_disease_classification import logger
from kidney_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidney_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>> {STAGE_NAME} started <<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> {STAGE_NAME} completed <<<<<')
except Exception as e:
    logger.error(f'Error in {STAGE_NAME} stage')
    raise e


STAGE_NAME = 'Prepare Base Model Stage'

try:
    logger.info(f'>>>>> {STAGE_NAME} started <<<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> {STAGE_NAME} completed <<<<<')
except Exception as e:
    logger.error(f'Error in {STAGE_NAME} stage')
    raise e
