import zipfile, os

def zipar(src, dest):
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(src):
            for f in files:
                z.write(os.path.join(root,f), os.path.relpath(os.path.join(root,f), src))

zipar('discord_monitor_ai','discord_monitor_ai.zip')
print("ZIP gerado com sucesso.")
