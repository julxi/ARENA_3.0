# run from repo root
from dotenv import load_dotenv
from pathlib import Path
import git
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import snapshot_download
import torch as t
import os


root_dir = Path.cwd()
print("root_dir:", root_dir)
exercises_dir = root_dir / "chapter1_transformer_interp" / "exercises"

load_dotenv(dotenv_path=str(exercises_dir / ".env"))
print(str(exercises_dir / ".env"))


# pull repos
GOT_ROOT = exercises_dir / "geometry-of-truth"  # geometry-of-truth repo
DD_ROOT = exercises_dir / "deception-detection"  # deception-detection repo
if not GOT_ROOT.exists() or not GOT_ROOT.joinpath(".git").exists():
    git.Repo.clone_from("https://github.com/saprmarks/geometry-of-truth.git", GOT_ROOT)
if not DD_ROOT.exists() or not DD_ROOT.joinpath(".git").exists():
    git.Repo.clone_from(
        "https://github.com/ApolloResearch/deception-detection.git", DD_ROOT
    )


# download models
HF_TOKEN = os.getenv("HF_TOKEN")
assert (
    HF_TOKEN
), "Please set HF_TOKEN in your chapter1_transformer_interp/exercises/.env file"

snapshot_download(
    repo_id="meta-llama/Llama-2-13b-hf",
)
# snapshot_download(
#    repo_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
# )
