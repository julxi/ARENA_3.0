from dotenv import load_dotenv
import os
from vastai_sdk import VastAI
from fabric import Connection

# get
load_dotenv(".env")
load_dotenv(".env.local")
load_dotenv("vastai_setup/.env.vastai")


# get ip_addr & port
vastai_api_key = os.getenv("VASTAI_API_KEY")
vastai_instance_id = os.getenv("VASTAI_INSTANCE_ID")
vast_sdk = VastAI(api_key=vastai_api_key)
instance = vast_sdk.show_instance(id=vastai_instance_id)
if instance == "":
    raise Exception(f"No instance with id {vastai_instance_id}")
ip_addr = instance["public_ipaddr"]
port = instance["ports"]["22/tcp"][0]["HostPort"]

# create configuration for vs code
identity_file = os.getenv("SSH_IDENTITY_FILE")
ssh_config_dir = os.getenv("SSH_CONFIG_DIR")
ssh_config_name = os.getenv("SSH_CONFIG_NAME")
ssh_config_file = os.path.join(ssh_config_dir, ssh_config_name)
os.makedirs(ssh_config_dir, exist_ok=True)
ssh_host_alias = os.getenv("SSH_HOST_ALIAS")
ssh_user = os.getenv("SSH_USER")
with open(ssh_config_file, "w") as f:
    f.write(
        f"""Host {ssh_host_alias}
    HostName {ip_addr}
    User {ssh_user}
    IdentityFile {identity_file}
    Port {port}
"""
    )
print(f"SSH configuration has been written to {ssh_config_file}")

# setup repo in vm
remote_workdir = os.getenv("REMOTE_WORKDIR")
remote_python = os.getenv("REMOTE_PYTHON")
repo_url = os.getenv("REPO_URL")
repo_name = os.getenv("REPO_NAME")

with Connection(
    host=ip_addr,
    user=ssh_user,
    port=port,
    connect_kwargs={"key_filename": identity_file},
) as conn:
    conn.run(f"mkdir -p {remote_workdir}", warn=True)
    conn.run(
        f"""
        cd {remote_workdir}
        if [ -d {repo_name}/.git ]; then
            cd {repo_name} && git pull --rebase
        else
            git clone {repo_url}
        fi
        """,
        warn=True,
    )
    conn.run(
        f"uv pip install --python {remote_python} -r {remote_workdir}/{repo_name}/requirements.txt",
        warn=True,
    )
    conn.put(".env.local", remote=f"{remote_workdir}/{repo_name}/.env.local")
