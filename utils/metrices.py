import os
import csv
import time
from threading import Lock
METRICES_DIR ="data/metrics"
METRICES_FILE = os.path.join(METRICES_DIR, "metrics.csv")
file_lock = Lock()
os.makedirs(METRICES_DIR, exist_ok=True)
if not os.path.exists(METRICES_FILE):
    with open(METRICES_FILE, "W",newline="")as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp",
            "model",
            "latency",
            "response_length"
        ])
def log_metrics(model: str, latency: float, response_length: int):
    with file_lock:
        with open(METRICES_FILE,"a", newline="")as f:
            writer = csv.writer(f)
            writer.writerow([
                time.time(),
                model,
                round(latency, 3),
                response_length
            ])