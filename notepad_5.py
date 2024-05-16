import time
from pywinauto.application import Application

app = Application(backend="uia", allow_magic_lookup=False).start('notepad.exe')
main = app['Untitled - Notepad']
main.wrapper_object().maximize()  # while debugging
main.menu_select('File->Print')  # 'click' instead of 'Click'

# Wait for the Print dialog to appear
time.sleep(1)  # Adjust the sleep duration as needed

# Connect to the Print dialog
print_dialog = main["print"]
print_dialog.print_control_identifiers()

var=print_dialog.child_window(title="Folder View", auto_id="1", control_type="List").click_input()

# Interact with the Print dialog
# Get the printer combobox and select the desired printer (replace "Printer Name" with the actual printer name)
printer_combobox = app.child_window(title="Microsoft Print to PDF", control_type="ListItem").wrapper_object
printer_combobox.select(1)
var=app.child_window(title="Print", auto_id="1", control_type="Button").click_input()




'''nex=app.printer_combobox.child_window(title="OneNote for Windows 10", control_type="ListItem").wrapper_object
nex.click_input()'''
'''# Set the number of copies
copies_edit = print_dialog.child_window(title="Copies:", control_type="Edit")
copies_edit.set_text("5")

# Click the Print button
print_button = print_dialog.child_window(title="Print", control_type="Button")
print_button.click()

# Wait for the Print dialog to close
time.sleep(1)  # Adjust the sleep duration as needed

# Close the Note'''