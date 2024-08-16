import os

# Define the root directory
ROOT = 'data'

# Define the training and testing directories
TRAIN_DIR = f'{ROOT}/train'
TEST_DIR = f'{ROOT}/test'

# Define the image size
IMAGE_SIZE = (448, 448)

CLASS_NAME = sorted(list(os.listdir(TRAIN_DIR)))
