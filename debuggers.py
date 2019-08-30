def debug_vscode():
    import ptvsd
    ptvsd.enable_attach(address=('127.0.0.1', 5678))
