import threading

from click_canvas import MainWindow
from web_feed import WebFeed

wf = WebFeed()
wf.get_feed()

# window = MainWindow()
# window.run()
# window_thread = threading.Thread(target=MainWindow().run())


