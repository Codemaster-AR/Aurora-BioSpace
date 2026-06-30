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