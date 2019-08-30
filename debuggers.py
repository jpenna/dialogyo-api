def debug_vscode():
    import ptvsd
    ptvsd.enable_attach(address=('localhost', 5678))
