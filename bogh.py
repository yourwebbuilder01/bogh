import os
import time
import platform
import psutil
import shutil
import socket
import subprocess
import threading
from datetime import datetime
import glob
import webbrowser

def hacker_print(text, delay=0.003):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_windows_version():
    try:
        if platform.system() == "Windows":
            build_number = int(platform.version().split('.')[2])
            if build_number >= 22000:
                return "Windows 11"
            else:
                return "Windows 10"
        return f"{platform.system()} {platform.release()}"
    except:
        return f"{platform.system()} {platform.release()}"

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("┌" + "─" * 58 + "┐")
    hacker_print("│                    ██████╗  ██████╗  ██████╗ ██╗  ██╗              │")
    hacker_print("│                    ██╔══██╗██╔═══██╗██╔════╝ ██║  ██║              │")
    hacker_print("│                    ██████╔╝██║   ██║██║  ███╗███████║              │")
    hacker_print("│                    ██╔══██╗██║   ██║██║   ██║██╔══██║              │")
    hacker_print("│                    ██████╔╝╚██████╔╝╚██████╔╝██║  ██║              │")
    hacker_print("│                    ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝              │")
    print("├" + "─" * 58 + "┤")
    hacker_print("│                  BOGH SYSTEM TOOLS v4.0                  │")
    print("├" + "─" * 58 + "┤")
    
    disk_usage = psutil.disk_usage('/')
    memory = psutil.virtual_memory()
    windows_ver = get_windows_version()
    hacker_print(f"│ System: {windows_ver}{' ' * (46 - len(windows_ver))}│")
    hacker_print(f"│ Disk: {disk_usage.percent}% used | RAM: {memory.percent}% used{' ' * 16}│")
    print("├" + "─" * 58 + "┤")
    hacker_print("│ [1] JUNK FILE CLEANER                                   │")
    hacker_print("│ [2] DUPLICATE FILE HUNTER                               │")
    hacker_print("│ [3] ADVANCED FILE EXPLORER                              │")
    hacker_print("│ [4] NETWORK CONFIGURATION                               │")
    hacker_print("│ [5] WIFI PASSWORD REVEALER                              │")
    hacker_print("│ [6] HARDWARE INFORMATION                                │")
    hacker_print("│ [7] ABOUT                                               │")
    hacker_print("│ [8] EXIT                                                │")
    print("└" + "─" * 58 + "┘")
    
    choice = input("\n[INPUT] Select operation: ").strip()
    return choice

def clean_temp_files():
    temp_folders = []
    
    if os.name == 'nt':
        temp_folders = [
            os.environ.get('TEMP', ''),
            os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Local', 'Temp'),
            r'C:\Windows\Temp',
        ]
    else:
        temp_folders = [
            '/tmp',
            '/var/tmp',
            os.path.expanduser('~/.cache'),
        ]
    
    total_cleaned = 0
    files_removed = 0
    
    for temp_folder in temp_folders:
        if os.path.exists(temp_folder):
            hacker_print(f"[CLEANING] {temp_folder}...")
            try:
                for root, dirs, files in os.walk(temp_folder):
                    for file in files:
                        try:
                            file_path = os.path.join(root, file)
                            if os.path.isfile(file_path):
                                file_size = os.path.getsize(file_path)
                                os.remove(file_path)
                                total_cleaned += file_size
                                files_removed += 1
                        except:
                            continue
            except:
                continue
    
    return total_cleaned, files_removed

def clean_browser_cache():
    browser_paths = []
    
    if os.name == 'nt':
        browser_paths = [
            os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Cache'),
            os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Local', 'Microsoft', 'Edge', 'User Data', 'Default', 'Cache'),
            os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Roaming', 'Mozilla', 'Firefox', 'Profiles'),
        ]
    else:
        browser_paths = [
            os.path.expanduser('~/.cache/google-chrome'),
            os.path.expanduser('~/.config/google-chrome/Default/Cache'),
            os.path.expanduser('~/.mozilla/firefox'),
        ]
    
    total_cleaned = 0
    files_removed = 0
    
    for cache_path in browser_paths:
        if os.path.exists(cache_path):
            hacker_print(f"[CLEANING] {os.path.basename(cache_path)}...")
            try:
                for root, dirs, files in os.walk(cache_path):
                    for file in files:
                        try:
                            file_path = os.path.join(root, file)
                            if os.path.isfile(file_path):
                                file_size = os.path.getsize(file_path)
                                os.remove(file_path)
                                total_cleaned += file_size
                                files_removed += 1
                        except:
                            continue
            except:
                continue
    
    return total_cleaned, files_removed

def junk_file_cleaner():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 58 + "┐")
        hacker_print("│               JUNK FILE CLEANER                         │")
        print("├" + "─" * 58 + "┤")
        
        hacker_print("[READY] Select cleaning option:")
        print("├" + "─" * 58 + "┤")
        hacker_print("│ [1] Clean Temporary Files                              │")
        hacker_print("│ [2] Clean Browser Cache                                │")
        hacker_print("│ [3] Clean Everything                                   │")
        hacker_print("│ [4] Return to Main Menu                                │")
        print("└" + "─" * 58 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip()
        
        if choice == '1':
            hacker_print("[CLEANING] Temporary files...")
            total_cleaned, files_removed = clean_temp_files()
            cleaned_mb = total_cleaned / (1024 * 1024)
            hacker_print(f"[SUCCESS] Removed {files_removed} temp files")
            hacker_print(f"[SUCCESS] Freed {cleaned_mb:.1f}MB of space")
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            hacker_print("[CLEANING] Browser cache...")
            total_cleaned, files_removed = clean_browser_cache()
            cleaned_mb = total_cleaned / (1024 * 1024)
            hacker_print(f"[SUCCESS] Removed {files_removed} cache files")
            hacker_print(f"[SUCCESS] Freed {cleaned_mb:.1f}MB of space")
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            hacker_print("[CLEANING] Temporary files...")
            temp_cleaned, temp_files = clean_temp_files()
            hacker_print("[CLEANING] Browser cache...")
            cache_cleaned, cache_files = clean_browser_cache()
            
            total_cleaned = temp_cleaned + cache_cleaned
            total_files = temp_files + cache_files
            cleaned_mb = total_cleaned / (1024 * 1024)
            
            hacker_print(f"[SUCCESS] Removed {total_files} files total")
            hacker_print(f"[SUCCESS] Freed {cleaned_mb:.1f}MB of space")
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            break

def find_duplicate_files(start_path):
    file_dict = {}
    duplicates = []
    
    hacker_print(f"[SCANNING] {start_path}...")
    
    for root, dirs, files in os.walk(start_path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path)
                    file_key = (file, file_size)
                    
                    if file_key in file_dict:
                        duplicates.append((file_path, file_dict[file_key], file_size))
                    else:
                        file_dict[file_key] = file_path
            except:
                continue
    
    return duplicates

def duplicate_file_hunter():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 58 + "┐")
        hacker_print("│             DUPLICATE FILE HUNTER                       │")
        print("├" + "─" * 58 + "┤")
        
        print("├" + "─" * 58 + "┤")
        hacker_print("│ [1] Scan Downloads Folder                             │")
        hacker_print("│ [2] Scan Pictures Folder                              │")
        hacker_print("│ [3] Scan Documents Folder                             │")
        hacker_print("│ [4] Custom Folder Path                                │")
        hacker_print("│ [5] Return to Main Menu                               │")
        print("└" + "─" * 58 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip()
        
        if choice == '1':
            folder = os.path.join(os.environ.get('USERPROFILE', ''), 'Downloads')
        elif choice == '2':
            folder = os.path.join(os.environ.get('USERPROFILE', ''), 'Pictures')
        elif choice == '3':
            folder = os.path.join(os.environ.get('USERPROFILE', ''), 'Documents')
        elif choice == '4':
            folder = input("[INPUT] Enter folder path: ").strip()
        elif choice == '5':
            break
        else:
            continue
        
        if not os.path.exists(folder):
            hacker_print("[ERROR] Folder does not exist")
            input("\nPress Enter to continue...")
            continue
        
        duplicates = find_duplicate_files(folder)
        
        if duplicates:
            total_size = 0
            hacker_print("[FOUND] Duplicate files:")
            for i, (file1, file2, size) in enumerate(duplicates[:15], 1):
                size_mb = size / (1024 * 1024)
                total_size += size_mb
                hacker_print(f"├── {os.path.basename(file1)} - {size_mb:.2f}MB")
            
            hacker_print(f"└── [TOTAL_SAVINGS] {len(duplicates)} files, {total_size:.2f}MB")
            
            if duplicates:
                confirm = input("\n[CONFIRM] Delete all duplicates? (y/n): ").lower()
                if confirm == 'y':
                    deleted_count = 0
                    deleted_size = 0
                    for file1, file2, size in duplicates:
                        try:
                            os.remove(file1)
                            deleted_count += 1
                            deleted_size += size
                        except:
                            continue
                    hacker_print(f"[SUCCESS] Removed {deleted_count} duplicates")
                    hacker_print(f"[SUCCESS] Freed {deleted_size/1024/1024:.2f}MB")
        else:
            hacker_print("[INFO] No duplicate files found")
        
        input("\nPress Enter to continue...")

def advanced_file_explorer():
    current_path = os.environ.get('USERPROFILE', '')
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 58 + "┐")
        hacker_print("│            ADVANCED FILE EXPLORER                      │")
        print("├" + "─" * 58 + "┤")
        hacker_print(f"│ Current: {current_path[:53]:<53} │")
        print("├" + "─" * 58 + "┤")
        
        try:
            items = os.listdir(current_path)
            dirs = []
            files = []
            
            for item in items:
                item_path = os.path.join(current_path, item)
                if os.path.isdir(item_path):
                    dirs.append(item)
                else:
                    files.append(item)
            
            hacker_print("│ [DIRECTORIES]                                       │")
            for i, dir_name in enumerate(dirs[:10], 1):
                hacker_print(f"│ {i:2d}. {dir_name:<50} │")
            
            hacker_print("│ [FILES]                                             │")
            for i, file_name in enumerate(files[:10], 1):
                file_path = os.path.join(current_path, file_name)
                try:
                    size = os.path.getsize(file_path)
                    size_kb = size / 1024
                    hacker_print(f"│ {i+len(dirs):2d}. {file_name:<36} {size_kb:8.1f}KB │")
                except:
                    hacker_print(f"│ {i+len(dirs):2d}. {file_name:<50} │")
            
            if len(dirs) + len(files) > 20:
                hacker_print(f"│ ... and {len(dirs) + len(files) - 20} more items                │")
                
        except PermissionError:
            hacker_print("│ [ERROR] Access denied                                │")
        except Exception as e:
            hacker_print(f"│ [ERROR] {str(e):<51} │")
        
        print("├" + "─" * 58 + "┤")
        hacker_print("│ [1-20] Open File/Directory                            │")
        hacker_print("│ [U] Go Up One Level                                  │")
        hacker_print("│ [H] Go to Home Directory                             │")
        hacker_print("│ [D] Go to Downloads                                  │")
        hacker_print("│ [S] Search Files                                     │")
        hacker_print("│ [B] Back to Main Menu                                │")
        print("└" + "─" * 58 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip().upper()
        
        if choice == 'B':
            break
        elif choice == 'U':
            parent = os.path.dirname(current_path)
            if os.path.exists(parent):
                current_path = parent
        elif choice == 'H':
            current_path = os.environ.get('USERPROFILE', '')
        elif choice == 'D':
            downloads = os.path.join(os.environ.get('USERPROFILE', ''), 'Downloads')
            if os.path.exists(downloads):
                current_path = downloads
        elif choice == 'S':
            search_term = input("[INPUT] Enter search term: ").strip().lower()
            if search_term:
                hacker_print(f"[SEARCHING] for '{search_term}'...")
                found_files = []
                for root, dirs, files in os.walk(current_path):
                    for file in files:
                        if search_term in file.lower():
                            found_files.append(os.path.join(root, file))
                            if len(found_files) >= 10:
                                break
                    if len(found_files) >= 10:
                        break
                
                if found_files:
                    hacker_print("[FOUND] Matching files:")
                    for i, file_path in enumerate(found_files, 1):
                        hacker_print(f"├── {i}. {os.path.basename(file_path)}")
                        hacker_print(f"│   └── {file_path}")
                else:
                    hacker_print("[INFO] No files found")
                input("\nPress Enter to continue...")
        elif choice.isdigit():
            index = int(choice) - 1
            try:
                items = os.listdir(current_path)
                if 0 <= index < len(items):
                    selected_item = items[index]
                    item_path = os.path.join(current_path, selected_item)
                    if os.path.isdir(item_path):
                        current_path = item_path
                    else:
                        hacker_print(f"[FILE_INFO] {selected_item}")
                        try:
                            size = os.path.getsize(item_path)
                            modified = datetime.fromtimestamp(os.path.getmtime(item_path))
                            hacker_print(f"│ Size: {size/1024/1024:.2f}MB")
                            hacker_print(f"│ Modified: {modified.strftime('%Y-%m-%d %H:%M')}")
                            hacker_print(f"│ Path: {item_path}")
                            
                            open_file = input("\n[INPUT] Open file? (y/n): ").lower()
                            if open_file == 'y':
                                if os.name == 'nt':
                                    os.startfile(item_path)
                                else:
                                    subprocess.run(['xdg-open', item_path])
                        except Exception as e:
                            hacker_print(f"[ERROR] {e}")
                        input("\nPress Enter to continue...")
            except:
                pass

def get_network_info():
    network_info = {}
    
    try:
        hostname = socket.gethostname()
        network_info['hostname'] = hostname
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        network_info['local_ip'] = local_ip
        
        interfaces = psutil.net_if_addrs()
        network_info['interfaces'] = interfaces
        
        if os.name == 'nt':
            try:
                result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
                network_info['ipconfig'] = result.stdout
            except:
                network_info['ipconfig'] = "Unable to get IP config"
        
        return network_info
    except Exception as e:
        hacker_print(f"[ERROR] Getting network info: {e}")
        return None

def network_configuration():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 58 + "┐")
        hacker_print("│            NETWORK CONFIGURATION                      │")
        print("├" + "─" * 58 + "┤")
        
        network_info = get_network_info()
        
        if network_info:
            hacker_print(f"[SYSTEM] Hostname: {network_info['hostname']}")
            hacker_print(f"[NETWORK] Local IP: {network_info['local_ip']}")
            
            hacker_print("[INTERFACES] Network adapters:")
            for interface, addrs in network_info['interfaces'].items():
                for addr in addrs:
                    if addr.family == socket.AF_INET and addr.address != '127.0.0.1':
                        hacker_print(f"├── {interface}: {addr.address}")
        
        print("├" + "─" * 58 + "┤")
        hacker_print("│ [1] Ping Google DNS                                 │")
        hacker_print("│ [2] Flush DNS Cache                                 │")
        hacker_print("│ [3] Display Routing Table                           │")
        hacker_print("│ [4] Return to Main Menu                             │")
        print("└" + "─" * 58 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip()
        
        if choice == '1':
            hacker_print("[PING] Testing connectivity to 8.8.8.8...")
            try:
                if os.name == 'nt':
                    result = subprocess.run(['ping', '-n', '4', '8.8.8.8'], capture_output=True, text=True)
                else:
                    result = subprocess.run(['ping', '-c', '4', '8.8.8.8'], capture_output=True, text=True)
                hacker_print("[PING_RESULT] Connection test completed")
            except:
                hacker_print("[ERROR] Ping failed")
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            hacker_print("[DNS] Flushing DNS cache...")
            try:
                if os.name == 'nt':
                    subprocess.run(['ipconfig', '/flushdns'], capture_output=True)
                else:
                    subprocess.run(['sudo', 'systemd-resolve', '--flush-caches'], capture_output=True)
                hacker_print("[SUCCESS] DNS cache flushed")
            except:
                hacker_print("[ERROR] Failed to flush DNS")
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            hacker_print("[ROUTE] Displaying routing table...")
            try:
                if os.name == 'nt':
                    result = subprocess.run(['route', 'print'], capture_output=True, text=True)
                else:
                    result = subprocess.run(['netstat', '-rn'], capture_output=True, text=True)
                lines = result.stdout.split('\n')[:15]
                for line in lines:
                    hacker_print(f"│ {line}")
            except:
                hacker_print("[ERROR] Failed to get routing table")
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            break

def get_wifi_passwords():
    """Get saved WiFi passwords on Windows"""
    if os.name != 'nt':
        hacker_print("[ERROR] This feature works only on Windows")
        return []
    
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, encoding='utf-8')
        profiles = []
        
        for line in result.stdout.split('\n'):
            if 'All User Profile' in line:
                profile_name = line.split(':')[1].strip()
                profiles.append(profile_name)
        
        wifi_info = []
        for profile in profiles:
            try:
                result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], 
                                      capture_output=True, text=True, encoding='utf-8')
                for line in result.stdout.split('\n'):
                    if 'Key Content' in line:
                        password = line.split(':')[1].strip()
                        wifi_info.append((profile, password))
                        break
            except:
                continue
        
        return wifi_info
    except Exception as e:
        hacker_print(f"[ERROR] Getting WiFi passwords: {e}")
        return []

def wifi_password_revealer():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 58 + "┐")
        hacker_print("│            WIFI PASSWORD REVEALER                     │")
        print("├" + "─" * 58 + "┤")
        
        if os.name != 'nt':
            hacker_print("│ [ERROR] This feature works only on Windows           │")
            print("├" + "─" * 58 + "┤")
            hacker_print("│ [1] Return to Main Menu                             │")
            print("└" + "─" * 58 + "┘")
            choice = input("\n[INPUT] Select operation: ").strip()
            if choice == '1':
                break
            continue
        
        hacker_print("[SCANNING] Saved WiFi networks...")
        wifi_passwords = get_wifi_passwords()
        
        if wifi_passwords:
            hacker_print("[FOUND] Saved WiFi networks with passwords:")
            for i, (ssid, password) in enumerate(wifi_passwords, 1):
                hacker_print(f"├── {i:2d}. {ssid:<40} │")
                hacker_print(f"│     Password: {password}")
            
            print("├" + "─" * 58 + "┤")
            hacker_print("│ [1] Export to text file                           │")
            hacker_print("│ [2] Show passwords again                          │")
            hacker_print("│ [3] Return to Main Menu                           │")
            print("└" + "─" * 58 + "┘")
        else:
            hacker_print("[INFO] No saved WiFi passwords found")
            print("├" + "─" * 58 + "┤")
            hacker_print("│ [1] Return to Main Menu                             │")
            print("└" + "─" * 58 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip()
        
        if choice == '1' and wifi_passwords:
            try:
                with open('wifi_passwords.txt', 'w', encoding='utf-8') as f:
                    f.write("BOGH - Saved WiFi Passwords\n")
                    f.write("=" * 50 + "\n")
                    for ssid, password in wifi_passwords:
                        f.write(f"SSID: {ssid}\n")
                        f.write(f"Password: {password}\n")
                        f.write("-" * 30 + "\n")
                hacker_print("[SUCCESS] Passwords saved to wifi_passwords.txt")
            except Exception as e:
                hacker_print(f"[ERROR] Saving file: {e}")
            input("\nPress Enter to continue...")
        elif choice == '2':
            continue
        elif choice == '3' or (not wifi_passwords and choice == '1'):
            break

def hardware_information():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 58 + "┐")
        hacker_print("│            HARDWARE INFORMATION                       │")
        print("├" + "─" * 58 + "┤")
        
        try:
            # CPU Information
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_cores = psutil.cpu_count(logical=False)
            cpu_threads = psutil.cpu_count(logical=True)
            cpu_freq = psutil.cpu_freq()
            
            # Memory Information
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            # Disk Information
            disk = psutil.disk_usage('/')
            disk_io = psutil.disk_io_counters()
            
            # Network Information
            net_io = psutil.net_io_counters()
            
            # Battery Information
            try:
                battery = psutil.sensors_battery()
            except:
                battery = None
            
            hacker_print("│ SYSTEM HEALTH & PERFORMANCE                       │")
            print("├" + "─" * 58 + "┤")
            hacker_print(f"│ CPU Usage: {cpu_percent:5.1f}% | Cores: {cpu_cores} | Threads: {cpu_threads}        │")
            if cpu_freq:
                hacker_print(f"│ CPU Frequency: {cpu_freq.current:.0f}MHz (Max: {cpu_freq.max:.0f}MHz)        │")
            hacker_print(f"│ RAM Usage: {memory.percent:5.1f}% | {memory.used//(1024**3)}GB/{memory.total//(1024**3)}GB used              │")
            hacker_print(f"│ Disk Usage: {disk.percent:5.1f}% | {disk.used//(1024**3)}GB/{disk.total//(1024**3)}GB used             │")
            
            if net_io:
                hacker_print(f"│ Network: ↓{net_io.bytes_recv//1024:6d}KB ↑{net_io.bytes_sent//1024:6d}KB                 │")
            
            if battery:
                hacker_print(f"│ Battery: {battery.percent:2d}% | {'Charging' if battery.power_plugged else 'On battery'} | {battery.secsleft//60}min left    │")
            
            # Health status
            health_status = "EXCELLENT"
            if memory.percent > 80 or disk.percent > 80:
                health_status = "NEEDS ATTENTION"
            if memory.percent > 90 or disk.percent > 90:
                health_status = "CRITICAL"
                
            hacker_print(f"│ SYSTEM HEALTH: {health_status:<38} │")
            
            print("├" + "─" * 58 + "┤")
            hacker_print("│ HARDWARE SPECIFICATIONS                           │")
            print("├" + "─" * 58 + "┤")
            hacker_print(f"│ Platform: {platform.processor()[:45]:<45} │")
            hacker_print(f"│ Architecture: {platform.machine():<42} │")
            hacker_print(f"│ System: {get_windows_version()[:45]:<45} │")
            
            # Disk partitions
            hacker_print("│ DISK PARTITIONS:                                  │")
            partitions = psutil.disk_partitions()
            for partition in partitions[:3]:  # Show first 3 partitions
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    hacker_print(f"│ ├── {partition.device} {usage.percent:3d}% used ({usage.free//1024**3}GB free) │")
                except:
                    hacker_print(f"│ ├── {partition.device} - Access denied           │")
            
        except Exception as e:
            hacker_print(f"[ERROR] Could not read hardware info: {e}")
        
        print("├" + "─" * 58 + "┤")
        hacker_print("│ [1] Refresh Information                             │")
        hacker_print("│ [2] Return to Main Menu                             │")
        print("└" + "─" * 58 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip()
        
        if choice == '1':
            continue
        elif choice == '2':
            break

def about_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 58 + "┐")
        hacker_print("│                   ABOUT                                │")
        print("├" + "─" * 58 + "┤")
        hacker_print("│           BOGH SYSTEM TOOLS v4.0                      │")
        hacker_print("│           Created by: yourwebbu1lder                  │")
        print("├" + "─" * 58 + "┤")
        hacker_print("│ [1] GitHub: github.com/yourwebbu1lder                 │")
        hacker_print("│ [2] Instagram: @yourwebbu1lder                        │")
        hacker_print("│ [3] Portfolio: yourwebbu1lder.dev                     │")
        print("├" + "─" * 58 + "┤")
        hacker_print("│ Features:                                              │")
        hacker_print("│ • Real-time System Monitoring                         │")
        hacker_print("│ • Advanced File Explorer                              │")
        hacker_print("│ • Network Configuration                               │")
        hacker_print("│ • WiFi Password Revealer                              │")
        hacker_print("│ • Hardware Information                                │")
        hacker_print("│ • Junk File Cleaner                                   │")
        hacker_print("│ • Duplicate File Hunter                               │")
        print("├" + "─" * 58 + "┤")
        hacker_print("│ [4] Return to Main Menu                               │")
        print("└" + "─" * 58 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip()
        
        if choice == '1':
            webbrowser.open('https://github.com/yourwebbu1lder')
            hacker_print("[SUCCESS] Opening GitHub...")
            time.sleep(1)
        elif choice == '2':
            webbrowser.open('https://instagram.com/yourwebbu1lder')
            hacker_print("[SUCCESS] Opening Instagram...")
            time.sleep(1)
        elif choice == '3':
            webbrowser.open('https://yourwebbu1lder.dev')
            hacker_print("[SUCCESS] Opening Portfolio...")
            time.sleep(1)
        elif choice == '4':
            break

def main():
    while True:
        choice = main_menu()
        
        if choice == '1':
            junk_file_cleaner()
        elif choice == '2':
            duplicate_file_hunter()
        elif choice == '3':
            advanced_file_explorer()
        elif choice == '4':
            network_configuration()
        elif choice == '5':
            wifi_password_revealer()
        elif choice == '6':
            hardware_information()
        elif choice == '7':
            about_section()
        elif choice == '8':
            hacker_print("\n[SYSTEM] Shutting down BOGH protocols...")
            time.sleep(1)
            hacker_print("[EXIT] BOGH System Tools terminated.")
            break
        else:
            hacker_print("[ERROR] Invalid command!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
