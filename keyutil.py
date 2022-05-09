from Xlib import X
from Xlib.keysymdef import latin1


def get_posmap(keys, disp):
    posmap = {}
    for i, key in enumerate(keys):
        posmap[keycode(key, disp)] = i

    return posmap


def initkeys(keys, disp, root):
    return [initkey(keycode(key, disp), root) for key in keys]


def initkey(code, root):
    root.grab_key(
        code,
        X.Mod1Mask | X.ShiftMask,
        1,
        X.GrabModeAsync,
        X.GrabModeAsync,
    )
    root.grab_key(
        code,
        X.Mod1Mask | X.Mod2Mask | X.ShiftMask,
        1,
        X.GrabModeAsync,
        X.GrabModeAsync,
    )

    return code


def keycode(key, disp):
    return disp.keysym_to_keycode(getattr(latin1, "XK_{}".format(key)))
