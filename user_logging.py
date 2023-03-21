import dbus
import dbus.mainloop.glib
from gi.repository import GLib

def on_login(*args):
    # Extract the user ID from the login event
    uid = args[0][0]

    # Do something with the user ID (e.g., print it)
    print(f"User {uid} logged in")


def main():

    # Set up a DBus connection to the system logind service
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    logind = bus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
    manager = dbus.Interface(logind, 'org.freedesktop.login1.Manager')

    # Subscribe to login events
    manager.connect_to_signal('UserNew', on_login)

    # Start the main event loop to listen for events
    loop = GLib.MainLoop()
    loop.run()


if __name__ == '__main__':
    main()
