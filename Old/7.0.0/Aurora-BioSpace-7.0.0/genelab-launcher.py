import webbrowser
import os
import subprocess
import sys
import platform
import threading
import time
import tarfile
import zipfile
import shutil
import tempfile

# Define your current local app version here
CURRENT_VERSION = "v7.0.0" 
GITHUB_REPO = "codemaster-ar/aurora"
NODE_VERSION = "v24.0.0"
NODE_DIR_NAME = "local_node"

# Try to import required libraries, handle gracefully if missing
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as rprint
    from rich.prompt import Prompt
    from rich.align import Align
    import requests
except ImportError:
    print("Error: The 'rich' and 'requests' libraries are required.")
    print("Please install them using: pip install rich requests")
    sys.exit(1)

console = Console()
logging_enabled = False
electron_process = None

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
                update_msg = (
                    f"Current Version: [bold red]{CURRENT_VERSION}[/bold red]\n"
                    f"Latest Version:  [bold green]{latest_version}[/bold green]\n\n"
                    f"Download here: [underline cyan]https://github.com/{GITHUB_REPO}/releases[/underline cyan]"
                )
                console.print(Panel(
                    Align.center(update_msg),
                    title="[bold yellow]⚠️ Update Available[/bold yellow]",
                    border_style="yellow",
                    expand=False,
                    padding=(1, 2)
                ))
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

    header_content = (
        f"[bold cyan]{aurora_art}[/bold cyan]\n"
        "✨ [bold italic violet]AI-powered[/bold italic violet] [bold italic sea_green2]Bioscience Dashboard[/bold italic sea_green2] ✨\n"
        "💻 [dim]Developed by [/dim][bold link=https://quantal-labs.com target=_blank]Quantal Labs[/bold link]\n\n"
        "[grey50]powered by NASA OSDR API - Only Google Auth accepted[/grey50]\n"
        f"[bold dim white]Local Version: {CURRENT_VERSION}[/bold dim white]"
    )

    console.print(Panel(
        Align.center(header_content),
        border_style="bold magenta",
        padding=(1, 4)
    ))

def show_about():
    about_text = (
        f"[bold cyan]Aurora Bioscience Dashboard[/bold cyan]\n"
        f"Version: [bold green]{CURRENT_VERSION}[/bold green]\n"
        f"Developer: [bold link=https://quantal-labs.com]Quantal Labs[/bold link]\n"
        f"Repository: [underline]https://github.com/{GITHUB_REPO}[/underline]\n\n"
        "An advanced interface for exploring biological space research data."
    )
    console.print(Panel(Align.center(about_text), title="[bold violet]About Aurora[/bold violet]", border_style="violet", expand=False))

def ensure_node_modules(app_dir):
    """Checks if node_modules exists, runs npm install with a loader if it doesn't."""
    # Ensure Node 24 is installed
    install_node_locally(app_dir)

    node_modules_path = os.path.join(app_dir, "node_modules")

    if not os.path.exists(node_modules_path):
        console.print(Panel(f"[bold yellow]📦 node_modules missing in {app_dir}. Initializing installation...[/bold yellow]", border_style="yellow"))

        with console.status("[bold cyan]Running 'npm install'... This might take a moment...[/bold cyan]", spinner="dots"):
            try:
                result = subprocess.run(
                    "npm install", 
                    cwd=app_dir, 
                    shell=True, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE,
                    text=True,
                    env=get_node_env(app_dir)
                )

                if result.returncode == 0:
                    console.print(Panel("[bold green]✅ Dependencies successfully installed![/bold green]", border_style="green"))
                else:
                    console.print(Panel(f"[bold red]❌ npm install failed![/bold red]\n[dim red]{result.stderr}[/dim red]", border_style="red"))
                    sys.exit(1)

            except Exception as e:
                console.print(Panel(f"[bold red]❌ Failed to execute npm install:[/bold red] {e}", border_style="red"))
                sys.exit(1)

def stream_logs(pipe):
    """Reads lines from the process output pipe and selectively displays them."""
    global logging_enabled
    try:
        with pipe:
            for line in iter(pipe.readline, ''):
                if logging_enabled:
                    console.print(f"[dim white]🧪 Engine Log:[/dim white] {line.strip()}")
    except Exception:
        pass

def launch_electron(app_dir):
    """Launch the Electron app process."""
    global electron_process
    try:
        console.print(Panel(
            Align.center(f"[bold green]🚀 Launching Genelab Core Engine...[/bold green]\n[dim]Path: {app_dir}[/dim]"),
            border_style="green"
        ))

        electron_process = subprocess.Popen(
            "npm start", 
            cwd=app_dir, 
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            env=get_node_env(app_dir)
        )

        stdout_thread = threading.Thread(target=stream_logs, args=(electron_process.stdout,), daemon=True)
        stderr_thread = threading.Thread(target=stream_logs, args=(electron_process.stderr,), daemon=True)
        stdout_thread.start()
        stderr_thread.start()

    except Exception as e:
        console.print(Panel(f"[bold red]❌ Error launching Genelab Engine:[/bold red] {e}", border_style="red"))
        sys.exit(1)

def main():
    global logging_enabled, electron_process
    display_header()
    check_for_updates()

    # 1. System Notification popup/box
    msg = "Created by Quantal-Labs, founded by Codemaster-AR. Contact: contact@quantal-labs.com"

    if platform.system() == "Darwin":
        os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
    else:
        console.print(Panel(
            Align.center(f"[yellow]{msg}[/yellow]"), 
            title="[bold blue]💻 System Notice[/bold blue]", 
            border_style="blue",
            padding=(1, 2)
        ))

    # 2. Workspace Setup
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(script_dir, "genelab")

    if not os.path.exists(os.path.join(app_dir, "package.json")):
        app_dir = script_dir

    ensure_node_modules(app_dir)

    # 3. Boot Electron Core with background output tracking
    launch_electron(app_dir)

    # Help Menu layout
    help_menu = (
        "[bold cyan]Available Terminal Controls:[/bold cyan]\n"
        " ❖ [bold green]logging[/bold green] : Stream raw dashboard logs   ❖ [bold green]about[/bold green] : Application details\n"
        " ❖ [bold green]launch[/bold green] : Relaunch the Electron app    ❖ [bold green]quit / exit[/bold green] : Safe shutdown\n"
        " ❖ [bold green]Ctrl + C[/bold green] : Hard exit.                 ❖ [bold green]website[/bold green] : Opens project website\n"
    )
    console.print(Panel(Align.center(help_menu), title="[bold dim white]Terminal Interface Active[/bold dim white]", border_style="dim white"))

    # Interactive loop
    while True:
        try:
            cmd = Prompt.ask("\n[bold magenta]aurora-sys[/bold magenta]").strip().lower()

            if cmd in ['quit', 'exit']:
                raise KeyboardInterrupt

            elif cmd == 'logging':
                logging_enabled = True
                console.print(Panel(
                    Align.center("[bold cyan]✨ Log Stream Active ✨\n[bold yellow]Press Control+C to stop streaming logs and return to commands.[/bold yellow]"),
                    border_style="cyan"
                ))

                # Dedicated sub-loop keeping the terminal open strictly for watching logs
                try:
                    while True:
                        time.sleep(0.5)
                        # Check if process died in the background while viewing logs
                        if electron_process.poll() is not None:
                            console.print("[bold red]⚠️ Core process ended while streaming logs.[/bold red]")
                            break
                except KeyboardInterrupt:
                    logging_enabled = False
                    console.print("\n")
                    console.print(Panel("[bold green]↩️ Exited Log Stream. Shell controls restored.[/bold green]", border_style="green"))

            elif cmd == 'about':
                show_about()

            elif cmd == 'launch':
                if electron_process:
                    console.print(Panel(
                        Align.center("[bold yellow]🔄 Relaunching Electron app...[/bold yellow]"),
                        border_style="yellow"
                    ))
                    electron_process.terminate()
                    electron_process.wait()
                launch_electron(app_dir)

            elif cmd == '':
                continue
            elif cmd == 'github-repo':
                webbrowser.open("https://github.com/Codemaster-AR/Aurora-7.0.0")  
            elif cmd == 'website':
                webbrowser.open("https://quantal-labs.com/projects/aurora-biospace/")                    
            else:
                console.print("[bold red]❓ Unknown terminal command. Type 'about', 'logging', 'launch', or 'exit'.[/bold red]")

        except (KeyboardInterrupt, EOFError):
            console.print("\n")
            console.print(Panel(Align.center("[bold red]🛑 Shutting down Aurora Environment & Killing Assets...[/bold red]"), border_style="red"))
            if electron_process:
                electron_process.terminate()
            sys.exit(0)

if __name__ == "__main__":
    main()