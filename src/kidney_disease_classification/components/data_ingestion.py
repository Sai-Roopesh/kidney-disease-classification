import os
import zipfile
import gdown
from kidney_disease_classification import logger
from kidney_disease_classification.utils.common import get_size
from kidney_disease_classification.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:

        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs('artifacts/data_ingestion', exist_ok=True)
            logger.info(
                f"Downloading dataset from {dataset_url} to {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?export=download&id='
            gdown.download(prefix + file_id, str(zip_download_dir))

            logger.info(
                f"Downloaded dataset from {dataset_url} to {zip_download_dir}")

        except Exception as e:
            logger.error(
                f"Error downloading dataset from {dataset_url} to {zip_download_dir}")
            raise e

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
