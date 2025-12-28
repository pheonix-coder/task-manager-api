import requests
import time
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()
# Use a separate DB file for testing
TEST_DB = "test.db"
BASE_URL = "http://127.0.0.1:5000/api"
USER_DATA = {"username": "rohan_sharma", "password": "radhika_sharma"}

results = []

def log_result(step, status, message):
    color = "green" if status == "SUCCESS" else "red"
    results.append([step, f"[{color}]{status}[/]", message])

def run_test():
    global token
    
    # Header 1
    console.print(Panel.fit("[bold cyan]🔐 AUTHENTICATION PHASE[/]", border_style="cyan"))
    
    with console.status("[bold yellow]Registering...", spinner="dots"):
        time.sleep(1)
        resp = requests.post(f"{BASE_URL}/auth/signup", json=USER_DATA)
        log_result("Signup", "SUCCESS", "User Account Created")

    with console.status("[bold yellow]Logging in...", spinner="balloon2"):
        time.sleep(1)
        resp = requests.post(f"{BASE_URL}/auth/login", json=USER_DATA)
        token = resp.json().get("access_token")
        log_result("Login", "SUCCESS", "JWT Token generated")

    # Fixed the concatenation error by printing separately
    console.print("") 
    console.print(Panel.fit("[bold magenta]📝 TASK OPERATIONS PHASE[/]", border_style="magenta"))
    
    headers = {"Authorization": f"Bearer {token}"}

    with console.status("[bold yellow]Creating Task...", spinner="dots11"):
        time.sleep(1)
        payload = {"title": "Isolated Test", "description": "Testing on test.db"}
        resp = requests.post(f"{BASE_URL}/tasks/", json=payload, headers=headers)
        task_id = resp.json().get("id")
        log_result("Create Task", "SUCCESS", f"Task ID {task_id} added to test.db")

    with console.status("[bold red]Deleting Task...", spinner="dots12"):
        time.sleep(1)
        requests.delete(f"{BASE_URL}/tasks/{task_id}", headers=headers)
        log_result("Delete Task", "SUCCESS", "Cleaned up test.db")

    # Final Table
    table = Table(title="\n📊 TEST SUMMARY", border_style="bright_black")
    table.add_column("Step")
    table.add_column("Status")
    table.add_column("Details")
    for row in results:
        table.add_row(*row)
    console.print(table)

if __name__ == "__main__":
    # Instruction to user
    console.print(f"[bold yellow]NOTE:[/] Ensure server is running with DATABASE_URL=sqlite:///{TEST_DB}")
    run_test()