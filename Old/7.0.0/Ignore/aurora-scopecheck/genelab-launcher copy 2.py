# # # #!/usr/bin/env python3
# # # import os
# # # import subprocess
# # # import sys
# # # import platform

# # # # Try to import rich, install it if missing or handle gracefully
# # # try:
# # #     from rich.console import Console
# # #     from rich.panel import Panel
# # #     from rich import print as rprint
# # # except ImportError:
# # #     print("Error: The 'rich' library is required. Please install it using: pip install rich")
# # #     sys.exit(1)

# # # console = Console()

# # # def display_header():
# # #     # Adding 'r' before the quotes makes it a raw string and fixes the SyntaxWarning
# # #     aurora_art = r"""
# # #     ___                                 
# # #    /   |  __  ___________  __________ _ 
# # #   / /| | / / / / ___/ __ \/ ___/ __ `/ 
# # #  / ___ |/ /_/ / /  / /_/ / /  / /_/ /  
# # # /_/  |_|\__,_/_/   \____/_/   \__,_/   
# # #     """
# # #     # Print the ASCII art with a nice cyan/purple gradient style vibe
# # #     console.print(aurora_art, style="bold cyan")
# # #     console.print("[bold magenta]=[/bold magenta]" * 50)
# # #     console.print()

# # # def main():
# # #     display_header()

# # #     # 1. Display the dialog based on OS
# # #     msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
    
# # #     if platform.system() == "Darwin":
# # #         # macOS: Use AppleScript for a native popup
# # #         os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
# # #     else:
# # #         # Linux / WSL / Others: Print a beautiful Rich Panel
# # #         console.print(Panel(
# # #             f"[yellow]{msg}[/yellow]", 
# # #             title="[bold blue]System Notice[/bold blue]", 
# # #             border_style="blue"
# # #         ))
# # #         console.print()

# # #     # 2. Get the current app directory (where package.json is located)
# # #     script_dir = os.path.dirname(os.path.abspath(__file__))
# # #     app_dir = os.path.join(script_dir, "genelab")
    
# # #     # Fallback check if script is already inside the genelab folder
# # #     if not os.path.exists(os.path.join(app_dir, "package.json")):
# # #         app_dir = script_dir

# # #     try:
# # #         # 3. Launch the Electron app using npm start
# # #         console.print(f"[bold green]🚀 Launching Genelab from:[/bold green] [underline]{app_dir}[/underline]\n")
# # #         subprocess.run("npm start", cwd=app_dir, shell=True)
# # #     except Exception as e:
# # #         console.print(f"[bold red]❌ Error launching Genelab:[/bold red] {e}")
# # #         sys.exit(1)

# # # if __name__ == "__main__":
# # #     main()
# # #!/usr/bin/env python3
# # import os
# # import subprocess
# # import sys
# # import platform

# # # Try to import rich, install it if missing or handle gracefully
# # try:
# #     from rich.console import Console
# #     from rich.panel import Panel
# #     from rich import print as rprint
# # except ImportError:
# #     print("Error: The 'rich' library is required. Please install it using: pip install rich")
# #     sys.exit(1)

# # console = Console()

# # def display_header():
# #     # ASCII Art for 'Aurora' (using raw string 'r' to prevent escape sequence warnings)
# #     aurora_art = r"""
# #     ___                                 
# #    /   |  __  ___________  __________ _ 
# #   / /| | / / / / ___/ __ \/ ___/ __ `/ 
# #  / ___ |/ /_/ / /  / /_/ / /  / /_/ /  
# # /_/  |_|\__,_/_/   \____/_/   \__,_/   
# #     """
# #     # Print the ASCII art
# #     console.print(aurora_art, style="bold cyan")
    
# #     # Print the fancy subtitle
# #     console.print("    ✨ [bold italic violet]AI-powered[/bold italic violet] [bold italic sea_green2]Bioscience Dashboard[/bold italic sea_green2] ✨\n")
    
# #     # Decorative divider line
# #     console.print("[bold magenta]=[/bold magenta]" * 50)
# #     console.print()

# # def main():
# #     display_header()

# #     # 1. Display the dialog based on OS
# #     msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
    
# #     if platform.system() == "Darwin":
# #         # macOS: Use AppleScript for a native popup
# #         os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
# #     else:
# #         # Linux / WSL / Others: Print a beautiful Rich Panel
# #         console.print(Panel(
# #             f"[yellow]{msg}[/yellow]", 
# #             title="[bold blue]System Notice[/bold blue]", 
# #             border_style="blue"
# #         ))
# #         console.print()

# #     # 2. Get the current app directory (where package.json is located)
# #     script_dir = os.path.dirname(os.path.abspath(__file__))
# #     app_dir = os.path.join(script_dir, "genelab")
    
# #     # Fallback check if script is already inside the genelab folder
# #     if not os.path.exists(os.path.join(app_dir, "package.json")):
# #         app_dir = script_dir

# #     try:
# #         # 3. Launch the Electron app using npm start
# #         console.print(f"[bold green]🚀 Launching Genelab from:[/bold green] [underline]{app_dir}[/underline]\n")
# #         subprocess.run("npm start", cwd=app_dir, shell=True)
# #     except Exception as e:
# #         console.print(f"[bold red]❌ Error launching Genelab:[/bold red] {e}")
# #         sys.exit(1)

# # if __name__ == "__main__":
# #     main()
# #!/usr/bin/env python3
# import os
# import subprocess
# import sys
# import platform

# # Try to import rich, install it if missing or handle gracefully
# try:
#     from rich.console import Console
#     from rich.panel import Panel
#     from rich import print as rprint
# except ImportError:
#     print("Error: The 'rich' library is required. Please install it using: pip install rich")
#     sys.exit(1)

# console = Console()

# def display_header():
#     # ASCII Art for 'Aurora' (using raw string 'r' to prevent escape sequence warnings)
#     aurora_art = r"""
#     ___                                 
#    /   |  __  ___________  __________ _ 
#   / /| | / / / / ___/ __ \/ ___/ __ `/ 
#  / ___ |/ /_/ / /  / /_/ / /  / /_/ /  
# /_/  |_|\__,_/_/   \____/_/   \__,_/   
#     """
#     # Print the ASCII art
#     console.print(aurora_art, style="bold cyan")
    
#     # Print the fancy subtitle
#     console.print("    ✨ [bold italic violet]AI-powered[/bold italic violet] [bold italic sea_green2]Bioscience Dashboard[/bold italic sea_green2] ✨")
    
#     # Print the API credit in gray
#     console.print("       [grey50]powered by NASA OSDR API - Only Google Auth accepted[/grey50]\n")
    
#     # Decorative divider line
#     console.print("[bold magenta]=[/bold magenta]" * 50)
#     console.print()

# def main():
#     display_header()

#     # 1. Display the dialog based on OS
#     msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
    
#     if platform.system() == "Darwin":
#         # macOS: Use AppleScript for a native popup
#         os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
#     else:
#         # Linux / WSL / Others: Print a beautiful Rich Panel
#         console.print(Panel(
#             f"[yellow]{msg}[/yellow]", 
#             title="[bold blue]System Notice[/bold blue]", 
#             border_style="blue"
#         ))
#         console.print()

#     # 2. Get the current app directory (where package.json is located)
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     app_dir = os.path.join(script_dir, "genelab")
    
#     # Fallback check if script is already inside the genelab folder
#     if not os.path.exists(os.path.join(app_dir, "package.json")):
#         app_dir = script_dir

#     try:
#         # 3. Launch the Electron app using npm start
#         console.print(f"[bold green]🚀 Launching Genelab from:[/bold green] [underline]{app_dir}[/underline]\n")
#         subprocess.run("npm start", cwd=app_dir, shell=True)
#     except Exception as e:
#         console.print(f"[bold red]❌ Error launching Genelab:[/bold red] {e}")
#         sys.exit(1)

# if __name__ == "__main__":
#     main()
#!/usr/bin/env python3
import os
import subprocess
import sys
import platform

# Define your current local app version here
CURRENT_VERSION = "v6.0.0" 
GITHUB_REPO = "codemaster-ar/aurora"

# Try to import required libraries, handle gracefully if missing
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as rprint
    import requests
except ImportError:
    print("Error: The 'rich' and 'requests' libraries are required.")
    print("Please install them using: pip install rich requests")
    sys.exit(1)

console = Console()

def check_for_updates():
    """Checks GitHub Releases for a newer version string."""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    try:
        # 1-second timeout to make sure it doesn't hang the app launch if offline
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
        # Silently pass on network/timeout issues so the launcher still opens the app offline
        pass

def display_header():
    # ASCII Art for 'Aurora' (using raw string 'r' to prevent escape sequence warnings)
    aurora_art = r"""
    ___                                 
   /   |  __  ___________  __________ _ 
  / /| | / / / / ___/ __ \/ ___/ __ `/ 
 / ___ |/ /_/ / /  / /_/ / /  / /_/ /  
/_/  |_|\__,_/_/   \____/_/   \__,_/   
    """
    # Print the ASCII art
    console.print(aurora_art, style="bold cyan")
    
    # Print the fancy subtitle
    console.print("    ✨ [bold italic violet]AI-powered[/bold italic violet] [bold italic sea_green2]Bioscience Dashboard[/bold italic sea_green2] ✨")
    
    # Print the API credit in gray
    console.print("       [grey50]powered by NASA OSDR API - Only Google Auth accepted[/grey50]\n")
    
    # Print local version indicator
    console.print(f"       [bold dim white]Local Version: {CURRENT_VERSION}[/bold dim white]\n")
    
    # Decorative divider line
    console.print("[bold magenta]=[/bold magenta]" * 50)
    console.print()

def main():
    display_header()
    
    # Run the GitHub version check
    check_for_updates()

    # 1. Display the dialog based on OS
    msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
    
    if platform.system() == "Darwin":
        # macOS: Use AppleScript for a native popup
        os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
    else:
        # Linux / WSL / Others: Print a beautiful Rich Panel
        console.print(Panel(
            f"[yellow]{msg}[/yellow]", 
            title="[bold blue]System Notice[/bold blue]", 
            border_style="blue"
        ))
        console.print()

    # 2. Get the current app directory (where package.json is located)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(script_dir, "genelab")
    
    # Fallback check if script is already inside the genelab folder
    if not os.path.exists(os.path.join(app_dir, "package.json")):
        app_dir = script_dir

    try:
        # 3. Launch the Electron app using npm start
        console.print(f"[bold green]🚀 Launching Genelab from:[/bold green] [underline]{app_dir}[/underline]\n")
        subprocess.run("npm start", cwd=app_dir, shell=True)
    except Exception as e:
        console.print(f"[bold red]❌ Error launching Genelab:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    # # # #!/usr/bin/env python3
# # # import os
# # # import subprocess
# # # import sys
# # # import platform

# # # # Define your current local app version here
# # # CURRENT_VERSION = "v6.0.0" 
# # # GITHUB_REPO = "codemaster-ar/aurora"

# # # # Try to import required libraries, handle gracefully if missing
# # # try:
# # #     from rich.console import Console
# # #     from rich.panel import Panel
# # #     from rich import print as rprint
# # #     import requests
# # # except ImportError:
# # #     print("Error: The 'rich' and 'requests' libraries are required.")
# # #     print("Please install them using: pip install rich requests")
# # #     sys.exit(1)

# # # console = Console()

# # # def check_for_updates():
# # #     """Checks GitHub Releases for a newer version string."""
# # #     url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
# # #     try:
# # #         # 1.5-second timeout to make sure it doesn't hang the app launch if offline
# # #         response = requests.get(url, timeout=1.5)
# # #         if response.status_code == 200:
# # #             latest_release = response.json()
# # #             latest_version = latest_release.get("tag_name", "").strip()
            
# # #             if latest_version and latest_version != CURRENT_VERSION:
# # #                 console.print(Panel(
# # #                     f"[bold yellow]⚠️  A new update is available![/bold yellow]\n\n"
# # #                     f"Current Version: [red]{CURRENT_VERSION}[/red]\n"
# # #                     f"Latest Version:  [green]{latest_version}[/green]\n\n"
# # #                     f"Download it here: [underline cyan]https://github.com/{GITHUB_REPO}/releases[/underline cyan]",
# # #                     title="[bold yellow]Update Notice[/bold yellow]",
# # #                     border_style="yellow"
# # #                 ))
# # #                 console.print()
# # #     except Exception:
# # #         # Silently pass on network/timeout issues so the launcher still opens the app offline
# # #         pass

# # # def display_header():
# # #     # ASCII Art for 'Aurora' (using raw string 'r' to prevent escape sequence warnings)
# # #     aurora_art = r"""
# # #     ___                                 
# # #    /   |  __  ___________  __________ _ 
# # #   / /| | / / / / ___/ __ \/ ___/ __ `/ 
# # #  / ___ |/ /_/ / /  / /_/ / /  / /_/ /  
# # # /_/  |_|\__,_/_/   \____/_/   \__,_/   
# # #     """
# # #     # Print the ASCII art
# # #     console.print(aurora_art, style="bold cyan")
    
# # #     # Print the fancy subtitle
# # #     console.print("    ✨ [bold italic violet]AI-powered[/bold italic violet] [bold italic sea_green2]Bioscience Dashboard[/bold italic sea_green2] ✨")
    
# # #     # Print the API credit in gray
# # #     console.print("       [grey50]powered by NASA OSDR API - Only Google Auth accepted[/grey50]\n")
    
# # #     # Print local version indicator
# # #     console.print(f"       [bold dim white]Local Version: {CURRENT_VERSION}[/bold dim white]\n")
    
# # #     # Decorative divider line
# # #     console.print("[bold magenta]=[/bold magenta]" * 50)
# # #     console.print()

# # # def ensure_node_modules(app_dir):
# # #     """Checks if node_modules exists, runs npm install with a loader if it doesn't."""
# # #     node_modules_path = os.path.join(app_dir, "node_modules")
    
# # #     if not os.path.exists(node_modules_path):
# # #         console.print(f"[bold yellow]📦 node_modules missing in {app_dir}[/bold yellow]")
        
# # #         # rich's status animation block
# # #         with console.status("[bold cyan]Running 'npm install'... This might take a moment...[/bold cyan]", spinner="dots"):
# # #             try:
# # #                 # Runs npm install and hides the messy stdout logs unless there is an error
# # #                 result = subprocess.run(
# # #                     "npm install", 
# # #                     cwd=app_dir, 
# # #                     shell=True, 
# # #                     stdout=subprocess.PIPE, 
# # #                     stderr=subprocess.PIPE,
# # #                     text=True
# # #                 )
                
# # #                 if result.returncode == 0:
# # #                     console.print("[bold green]✅ Dependencies successfully installed![/bold green]\n")
# # #                 else:
# # #                     console.print("[bold red]❌ npm install failed![/bold red]")
# # #                     console.print(f"[dim red]{result.stderr}[/dim red]")
# # #                     sys.exit(1)
                    
# # #             except Exception as e:
# # #                 console.print(f"[bold red]❌ Failed to execute npm install:[/bold red] {e}")
# # #                 sys.exit(1)

# # # def main():
# # #     display_header()
    
# # #     # Run the GitHub version check
# # #     check_for_updates()

# # #     # 1. Display the dialog based on OS
# # #     msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
    
# # #     if platform.system() == "Darwin":
# # #         # macOS: Use AppleScript for a native popup
# # #         os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
# # #     else:
# # #         # Linux / WSL / Others: Print a beautiful Rich Panel
# # #         console.print(Panel(
# # #             f"[yellow]{msg}[/yellow]", 
# # #             title="[bold blue]System Notice[/bold blue]", 
# # #             border_style="blue"
# # #         ))
# # #         console.print()

# # #     # 2. Get the current app directory (where package.json is located)
# # #     script_dir = os.path.dirname(os.path.abspath(__file__))
# # #     app_dir = os.path.join(script_dir, "genelab")
    
# # #     # Fallback check if script is already inside the genelab folder
# # #     if not os.path.exists(os.path.join(app_dir, "package.json")):
# # #         app_dir = script_dir

# # #     # 2b. Make sure node_modules are installed before trying to run the app
# # #     ensure_node_modules(app_dir)

# # #     try:
# # #         # 3. Launch the Electron app using npm start
# # #         console.print(f"[bold green]🚀 Launching Genelab from:[/bold green] [underline]{app_dir}[/underline]\n")
# # #         subprocess.run("npm start", cwd=app_dir, shell=True)
# # #     except Exception as e:
# # #         console.print(f"[bold red]❌ Error launching Genelab:[/bold red] {e}")
# # #         sys.exit(1)

# # # if __name__ == "__main__":
# # #     main()

# # #!/usr/bin/env python3
# # import os
# # import subprocess
# # import sys
# # import platform
# # import threading

# # # Try to import required libraries, handle gracefully if missing
# # try:
# #     from rich.console import Console
# #     from rich.panel import Panel
# #     from rich.align import Align
# #     from rich.text import Text
# #     from rich import print as rprint
# #     import requests
# # except ImportError:
# #     print("Error: The 'rich' and 'requests' libraries are required.")
# #     print("Please install them using: pip install rich requests")
# #     sys.exit(1)

# # console = Console()

# # # Configuration
# # CURRENT_VERSION = "v6.0.0" 
# # GITHUB_REPO = "codemaster-ar/aurora"
# # LOGGING_ENABLED = False  # Controlled via interactive console

# # def check_for_updates():
# #     """Checks GitHub Releases for a newer version string."""
# #     url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
# #     try:
# #         response = requests.get(url, timeout=1.5)
# #         if response.status_code == 200:
# #             latest_release = response.json()
# #             latest_version = latest_release.get("tag_name", "").strip()
            
# #             if latest_version and latest_version != CURRENT_VERSION:
# #                 console.print(Panel(
# #                     f"[bold yellow]⚠️  A new update is available![/bold yellow]\n\n"
# #                     f"Current Version: [red]{CURRENT_VERSION}[/red]\n"
# #                     f"Latest Version:  [green]{latest_version}[/green]\n\n"
# #                     f"Download it here: [underline cyan]https://github.com/{GITHUB_REPO}/releases[/underline cyan]",
# #                     title="[bold yellow]Update Notice[/bold yellow]",
# #                     border_style="yellow",
# #                     expand=False
# #                 ))
# #                 console.print()
# #     except Exception:
# #         pass

# # def display_header():
# #     """Displays the main Aurora Dashboard header encased in a styled Rich Panel."""
# #     aurora_art = r"""
# #     ___                                 
# #    /   |  __  ___________  __________ _ 
# #   / /| | / / / / ___/ __ \/ ___/ __ `/ 
# #  / ___ |/ /_/ / /  / /_/ / /  / /_/ /  
# # /_/  |_|\__,_/_/   \____/_/   \__,_/   
# #     """
    
# #     header_text = Text()
# #     header_text.append(aurora_art, style="bold cyan")
# #     header_text.append("\n    ✨ AI-powered Bioscience Dashboard ✨\n", style="bold italic violet")
# #     header_text.append("       powered by NASA OSDR API - Only Google Auth accepted\n\n", style="grey50")
# #     header_text.append(f"       Local Version: {CURRENT_VERSION}\n", style="bold dim white")
    
# #     # Wrap everything elegantly in a Panel box
# #     console.print(Panel(
# #         Align.center(header_text),
# #         border_style="magenta",
# #         title="[bold magenta]Aurora System Environment[/bold magenta]",
# #         subtitle="[dim white]Initialization Complete[/dim white]"
# #     ))
# #     console.print()

# # def show_about():
# #     """Displays information about the application."""
# #     about_text = (
# #         f"[bold cyan]Aurora Bioscience Dashboard[/bold cyan]\n"
# #         f"Version: [green]{CURRENT_VERSION}[/green]\n"
# #         f"Developer: [bold deep_sky_blue1]Codemaster-AR[/bold deep_sky_blue1]\n\n"
# #         f"For support or inquiries, please contact: [underline]codemaster.ar@gmail.com[/underline]"
# #     )
# #     console.print(Panel(about_text, title="[bold True]About Aurora[/bold True]", border_style="cyan", expand=False))

# # def ensure_node_modules(app_dir):
# #     """Checks if node_modules exists, runs npm install with a loader if it doesn't."""
# #     node_modules_path = os.path.join(app_dir, "node_modules")
    
# #     if not os.path.exists(node_modules_path):
# #         console.print(Panel(f"[bold yellow]📦 node_modules missing in {app_dir}[/bold yellow]", border_style="yellow", expand=False))
        
# #         with console.status("[bold cyan]Running 'npm install'... This might take a moment...[/bold cyan]", spinner="dots"):
# #             try:
# #                 result = subprocess.run(
# #                     "npm install", 
# #                     cwd=app_dir, 
# #                     shell=True, 
# #                     stdout=subprocess.PIPE, 
# #                     stderr=subprocess.PIPE,
# #                     text=True
# #                 )
                
# #                 if result.returncode == 0:
# #                     console.print("[bold green]✅ Dependencies successfully installed![/bold green]\n")
# #                 else:
# #                     console.print("[bold red]❌ npm install failed![/bold red]")
# #                     console.print(f"[dim red]{result.stderr}[/dim red]")
# #                     sys.exit(1)
                    
# #             except Exception as e:
# #                 console.print(f"[bold red]❌ Failed to execute npm install:[/bold red] {e}")
# #                 sys.exit(1)

# # def run_electron_app(app_dir):
# #     """Launches Electron in a background thread or process based on log preferences."""
# #     global LOGGING_ENABLED
# #     try:
# #         console.print(f"[bold green]🚀 Launching Genelab from:[/bold green] [underline]{app_dir}[/underline]\n")
        
# #         # Decide if we hide output logs or stream them
# #         stdout_dest = None if LOGGING_ENABLED else subprocess.DEVNULL
# #         stderr_dest = None if LOGGING_ENABLED else subprocess.DEVNULL
        
# #         # Launching as a non-blocking background process so the terminal stays active
# #         subprocess.Popen("npm start", cwd=app_dir, shell=True, stdout=stdout_dest, stderr=stderr_dest)
# #     except Exception as e:
# #         console.print(f"[bold red]❌ Error launching Genelab:[/bold red] {e}")

# # def main():
# #     global LOGGING_ENABLED
# #     display_header()
# #     check_for_updates()

# #     # System notice handling
# #     msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
# #     if platform.system() == "Darwin":
# #         os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
# #     else:
# #         console.print(Panel(f"[yellow]{msg}[/yellow]", title="[bold blue]System Notice[/bold blue]", border_style="blue"))
# #         console.print()

# #     # Locate application path
# #     script_dir = os.path.dirname(os.path.abspath(__file__))
# #     app_dir = os.path.join(script_dir, "genelab")
# #     if not os.path.exists(os.path.join(app_dir, "package.json")):
# #         app_dir = script_dir

# #     ensure_node_modules(app_dir)
    
# #     # Auto-launch app on start
# #     run_electron_app(app_dir)

# #     # Help Menu layout box
# #     help_menu = (
# #         "Available Commands:\n"
# #         "  [bold cyan]logging[/bold cyan] : Toggle framework/app standard logs on/off\n"
# #         "  [bold cyan]about[/bold cyan]   : Show application developer metadata\n"
# #         "  [bold cyan]quit[/bold cyan]    : Terminate launcher session (or press [bold red]Ctrl+C[/bold red])"
# #     )
# #     console.print(Panel(help_menu, title="[bold green]Interactive Terminal Console[/bold green]", border_style="green"))

# #     # Interactive Command Loop
# #     while True:
# #         try:
# #             # Styled prompt input
# #             cmd = console.input("[bold magenta]aurora-shell❯[/bold magenta] ").strip().lower()
            
# #             if cmd in ("quit", "exit"):
# #                 console.print("[bold red]Shutting down launcher console. Goodbye![/bold red]")
# #                 break
                
# #             elif cmd == "logging":
# #                 LOGGING_ENABLED = not LOGGING_ENABLED
# #                 status = "[bold green]ENABLED[/bold green] (Relaunch required to hook stdout)" if LOGGING_ENABLED else "[bold red]DISABLED[/bold red]"
# #                 console.print(f"[*] Framework logging is now {status}")
                
# #             elif cmd == "about":
# #                 show_about()
                
# #             elif cmd == "":
# #                 continue
# #             else:
# #                 console.print(f"[bold red]Unknown command:[/bold red] '{cmd}'. Type 'about', 'logging', or 'quit'.")
                
# #         except (KeyboardInterrupt, EOFError):
# #             console.print("\n[bold red]Session interrupted. Exiting...[/bold red]")
# #             break

# # if __name__ == "__main__":
# #     main()
# #!/usr/bin/env python3
# import os
# import subprocess
# import sys
# import platform

# # Define your current local app version here
# CURRENT_VERSION = "v6.0.0" 
# GITHUB_REPO = "codemaster-ar/aurora"

# # Try to import required libraries, handle gracefully if missing
# try:
#     from rich.console import Console
#     from rich.panel import Panel
#     from rich import print as rprint
#     from rich.prompt import Prompt
#     from rich.align import Align
#     import requests
# except ImportError:
#     print("Error: The 'rich' and 'requests' libraries are required.")
#     print("Please install them using: pip install rich requests")
#     sys.exit(1)

# console = Console()
# logging_enabled = False
# electron_process = None

# def check_for_updates():
#     """Checks GitHub Releases for a newer version string."""
#     url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
#     try:
#         response = requests.get(url, timeout=1.5)
#         if response.status_code == 200:
#             latest_release = response.json()
#             latest_version = latest_release.get("tag_name", "").strip()
            
#             if latest_version and latest_version != CURRENT_VERSION:
#                 update_msg = (
#                     f"Current Version: [bold red]{CURRENT_VERSION}[/bold red]\n"
#                     f"Latest Version:  [bold green]{latest_version}[/bold green]\n\n"
#                     f"Download here: [underline cyan]https://github.com/{GITHUB_REPO}/releases[/underline cyan]"
#                 )
#                 console.print(Panel(
#                     Align.center(update_msg),
#                     title="[bold yellow]⚠️ Update Available[/bold yellow]",
#                     border_style="yellow",
#                     expand=False,
#                     padding=(1, 2)
#                 ))
#     except Exception:
#         pass

# def display_header():
#     aurora_art = r"""
#     ___                                 
#    /   |  __  ___________  __________ _ 
#   / /| | / / / / ___/ __ \/ ___/ __ `/ 
#  / ___ |/ /_/ / /  / /_/ / /  / /_/ /  
# /_/  |_|\__,_/_/   \____/_/   \__,_/   
#     """
    
#     header_content = (
#         f"[bold cyan]{aurora_art}[/bold cyan]\n"
#         "✨ [bold italic violet]AI-powered[/bold italic violet] [bold italic sea_green2]Bioscience Dashboard[/bold italic sea_green2] ✨\n\n"
#         "[grey50]powered by NASA OSDR API - Only Google Auth accepted[/grey50]\n"
#         f"[bold dim white]Local Version: {CURRENT_VERSION}[/bold dim white]"
#     )
    
#     console.print(Panel(
#         Align.center(header_content),
#         border_style="bold magenta",
#         padding=(1, 4)
#     ))

# def show_about():
#     about_text = (
#         f"[bold cyan]Aurora Bioscience Dashboard[/bold cyan]\n"
#         f"Version: [bold green]{CURRENT_VERSION}[/bold green]\n"
#         f"Repository: [underline]https://github.com/{GITHUB_REPO}[/underline]\n\n"
#         "An advanced interface for exploring biological space research data."
#     )
#     console.print(Panel(Align.center(about_text), title="[bold violet]About Aurora[/bold violet]", border_style="violet", expand=False))

# def ensure_node_modules(app_dir):
#     """Checks if node_modules exists, runs npm install with a loader if it doesn't."""
#     node_modules_path = os.path.join(app_dir, "node_modules")
    
#     if not os.path.exists(node_modules_path):
#         console.print(Panel(f"[bold yellow]📦 node_modules missing in {app_dir}. Initializing installation...[/bold yellow]", border_style="yellow"))
        
#         with console.status("[bold cyan]Running 'npm install'... This might take a moment...[/bold cyan]", spinner="dots"):
#             try:
#                 result = subprocess.run(
#                     "npm install", 
#                     cwd=app_dir, 
#                     shell=True, 
#                     stdout=subprocess.PIPE, 
#                     stderr=subprocess.PIPE,
#                     text=True
#                 )
                
#                 if result.returncode == 0:
#                     console.print(Panel("[bold green]✅ Dependencies successfully installed![/bold green]", border_style="green"))
#                 else:
#                     console.print(Panel(f"[bold red]❌ npm install failed![/bold red]\n[dim red]{result.stderr}[/dim red]", border_style="red"))
#                     sys.exit(1)
                    
#             except Exception as e:
#                 console.print(Panel(f"[bold red]❌ Failed to execute npm install:[/bold red] {e}", border_style="red"))
#                 sys.exit(1)

# def main():
#     global logging_enabled, electron_process
#     display_header()
#     check_for_updates()

#     # 1. System Notification popup/box
#     msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
    
#     if platform.system() == "Darwin":
#         os.system(f"osascript -e 'display dialog \"{msg}\" buttons {{\"OK\"}} default button \"OK\"'")
#     else:
#         console.print(Panel(
#             Align.center(f"[yellow]{msg}[/yellow]"), 
#             title="[bold blue]💻 System Notice[/bold blue]", 
#             border_style="blue",
#             padding=(1, 2)
#         ))

#     # 2. Workspace Setup
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     app_dir = os.path.join(script_dir, "genelab")
    
#     if not os.path.exists(os.path.join(app_dir, "package.json")):
#         app_dir = script_dir

#     ensure_node_modules(app_dir)

#     # 3. Asynchronously Boot Electron Core
#     try:
#         console.print(Panel(
#             Align.center(f"[bold green]🚀 Launching Genelab Core Engine...[/bold green]\n[dim]Path: {app_dir}[/dim]"),
#             border_style="green"
#         ))
        
#         # Open in background so the script terminal interface is interactive
#         stdout_dest = None if logging_enabled else subprocess.DEVNULL
#         stderr_dest = None if logging_enabled else subprocess.DEVNULL
        
#         electron_process = subprocess.Popen(
#             "npm start", 
#             cwd=app_dir, 
#             shell=True,
#             stdout=stdout_dest,
#             stderr=stderr_dest
#         )
#     except Exception as e:
#         console.print(Panel(f"[bold red]❌ Error launching Genelab Engine:[/bold red] {e}", border_style="red"))
#         sys.exit(1)

#     # Help Menu layout
#     help_menu = (
#         "[bold cyan]Available Terminal Controls:[/bold cyan]\n"
#         " ❖ [bold green]logging[/bold green] : Toggle logs output     ❖ [bold green]about[/bold green] : Application details\n"
#         " ❖ [bold green]quit / exit[/bold green] : Safe shutdown     ❖ [bold green]Ctrl + C[/bold green] : Hard exit"
#     )
#     console.print(Panel(Align.center(help_menu), title="[bold dim white]Terminal Interface Active[/bold dim white]", border_style="dim white"))

#     # Interactive loop
#     while True:
#         try:
#             cmd = Prompt.ask("\n[bold magenta]aurora-sys[/bold magenta]").strip().lower()
            
#             if cmd in ['quit', 'exit']:
#                 raise KeyboardInterrupt
                
#             elif cmd == 'logging':
#                 logging_enabled = not logging_enabled
#                 status = "[bold green]ENABLED[/bold green] (Restart required for full process streams)" if logging_enabled else "[bold red]DISABLED[/bold red]"
#                 console.print(Panel(f"Engine Log Streaming is now: {status}", border_style="cyan"))
                
#             elif cmd == 'about':
#                 show_about()
                
#             elif cmd == '':
#                 continue
#             else:
#                 console.print("[bold red]❓ Unknown terminal command. Type 'about', 'logging', or 'exit'.[/bold red]")
                
#         except (KeyboardInterrupt, EOFError):
#             console.print("\n")
#             console.print(Panel(Align.center("[bold red]🛑 Shutting down Aurora Environment & Killing Assets...[/bold red]"), border_style="red"))
#             if electron_process:
#                 electron_process.terminate()
#             sys.exit(0)

# if __name__ == "__main__":
#     main()
#!/usr/bin/env python3
import os
import subprocess
import sys
import platform

# Define your current local app version here
CURRENT_VERSION = "v6.0.0" 
GITHUB_REPO = "codemaster-ar/aurora"

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
                    text=True
                )
                
                if result.returncode == 0:
                    console.print(Panel("[bold green]✅ Dependencies successfully installed![/bold green]", border_style="green"))
                else:
                    console.print(Panel(f"[bold red]❌ npm install failed![/bold red]\n[dim red]{result.stderr}[/dim red]", border_style="red"))
                    sys.exit(1)
                    
            except Exception as e:
                console.print(Panel(f"[bold red]❌ Failed to execute npm install:[/bold red] {e}", border_style="red"))
                sys.exit(1)

def main():
    global logging_enabled, electron_process
    display_header()
    check_for_updates()

    # 1. System Notification popup/box
    msg = "Created by Codemaster-AR: There could be an error. If there is, just press OK. Additionally, if you face any issues, please contact codemaster.ar@Gmail.com"
    
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

    # 3. Asynchronously Boot Electron Core
    try:
        console.print(Panel(
            Align.center(f"[bold green]🚀 Launching Genelab Core Engine...[/bold green]\n[dim]Path: {app_dir}[/dim]"),
            border_style="green"
        ))
        
        # Open in background so the script terminal interface is interactive
        stdout_dest = None if logging_enabled else subprocess.DEVNULL
        stderr_dest = None if logging_enabled else subprocess.DEVNULL
        
        electron_process = subprocess.Popen(
            "npm start", 
            cwd=app_dir, 
            shell=True,
            stdout=stdout_dest,
            stderr=stderr_dest
        )
    except Exception as e:
        console.print(Panel(f"[bold red]❌ Error launching Genelab Engine:[/bold red] {e}", border_style="red"))
        sys.exit(1)

    # Help Menu layout
    help_menu = (
        "[bold cyan]Available Terminal Controls:[/bold cyan]\n"
        " ❖ [bold green]logging[/bold green] : Toggle logs output     ❖ [bold green]about[/bold green] : Application details\n"
        " ❖ [bold green]quit / exit[/bold green] : Safe shutdown     ❖ [bold green]Ctrl + C[/bold green] : Hard exit"
    )
    console.print(Panel(Align.center(help_menu), title="[bold dim white]Terminal Interface Active[/bold dim white]", border_style="dim white"))

    # Interactive loop
    while True:
        try:
            cmd = Prompt.ask("\n[bold magenta]aurora-sys[/bold magenta]").strip().lower()
            
            if cmd in ['quit', 'exit']:
                raise KeyboardInterrupt
                
            elif cmd == 'logging':
                logging_enabled = not logging_enabled
                status = "[bold green]ENABLED[/bold green] (Restart required for full process streams)" if logging_enabled else "[bold red]DISABLED[/bold red]"
                console.print(Panel(f"Engine Log Streaming is now: {status}", border_style="cyan"))
                
            elif cmd == 'about':
                show_about()
                
            elif cmd == '':
                continue
            else:
                console.print("[bold red]❓ Unknown terminal command. Type 'about', 'logging', or 'exit'.[/bold red]")
                
        except (KeyboardInterrupt, EOFError):
            console.print("\n")
            console.print(Panel(Align.center("[bold red]🛑 Shutting down Aurora Environment & Killing Assets...[/bold red]"), border_style="red"))
            if electron_process:
                electron_process.terminate()
            sys.exit(0)

if __name__ == "__main__":
    main()