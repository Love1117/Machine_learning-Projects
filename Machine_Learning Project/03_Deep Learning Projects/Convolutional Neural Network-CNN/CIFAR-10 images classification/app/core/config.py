from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"
DATABASE_URL = "sqlite:///./CIFAR-10_images_classification.db"
