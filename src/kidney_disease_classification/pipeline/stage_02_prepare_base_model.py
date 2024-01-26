from kidney_disease_classification.config.configuration import ConfigurationManager
from kidney_disease_classification.components.prepare_base_model import PrepareBaseModel
from kidney_disease_classification import logger

STAGE_NAME = 'Prepare Base Model Stage'


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepareBaseModelConfig = config.get_prepare_base_model_config()
            prepareBaseModel = PrepareBaseModel(config=prepareBaseModelConfig)
            prepareBaseModel.get_base_model()
            prepareBaseModel.updated_base_model()
        except Exception as e:
            logger.error("Error in prepare base model")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> {STAGE_NAME} started <<<<<')
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> {STAGE_NAME} completed <<<<<')
    except Exception as e:
        logger.error(f'Error in {STAGE_NAME} stage')
        raise e
