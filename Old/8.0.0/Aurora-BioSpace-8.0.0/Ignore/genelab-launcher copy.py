#!/usr/bin/env python3
import os
import subprocess
import sys
import platform
import tarfile
import zipfile
import shutil
import tempfile
import requests

# Define your current local app version here
CURRENT_VERSION = "v6.0.0" 
GITHUB_REPO = "codemaster-ar/aurora"
NODE_VERSION = "v24.0.0"
NODE_DIR_NAME = "local_node"

# Try to import required libraries, handle gracefully if missing
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as rprint
except ImportError:
    print("Error: The 'rich' and 'requests' libraries are required.")
    print("Please install them using: pip install rich requests")
    sys.exit(1)

console = Console()

def get_node_env(app_dir):
    """Returns a dictionary with PATH updated to include local node."""
    # Windows puts binaries in root, others in bin/
    if platform.system().lower() == "windows":
        local_node_bin = os.path.join(app_dir, NODE_DIR_NAME)
    else:
        local_node_bin = os.path.join(app_dir, NODE_DIR_NAME, "bin")

    env = os.environ.copy()
    # Use os.pathsep to handle platform-specific path separators
    env["PATH"] = f"{local_node_bin}{os.pathsep}{env.get('PATH', '')}"
    return env

def install_node_locally(app_dir):
    """Downloads and extracts Node 24 for the current platform."""
    local_node_dir = os.path.join(app_dir, NODE_DIR_NAME)
    if os.path.exists(local_node_dir):
        return
        
    console.print(Panel(f"[bold yellow]📦 Node.js {NODE_VERSION} not found. Installing locally...[/bold yellow]", border_style="yellow"))
    
    # Determine OS/Arch/Format for binary
    os_system = platform.system().lower() # 'windows', 'linux', 'darwin'
    arch = platform.machine().lower()
    
    if "arm64" in arch or "aarch64" in arch:
        arch_str = "arm64"
    else:
        arch_str = "x64"

    if os_system == "windows":
        os_str = "win"
        ext = "zip"
    elif os_system == "darwin":
        os_str = "darwin"
        ext = "tar.gz"
    else: # Linux
        os_str = "linux"
        ext = "tar.gz"
        
    url = f"https://nodejs.org/dist/{NODE_VERSION}/node-{NODE_VERSION}-{os_str}-{arch_str}.{ext}"
    
    with tempfile.TemporaryDirectory() as tmpdir:
        archive_path = os.path.join(tmpdir, f"node.{ext}")
        
        with console.status(f"[bold cyan]Downloading {NODE_VERSION}...[/bold cyan]", spinner="dots"):
            response = requests.get(url, stream=True)
            if response.status_code != 200:
                console.print(f"[bold red]❌ Failed to download Node binary ({response.status_code}).[/bold red]")
                sys.exit(1)
            with open(archive_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
        with console.status(f"[bold cyan]Extracting Node.js...[/bold cyan]", spinner="dots"):
            if ext == "tar.gz":
                with tarfile.open(archive_path, "r:gz") as tar:
                    tar.extractall(path=tmpdir)
                    extracted_dir = os.path.join(tmpdir, f"node-{NODE_VERSION}-{os_str}-{arch_str}")
                    shutil.move(extracted_dir, local_node_dir)
            else: # zip
                with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                    zip_ref.extractall(path=tmpdir)
                    extracted_dir = os.path.join(tmpdir, f"node-{NODE_VERSION}-{os_str}-{arch_str}")
                    shutil.move(extracted_dir, local_node_dir)
                
    console.print(Panel("[bold green]✅ Node.js successfully installed locally![/bold green]", border_style="green"))

def check_for_updates():
    """Checks GitHub Releases for a newer version string."""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    try:
        response = requests.get(url, timeout=1.5)
        if response.status_code == 200:
            latest_release = response.json()
            latest_version = latest_release.get("tag_name", "").strip()
            
            if latest_version and latest_version != CURRENT_VERSION:
                console.print(Panel(
                    f"[bold yellow]⚠️  A new update is available![/bold yellow]\n\n"
                    f"Current Version: [red]{CURRENT_VERSION}[/red]\n"
                    f"Latest Version:  [green]{latest_version}[/green]\n\n"
                    f"Run 'brew update && brew upgrade' to update.",
                    title="[bold yellow]Update Notice[/bold yellow]",
                    border_style="yellow"
                ))
                console.print()
    except Exception:
        pass

def display_header():
    aurora_art = r"""
    ___                                 
   /   |  __  ___________  __________ _ 
  / /| | / / / / ___/ __ \/ ___/ __ `/ 
 / ___ |/ /_/ / /  / /_/ / /  / /_/ /  
/_/  |_|\__,_/_/   \____/_/   \__,_/   
    """
    console.print(aurora_art, style="bold cyan")
    console.print("    ✨ [bold italic violet]AI-powered[/bold italic violet] [bold italic sea_green2]Bioscience Dashboard[/bold italic sea_green2] ✨")
    console.print("       [grey50]powered by NASA OSDR API - Only Google Auth accepted[/grey50]\n")
    console.print(f"       [bold dim white]Local Version: {CURRENT_VERSION}[/bold dim white]\n")
    console.print("[bold magenta]=[/bold magenta]" * 50)
    console.print()

def main():
    display_header()
    check_for_updates()

    msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
    
    if platform.system() == "Darwin":
        os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
    else:
        console.print(Panel(
            f"[yellow]{msg}[/yellow]", 
            title="[bold blue]System Notice[/bold blue]", 
            border_style="blue"
        ))
        console.print()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(script_dir, "genelab")
    if not os.path.exists(os.path.join(app_dir, "package.json")):
        app_dir = script_dir

    # Install Node 24 locally
    install_node_locally(app_dir)

    try:
        console.print(f"[bold green]🚀 Launching Genelab from:[/bold green] [underline]{app_dir}[/underline]\n")
        subprocess.run("npm start", cwd=app_dir, shell=True, env=get_node_env(app_dir))
    except Exception as e:
        console.print(f"[bold red]❌ Error launching Genelab:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
