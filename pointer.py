from gi.repository import Gdk


def move_pointer_to(x, y):
    display = Gdk.Display.get_default()
    screen = Gdk.Screen.get_default()
    pointer = display.get_default_seat().get_pointer()
    pointer.warp(screen, x, y)
    # -> flush
    pointer.get_position()


def pointer_position(pos):
    display = Gdk.Display.get_default()

    monitor = display.get_monitor(pos)
    workarea = monitor.get_workarea()

    center = (
        0.5 * workarea.width + workarea.x,
        0.5 * workarea.height + workarea.y,
    )
    move_pointer_to(*center)
