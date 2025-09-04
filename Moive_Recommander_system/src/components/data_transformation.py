import sys
import os
from dataclasses import dataclass
from src.logger import logging
import ast
from src.exception import CustomException



import numpy as np
import pandas as pd

file1=os.path.join("..","data","tmdb_5000_credits.csv")
file2=os.path.join("..","data","tmdb_5000_movies.csv")

try :
    movie=pd.read_csv(file2)
    credits=pd.read_csv(file1)
    logging.info(f"Data Loaded Successfully")
    logging.info(f"Before Cleaning")
    logging.info(f"Movie Shape{movie.shape},Credits Shape :{credits.shape}")

    # Merge datasets on 'title'
    df = movie.merge(credits, on="title")

    logging.info("✅ Data Merged Successfully")
    logging.info(f"Merged Data Shape: {df.shape}")

except Exception as e:
    logging.error("❌ Error loading data")
    raise CustomException(e,sys)


