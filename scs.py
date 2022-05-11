#!/usr/bin/python3

import signal

import gi
from Xlib import X, display

gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")

from gi.repository import Gdk, GLib, Gtk

from keyutil import get_posmap, initkeys
from pointer import pointer_position

n_monitors = Gdk.Display.get_default().get_n_monitors()
keys = ["h", "j", "k", "l"][1 - n_monitors // 4 : 3 + n_monitors // 3]


def global_inital_states():
    displ = display.Display()
    rt = displ.screen().root
    rt.change_attributes(event_mask=X.KeyPressMask)

    return (displ, rt, get_posmap(keys, displ))


global disp, root, posmap


def run():
    global disp, root, posmap
    disp, root, posmap = global_inital_states()

    initkeys(keys, disp, root)
    for _ in range(0, root.display.pending_events()):
        root.display.next_event()
    GLib.io_add_watch(root.display, GLib.IO_IN, checkevt)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    Gtk.main()


def checkevt(_, __, handle=None):
    handle = handle or root.display
    for _ in range(0, handle.pending_events()):
        event = handle.next_event()

        if event.type == X.KeyPress:
            handle_pointer_event(event.detail)

    return True


def handle_pointer_event(key):
    return pointer_position(posmap[key])


if __name__ == "__main__":
    run()
