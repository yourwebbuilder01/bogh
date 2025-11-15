# BOGH System Tools 🚀

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Windows](https://img.shields.io/badge/Platform-Windows-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📦 Installation Guide

### Step 1: Install Python
**Download Python 3.6 or higher:**
- Go to [python.org](https://python.org/downloads)
- Download Python 3.8+ for Windows
- **IMPORTANT:** During installation, CHECK "Add Python to PATH"
- Complete the installation

### Step 2: Download BOGH
**Option A: Download ZIP**
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the folder to your Desktop

**Option B: Git Clone (if you have Git)**
```bash
git clone https://github.com/yourwebbuilder01/bogh.git
cd bogh
```

### Step 3: Install Required Packages
Open **Command Prompt** or **PowerShell** and run:

```bash
# Navigate to BOGH folder (replace with your actual path)
cd C:\Users\YourName\Desktop\bogh

# Install the required package
pip install psutil
```

**Troubleshooting:**
- If `pip` is not recognized, restart your computer after Python installation
- Or use: `python -m pip install psutil`

### Step 4: Run BOGH
```bash
python bogh_system_tools.py
```

---

## 🎮 How to Use BOGH

### First Launch
When you run BOGH, you'll see this interface:
```
┌──────────────────────────────────────────┐
│                BOGH SYSTEM TOOLS v4.0    │
├──────────────────────────────────────────┤
│ System: Windows 11                       │
│ Disk: 45% used | RAM: 62% used           │
├──────────────────────────────────────────┤
│ [1] JUNK FILE CLEANER                    │
│ [2] DUPLICATE FILE HUNTER                │
│ [3] ADVANCED FILE EXPLORER               │
│ [4] NETWORK CONFIGURATION                │
│ [5] WIFI PASSWORD REVEALER               │
│ [6] HARDWARE INFORMATION                 │
│ [7] ABOUT                                │
│ [8] EXIT                                 │
└──────────────────────────────────────────┘
```

### Tool Guide

#### 🗑️ **1. Junk File Cleaner**
- Cleans temporary files and browser cache
- **Usage:** Select option 1, then choose what to clean
- **Safe:** Always asks for confirmation before deleting

#### 🔍 **2. Duplicate File Hunter**
- Finds files with same names and sizes
- **Usage:** Select folder to scan, review duplicates, delete if needed
- **Saves:** Typically 1-5GB of space

#### 📁 **3. Advanced File Explorer**
- Browse files and folders in terminal
- **Features:** Search files, view file info, open files
- **Navigation:** Use numbers to select, U=Up, H=Home

#### 🌐 **4. Network Configuration**
- View your IP address and network info
- **Tools:** Ping test, DNS flush, routing table
- **Usage:** Great for troubleshooting internet issues

#### 📡 **5. WiFi Password Revealer**
- **Shows all saved WiFi passwords**
- **Requires:** Administrator rights
- **Export:** Save passwords to text file

#### 💻 **6. Hardware Information**
- Real-time system monitoring
- **Shows:** CPU, RAM, Disk usage, temperatures
- **Health:** System health status and alerts

#### 👨‍💻 **7. About**
- Developer information and links
- **Clickable:** Opens GitHub, Instagram, Portfolio in browser

---

## ⚡ Quick Commands Cheat Sheet

```bash
# Always run from BOGH folder
cd C:\Users\YourName\Desktop\bogh

# Start BOGH
python bogh_system_tools.py

# Install dependencies (if missing)
pip install psutil

# Run as Administrator (for WiFi passwords)
# Right-click Command Prompt → "Run as administrator"
```

---

## 🛠️ Troubleshooting

### ❌ "Python not found"
- Python not installed or not in PATH
- **Fix:** Reinstall Python and check "Add to PATH"

### ❌ "No module named psutil"
- Dependencies not installed
- **Fix:** Run `pip install psutil`

### ❌ "Access denied" for WiFi passwords
- Need Administrator privileges
- **Fix:** Run Command Prompt as Administrator

### ❌ File not found errors
- Running from wrong directory
- **Fix:** Navigate to BOGH folder first

### ❌ Script won't start
- File might be blocked by Windows
- **Fix:** Right-click → Properties → Unblock

---

## 🔧 Advanced Usage

### Run as Administrator
For full functionality (especially WiFi passwords):
1. Search "cmd" in Windows
2. Right-click "Command Prompt"
3. Select "Run as administrator"
4. Navigate to BOGH folder and run the script

### Create Desktop Shortcut
1. Right-click on desktop → New → Shortcut
2. Location: `python C:\path\to\bogh\bogh_system_tools.py`
3. Name: "BOGH System Tools"

### Batch File for Easy Launch
Create `run_bogh.bat` in the BOGH folder:
```batch
@echo off
cd /d "C:\Users\YourName\Desktop\bogh"
python bogh_system_tools.py
pause
```

---

## 📋 System Requirements

- **OS:** Windows 10 or Windows 11
- **Python:** Version 3.6 or higher
- **RAM:** 2GB minimum
- **Storage:** 50MB free space
- **Permissions:** Standard user (Admin for WiFi features)

---

## 🎯 What Makes BOGH Special?

✅ **All-in-One** - 6 essential tools in one interface  
✅ **Safe** - All destructive operations require confirmation  
✅ **No Internet** - Works completely offline  
✅ **Privacy** - No data collection whatsoever  
✅ **User-Friendly** - Clear menus and instructions  
✅ **Powerful** - Real system utilities with hacker style  

---

## ❓ Frequently Asked Questions

**Q: Is BOGH safe to use?**  
A: Absolutely! All operations are transparent and require confirmation. No system files are touched.

**Q: Does it work on Mac/Linux?**  
A: Currently optimized for Windows, but many features work on other systems.

**Q: Can I see the source code?**  
A: Yes! BOGH is open source - all code is visible and modifiable.

**Q: Will this slow down my computer?**  
A: No, BOGH is lightweight and only runs when you use it.

---

## 📞 Support

- **GitHub Issues:** Report bugs or request features
- **Email:** Check the About section in the app
- **Documentation:** This README file

---

## 🚀 Ready to Start?

```bash
# Open Command Prompt and run:
cd Desktop\bogh
python bogh_system_tools.py
```

**Enjoy your new system power tools!** 🎉

