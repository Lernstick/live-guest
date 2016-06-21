Copy the `wait_dialog` dir to `/usr/share/live-guest/wait_dialog` and add the
following lines to `/etc/gdm3/Init/Default`:

    xsetroot -cursor_name X_cursor
    /usr/share/live-guest/wait_dialog/wait_dialog.py
