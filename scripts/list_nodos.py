import os
BASE = os.path.expanduser('~/workspace/projects/esquema-red-nodos')
for root, dirs, files in os.walk(BASE):
    depth = root.replace(BASE, '').count(os.sep)
    indent = '  ' * depth
    print(f"{indent}- {os.path.basename(root) or 'root'}")
    for f in files:
        print(f"{indent}  * {f}")
