# TechZone

TechZone is a Python program designed to optimize and manage file associations and shortcuts on Windows systems. By allowing users to associate file types with specific programs and create shortcuts efficiently, TechZone enhances user productivity and system organization.

## Features

- **File Association Management**: Associate file extensions with specific programs.
- **Shortcut Creation**: Create and manage shortcuts to streamline access to frequently used applications.
- **List Associations and Shortcuts**: View current file associations and shortcuts.
- **Remove Associations and Shortcuts**: Clean up unnecessary file associations and shortcuts.

## Prerequisites

- Python 3.x
- `pywin32` library (for managing shortcuts)

You can install `pywin32` using pip:

```bash
pip install pywin32
```

## Usage

1. **Adding a File Association**

   ```python
   tz.add_file_association('.txt', 'C:\\Program Files\\Notepad++\\notepad++.exe')
   ```

2. **Creating a Shortcut**

   ```python
   tz.create_shortcut('C:\\Program Files\\Notepad++\\notepad++.exe', 'C:\\Users\\YourUsername\\Desktop\\Notepad++.lnk')
   ```

3. **Listing Current Associations and Shortcuts**

   ```python
   tz.list_associations()
   tz.list_shortcuts()
   ```

4. **Removing a File Association**

   ```python
   tz.remove_file_association('.txt')
   ```

5. **Removing a Shortcut**

   ```python
   tz.remove_shortcut('C:\\Users\\YourUsername\\Desktop\\Notepad++.lnk')
   ```

## Note

- Administrative privileges may be required to modify some system settings.
- Use this program responsibly, as incorrect modifications can affect system behavior.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This program utilizes the `pywin32` library for Windows-specific functionalities.