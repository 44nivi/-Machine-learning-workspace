from pywinauto.application import Application
app = Application(backend="uia").start('notepad.exe')

# describe the window inside Notepad.exe process
dlg_spec = app.UntitledNotepad
# wait till the window is really open
# actionable_dlg = dlg_spec.wait('visible')
dlg_spec = app.window(title='Untitled - Notepad')
dlg_spec.wrapper_object().minimize() # while debugging
dlg_spec.print_control_identifiers()
