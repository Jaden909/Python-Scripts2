import Computer,pygame,PyEngine,sys,os
print(Computer.path)
i=1
for root, dirs, files in os.walk(f'{Computer.path}\\Apps'):
    for name in dirs:
        if name[0].isupper():
            meta=PyEngine.load(f'{Computer.path}\\Apps\\{name}\\meta.json')
            print(f'App {i}:')
            print(meta.get('title'))
            print(meta.get('description'))
            print(meta.get('id'))
            print(meta.get('author'))
            print(meta.get('modified'))
            i+=1
print(f'{i-1} apps installed.')      
def loop():
    pass