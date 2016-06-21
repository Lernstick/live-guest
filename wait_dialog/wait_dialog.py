#!/usr/bin/env python2
CHECK_FREQUENCY = 1  # seconds
LOG_TO_SYSLOG = True

import os
from subprocess import Popen, PIPE

import gi
from gi.repository import Gtk, GLib

script_dir = os.path.dirname(os.path.abspath(__file__))

builder = Gtk.Builder()
builder.add_from_file(script_dir + '/dialog.glade')
handlers = {
    "on_continue_without_stick_clicked": Gtk.main_quit,
}
builder.connect_signals(handlers)
w = builder.get_object('wait_dialog')
w.resize(370, 170)
w.set_position(Gtk.WindowPosition.CENTER)
w.show_all()

def log(msg):
    print(msg)
    if LOG_TO_SYSLOG:
        p = Popen(['/usr/bin/logger', '-t', 'live-guest-wait', '-p', 'user.notice'],
                  stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.communicate(msg)

def check():
    log("Checking...")
    if 0 == os.system("id live-guest 2>/dev/null"):
        log("Live-guest mounted, exiting!")
        Gtk.main_quit() 
    GLib.timeout_add_seconds(CHECK_FREQUENCY, check)

GLib.timeout_add_seconds(CHECK_FREQUENCY, check)
Gtk.main()
