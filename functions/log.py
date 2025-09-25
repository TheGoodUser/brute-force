from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
from datetime import datetime

console = Console()

def ts_ms():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def rich_log(email: str, password: str, ok: bool):
    time = ts_ms()

    # Minimal failure line
    if not ok:
        text = Text.assemble(
            (f"[{time}] ", "white on black"),
            ("[FAILED]", "bold white on red"),
            (" Email: ", "bold"),
            (email, "yellow"),
            (" | Password: ", "bold"),
            (password, "magenta"),
        )
        console.print(text)
        return

    # Success panel with highlighted details
    table = Table.grid(padding=(0,1))
    table.add_column(justify="right", ratio=1, style="bold")
    table.add_column(justify="left", ratio=3)

    table.add_row("Status", "[bold green]SUCCESS[/bold green]")
    table.add_row("Timestamp", f"[white on black]{time}[/white on black]")
    table.add_row("Email", f"[yellow]{email}[/yellow]")
    table.add_row("Password", f"[magenta]{password}[/magenta]")

    panel = Panel(
        table,
        title="[bold]AUTH LOG[/bold]",
        subtitle=f"[dim]{time}[/dim]",
        border_style="green",
        box=box.ROUNDED,
        padding=(1,2),
    )
    console.print(panel)