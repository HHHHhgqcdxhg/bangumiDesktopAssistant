from config import config

def setFocusedOpacity(el):
    el.setOpacity(config.elFocusedOpacity)

def setUnfocusedOpacity(el):
    el.setOpacity(config.elUnfocusedOpacity)
