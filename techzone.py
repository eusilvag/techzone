import os
import winreg

class TechZone:
    def __init__(self):
        self.associations = {}
        self.shortcuts = {}

    def add_file_association(self, extension, program_path):
        """Associates a file extension with a specific program."""
        try:
            key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, extension)
            winreg.SetValue(key, '', winreg.REG_SZ, f'{extension}_auto_file')
            key2 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f'{extension}_auto_file\\shell\\open\\command')
            winreg.SetValue(key2, '', winreg.REG_SZ, f'"{program_path}" "%1"')
            self.associations[extension] = program_path
            print(f"Associated {extension} with {program_path}")
        except Exception as e:
            print(f"Failed to associate {extension}: {e}")

    def create_shortcut(self, target, shortcut_path):
        """Creates a shortcut for a given target at the specified location."""
        try:
            import pythoncom
            from win32com.shell import shell, shellcon

            shortcut = shell.CreateShortcut(shortcut_path)
            shortcut.TargetPath = target
            shortcut.IconLocation = target
            shortcut.save()
            self.shortcuts[target] = shortcut_path
            print(f"Shortcut created at {shortcut_path}")
        except Exception as e:
            print(f"Failed to create shortcut: {e}")

    def remove_file_association(self, extension):
        """Removes file association for a given extension."""
        try:
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, f'{extension}_auto_file\\shell\\open\\command')
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, extension)
            del self.associations[extension]
            print(f"Removed association for {extension}")
        except Exception as e:
            print(f"Failed to remove association for {extension}: {e}")

    def remove_shortcut(self, shortcut_path):
        """Removes a shortcut from the specified location."""
        try:
            os.remove(shortcut_path)
            target = [k for k, v in self.shortcuts.items() if v == shortcut_path]
            if target:
                del self.shortcuts[target[0]]
            print(f"Removed shortcut at {shortcut_path}")
        except Exception as e:
            print(f"Failed to remove shortcut: {e}")

    def list_associations(self):
        """Lists all current file associations."""
        print("Current file associations:")
        for ext, prog in self.associations.items():
            print(f"{ext}: {prog}")

    def list_shortcuts(self):
        """Lists all current shortcuts."""
        print("Current shortcuts:")
        for target, path in self.shortcuts.items():
            print(f"{path} -> {target}")

if __name__ == "__main__":
    tz = TechZone()
    # Example usage:
    # tz.add_file_association('.txt', 'C:\\Program Files\\Notepad++\\notepad++.exe')
    # tz.create_shortcut('C:\\Program Files\\Notepad++\\notepad++.exe', 'C:\\Users\\YourUsername\\Desktop\\Notepad++.lnk')
    # tz.list_associations()
    # tz.list_shortcuts()
    # tz.remove_file_association('.txt')
    # tz.remove_shortcut('C:\\Users\\YourUsername\\Desktop\\Notepad++.lnk')