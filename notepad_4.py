import time
from pywinauto.application import Application,timings

app = Application(backend="uia").start('notepad.exe')
main = app['Untitled - Notepad']
main.wrapper_object().maximize() # while debugging
main.menu_select("Edit -> Replace")
main.Replace.print_control_identifiers()
main.Replace.Cancel.click()
main.Edit.type_keys("Hi from Python interactive prompt %s" % str(dir()), with_spaces=True)
main.type_keys('^a')  # Simulate Ctrl+A keyboard shortcut
# main.menu_select("File -> Exit")
main.menu_select(u'F&ormat->&Font...') # 'click' instead of 'Click'
main.ComboBox0.Edit.set_text(u'Arial')
main.OK.click()
main.menu_select("File -> Exit")
main.SaveAs.click()
save_as_window = main['Save As']
# Set the file name and path
save_as_window.Pane.ComboBox0.Edit.set_text("C:\\Users\\nraman\\Desktop\\New folder\\file2.txt")
# Click the Save button
save_as_window.Cancel.click()
main.menu_select('File->print') # 'click' instead of 'Click'
ctrl = main['&Print']
main.Print.print_control_identifiers()
vary=ctrl.child_window(title="Folder View", auto_id="1", control_type="List").click_input()
dif=ctrl.child_window(title="Microsoft Print to PDF", control_type="ListItem")
#dif.select(1)
ctrl.child_window(title="Print", auto_id="1", control_type="Button").click_input()
ctrl.Print.click()
