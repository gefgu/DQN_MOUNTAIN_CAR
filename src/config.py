from pathlib import Path
from torch.cuda import is_available

N_STATE_FEATURES = 2

N_ACTIONS = 3

N_FRAMES_TO_TRAIN = 1000000

MIN_EPSILON = 0.1

ENV_NAME = "MountainCar-v0"

BATCH_SIZE = 32

DISCOUNT = 0.99

LEARNING_RATE = 0.00025

GRADIENT_MOMENTUM = 0.95

EXPERIENCE_SIZE = N_FRAMES_TO_TRAIN // 10

MODEL_SAVE_PATH = Path("models/") 

DEVICE = ("cuda" if is_available else "cpu")