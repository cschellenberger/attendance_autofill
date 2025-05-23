# Attendance Autofill

This project automates form filling from CSV files using Python and GUI automation.

## Features
- Select a CSV file with your class schedule or attendance data
- Automatically fill out web or desktop forms using keyboard automation
- Simple GUI prompts for user interaction
- Build a standalone Windows executable for easy distribution

## Sample CSV
A sample file is included as `sample.csv`:

```
Class Dates,Week Session
2025-09-02,Week 1 - Day 1
2025-09-04,Week 1 - Day 2
2025-09-09,Week 2 - Day 1
2025-09-11,Week 2 - Day 2
2025-09-16,Week 3 - Day 1
```

## Installation (for developers)
1. Clone this repository:
   ```sh
   git clone https://github.com/cschellenberger/attendance_autofill.git
   cd attendance_autofill
   ```
2. (Recommended) Create and activate a virtual environment:
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Usage (with Python)
- Run the script:
  ```powershell
  python autofill.py
  ```

## Build a Windows Executable
1. Install dependencies (see above).
2. Run:
   ```powershell
   pyinstaller --onefile --windowed autofill.py
   ```
3. The standalone `.exe` will be in the `dist/` folder. You can distribute this file directly to users—no Python required.

## Usage (for end users)
- Download the latest release `.exe` from the [Releases](https://github.com/cschellenberger/attendance_autofill/releases) page (if available).
- Double-click the `.exe` to run. No installation or Python required.

## License
MIT License. See [LICENSE](LICENSE).

---
If you encounter issues with PowerShell script execution, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
