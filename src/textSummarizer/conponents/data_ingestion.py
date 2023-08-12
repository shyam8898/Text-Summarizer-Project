import os
import urllib.request as request
import zipfile
import shutil
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def get_data(self):
        if not os.path.exists(self.config.local_data_file):
            source_path = self.config.source_URL
            destination_path = self.config.local_data_file
            shutil.copy(source_path,destination_path)
            logger.info(f"Data copied successfully: {destination_path}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}") 

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Data unzipped successfully: {unzip_path}")