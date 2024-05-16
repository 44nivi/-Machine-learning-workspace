import time
from pywinauto.application import Application
app = Application(backend="uia").start('notepad.exe')
main=app['Untitled - Notepad']
# is the same as
main.menu_select("Edit -> Replace")
main.Replace.print_control_identifiers()
main.Replace.Cancel.click()
main.Edit.type_keys("Hi from Python interactive prompt %s" % str(dir()), with_spaces = True)
main.SaveAs.click()
save_as_window = main['Save As']
# Set the file name and path
save_as_window.Pane.ComboBox0.Edit.set_text("C:\\Users\\nraman\\Desktop\\New folder\\file2.txt")
# Click the Save button
save_as_window.Cancel.click()
