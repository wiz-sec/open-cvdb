import os
import re

def fix_yaml_image_format(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    fixed_lines = []
    i = 0
    while i < len(lines):
        if re.match(r'^image:\s*$', lines[i]):  # Match "image:" on its own line
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('http'):  # Next line contains URL
                fixed_lines.append(f"image: {lines[i + 1].strip()}\n")
                i += 1  # Skip the next line as it's now merged
            else:
                fixed_lines.append(lines[i])
        else:
            fixed_lines.append(lines[i])
        i += 1
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(fixed_lines)

def process_yaml_files():
    for file in os.listdir():
        if file.endswith('.yaml') or file.endswith('.yml'):
            fix_yaml_image_format(file)

if __name__ == "__main__":
    process_yaml_files()
