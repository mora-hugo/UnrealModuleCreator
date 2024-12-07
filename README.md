
# Unreal Module Creator

**Unreal Module Creator** is a lightweight, cross-platform tool designed to streamline the creation of Unreal Engine modules. It automates the generation of folder structures, configuration files, and boilerplate code, helping developers save time and maintain consistency.

---

## 🚀 Features

- **Module Automation**: Quickly create Unreal Engine module files (`.Build.cs`, `.h`, `.cpp`) with a single command.
- **Customizable Templates**: Adjust the included templates to match your project's coding style.
---

## 📦 Installation

### Option 1: Python Script

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/UnrealModuleCreator.git
   cd UnrealModuleCreator
   ```

2. Install Python dependencies (if required):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python create_module.py <ModuleName> [BasePath]
   ```

### Option 2: Standalone Executable

1. Download the latest version of the standalone executable from the [Releases page](https://github.com/YourUsername/UnrealModuleCreator/releases).
2. Run the installer to enable global access.

---

## 💻 Usage

### Python Script

Use the following command to create a module:
```bash
create_module.py MyModule ./MyProject
```

### Standalone Executable

For the standalone version:
```bash
create_module MyModule C:\UnrealProjects\MyGame
```

---

## ✏️ Customization

Templates are stored in the `Template/` directory. You can modify these files to match your project's coding conventions:

- **`Module.Build.cs.template`**: For the module build configuration.
- **`ModuleModule.h.template`**: For the module header file.
- **`ModuleModule.cpp.template`**: For the module source file.

---

## 🤝 Contribution

Contributions are welcome! You can:

- Report bugs or suggest features by opening an issue.
- Submit a pull request with improvements to the tool or its documentation.
