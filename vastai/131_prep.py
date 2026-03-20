from dotenv import load_dotenv
import os
import paramiko
from pathlib import Path
from fabric import Connection

from utils import (
    load_settings,
    make_connection,
)


settings = load_settings()

with make_connection(settings) as conn:
    conn.put(
        "chapter1_transformer_interp/exercises/.env",
        remote=f"{settings.remote_repo_dir}/chapter1_transformer_interp/exercises/.env",
    )
    conn.run(
        f"cd {settings.remote_repo_dir} && {settings.remote_python} chapter1_transformer_interp/exercises/part31_linear_probes/preparations.py",
        warn=True,
        hide=False,
    )
