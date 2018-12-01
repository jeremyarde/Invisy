import threading
from multiprocessing.pool import ThreadPool

from src.click_canvas import MainWindow
from src.web_feed import WebFeed


# wf = WebFeed()
# wf.get_feed()

window = MainWindow()
window.run()
window_thread = threading.Thread(target=MainWindow().run())


