import os
import shutil
import logging
import re

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class DownloadHandler:
    def __init__(self, source_folder, target_folder, series_name):
        self.series_name = self.normalize_name(series_name)
        self.source_folder = source_folder
        self.target_folder = target_folder

        logging.info(f"Trying to move downloaded episodes of '{series_name}'.")
        logging.info(f"From: {source_folder} | To: {target_folder}")

    def move_files(self):
        """Scans the downloads folder and moves matching files to the correct season folder."""
        if not os.path.exists(self.source_folder):
            logging.warning(f"Source folder '{self.source_folder}' does not exist. Skipping.")
            return

        files_moved = 0
        for filename in os.listdir(self.source_folder):
            normalized_filename = self.normalize_name(filename)
            
            if self.series_name in normalized_filename:
                season_folder = self.get_season_folder(filename)

                if season_folder:
                    source = os.path.join(self.source_folder, filename)
                    destination = os.path.join(self.target_folder, season_folder, filename)

                    os.makedirs(os.path.dirname(destination), exist_ok=True)

                    try:
                        shutil.move(source, destination)
                        logging.info(f"Moved: {filename} → {destination}")
                        files_moved += 1
                    except Exception as e:
                        logging.error(f"Failed to move {filename}: {e}")

        if files_moved == 0:
            logging.info("No matching series found to move.")
        else:
            logging.info(f"Finished moving {files_moved} files.")

    def get_season_folder(self, filename):
        """Extracts the season number from a filename and returns the corresponding folder name."""
        match = re.search(r"[sS](\d{2})", filename)

        if match:
            return f"S{match.group(1)}"
        else:
            logging.debug(f"Could not determine season for '{filename}'. Skipping.")
            return None

    def normalize_name(self, name):
        """Replaces separators (._-) with spaces and converts to lowercase."""
        return re.sub(r"[._-]", " ", name).lower().strip()


def move_existing_files(source_folder, target_folder, series_name):
    """Creates a handler and moves files accordingly."""
    handler = DownloadHandler(source_folder, target_folder, series_name)
    handler.move_files()
    logging.info("File processing complete.")


if __name__ == "__main__":
    downloads_folder = os.path.expanduser("~/Downloads")

    series_name = input("Enter the TV series name: ").strip()
    target_folder = os.path.expanduser(f"~/videos/{series_name}")

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        logging.info(f"Created target folder: {target_folder}")

    move_existing_files(downloads_folder, target_folder, series_name)
