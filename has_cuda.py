# run to see if cuda is available
import torch as t

print(f"cuda available: {t.cuda.is_available()}")
print(f"gpus: {t.cuda.device_count()}")
