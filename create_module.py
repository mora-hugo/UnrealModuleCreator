import os
import sys

# PyInstaller temporary directory
def get_template_dir():
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "Template")
    return os.path.join(os.path.dirname(__file__), "Template")

TEMPLATE_DIR = get_template_dir()

def read_template(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Template {filepath} not found.")
        sys.exit(1)

def replace_placeholders(template, module_name):
    return template.replace("{{MODULE_NAME}}", module_name)

def resolve_path(base_path):
    return os.path.abspath(base_path) if os.path.isabs(base_path) else os.path.abspath(os.path.join(os.getcwd(), base_path))

def create_directories(base_path, module_name):
    source_dir = os.path.join(base_path)
    module_dir = os.path.join(source_dir, module_name)
    public_dir = os.path.join(module_dir, "Public")
    private_dir = os.path.join(module_dir, "Private")
    os.makedirs(public_dir, exist_ok=True)
    os.makedirs(private_dir, exist_ok=True)
    return module_dir, public_dir, private_dir

def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def copy_templates(module_name, module_dir, public_dir, private_dir):
    build_cs_path = os.path.join(module_dir, f"{module_name}.Build.cs")
    module_header_path = os.path.join(public_dir, f"{module_name}Module.h")
    module_cpp_path = os.path.join(private_dir, f"{module_name}Module.cpp")

    build_cs_template = read_template(os.path.join(TEMPLATE_DIR, "Module.Build.cs.template"))
    header_template = read_template(os.path.join(TEMPLATE_DIR, "Public", "ModuleModule.h.template"))
    cpp_template = read_template(os.path.join(TEMPLATE_DIR, "Private", "ModuleModule.cpp.template"))

    build_cs_content = replace_placeholders(build_cs_template, module_name)
    header_content = replace_placeholders(header_template, module_name)
    cpp_content = replace_placeholders(cpp_template, module_name)

    write_file(build_cs_path, build_cs_content)
    write_file(module_header_path, header_content)
    write_file(module_cpp_path, cpp_content)

def create_module(module_name, base_path="."):
    resolved_path = resolve_path(base_path)
    module_dir, public_dir, private_dir = create_directories(resolved_path, module_name)
    copy_templates(module_name, module_dir, public_dir, private_dir)
    print(f"Module '{module_name}' created successfully in '{os.path.abspath(module_dir)}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_module.py <ModuleName> [BasePath]")
        sys.exit(1)

    module_name = sys.argv[1]
    base_path = sys.argv[2] if len(sys.argv) > 2 else "."
    create_module(module_name, base_path)
