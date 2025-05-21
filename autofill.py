# autofill.py
# Entry point for your automation workflow.

import csv
import time
import pyautogui
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------- Configuration ---------------------------------------------
TAB_COUNT  = 3        # extra tabs after 2nd field
ROW_DELAY  = 0.30     # pause after each row (sec)
# -----------------------------------------------------------------------------


def choose_csv() -> Path | None:
    """Open a file-picker dialog and return the chosen Path (or None)."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select attendance CSV",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    root.destroy()
    return Path(file_path) if file_path else None


def wait_for_user() -> None:
    """Show a 'Start' dialog so the user can focus the form field."""
    def _proceed():
        dialog.destroy()

    dialog = tk.Tk()
    dialog.title("Autofill – Ready?")
    dialog.resizable(False, False)

    msg = tk.Label(
        dialog,
        text=("Place the text cursor in the FIRST form field, then click "
              "'Start' to begin."),
        padx=20, pady=15, wraplength=300, justify="left"
    )
    msg.pack()

    start_btn = tk.Button(dialog, text="Start", width=12, command=_proceed)
    start_btn.pack(pady=(0, 15))

    dialog.attributes("-topmost", True)          # stay on top
    start_btn.focus_set()
    dialog.mainloop()                            # pause here until closed


def autofill(csv_path: Path) -> None:
    """Read a two-column CSV and send keystrokes to the active window."""
    with csv_path.open(newline='') as f:
        reader = csv.reader(f)
        next(reader, None)                       # skip header if present
        for row in reader:
            if len(row) < 2:                     # skip malformed lines
                continue
            pyautogui.write(row[0])
            pyautogui.press('tab')
            pyautogui.write(row[1])
            pyautogui.press('tab', presses=TAB_COUNT)
            time.sleep(ROW_DELAY)


if __name__ == "__main__":
    csv_file = choose_csv()
    if not csv_file:
        messagebox.showinfo("Autofill", "No file selected — exiting.")
        raise SystemExit

    wait_for_user()        # user positions cursor and clicks “Start”

    try:
        autofill(csv_file)
        messagebox.showinfo("Autofill", "✅ Autofill complete.")
    except Exception as e:
        messagebox.showerror("Autofill", f"⚠ An error occurred:\n{e}")
