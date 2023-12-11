from sort import sort
import config

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class myHandler(FileSystemEventHandler):
    def on_created(self, event):
        sort()

    def on_moved(self, event):
        sort()


def main():
    config.load_config()
    downloads_path = config.get_downloads_path()

    observer = Observer()
    observer.schedule(myHandler(), downloads_path, recursive=True)
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()