import threading

from click_canvas import MainWindow

# wf = WebFeed()
# wf.get_feed()

window = MainWindow()
window.run()
window_thread = threading.Thread(target=MainWindow().run())


