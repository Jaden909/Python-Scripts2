import time
print('Rock Launcher v0.0 DEV')
_=input('What do you want to do? (start game or start engine)\n').lower()
if _=='start game':
    print('Starting game...')
    time.sleep(0.5)
    try:    
        import QuarryTycoonPROTO
    except ImportError:
        print('Game failed to start. Most likely due to missing file or fatal error when starting.')
if _=='start engine':
    print('Starting engine...')
    time.sleep(0.5)
    try:    
        import PyEngine
        print('Engine sucessfully started.')
    except ImportError:
        print('Engine failed to start. Most likely due to missing file or fatal error when starting. Game will also fail to start.')