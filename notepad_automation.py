from pywinauto.application import Application

# Launch Notepad
app = Application().start("notepad.exe")
main_window = app["Untitled - Notepad"]

# Do something with the Notepad window
main_window.menu_select("Help->About Notepad")
about_window = app["About Notepad"]

about_window.print_control_identifiers()

# Close the windows
about_window.OK.click()
main_window.menu_select("File->	Open")

