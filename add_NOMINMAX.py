# -*-coding:utf-8-*- 
import os 
for root,dirs,files in os.walk("."):
    for file in files: 
        if file.endswith('.h') or file.endswith('.h.in'):
            path = os.path.join(root, file)
            content = '#define NOMINMAX\n'
            with open(path) as f:
                content += f.read()
            with open(path, 'w') as f:
                f.write(content)
            