# File Downloader

This is a simple **File Downloader** application built using Python's `Tkinter` library for the GUI. It allows users to download files from the internet by providing a URL.

## Features

- **Download Files from URL**: Users can input a file URL to download files such as images, documents, or any type of file available via HTTP.
- **Save File Dialog**: Allows the user to select a file name and location to save the downloaded file, with file type options (e.g., JPG, PNG).
- **Automatic File Extension Handling**: Automatically appends the correct file extension (e.g., `.jpg`, `.png`, etc.) based on the file type selected by the user in the save dialog.
- **Smooth Progress Bar**: A styled, smooth, and centralized progress bar with curved edges that displays the current download progress.
- **Download Progress Display**: Real-time download progress displayed in both percentage and actual size (KB/MB).
- **Threaded Downloading**: The downloading process runs in a separate thread to prevent the UI from freezing during large downloads.
- **Exit Confirmation**: The user is prompted for confirmation before exiting the application.

## Installation and Requirements

### Prerequisites

1. **Python 3.x**: Ensure you have Python installed. You can download Python from [here](https://www.python.org/downloads/).
2. **Required Libraries**: The following libraries are required:
   - `Tkinter` (comes pre-installed with Python).
   - `urllib` (comes with Python’s standard library).
   - `threading` (used to run the download on a separate thread).
   
   Since these libraries are part of Python’s standard distribution, no extra installation is required.

### Steps to Run

1. Clone or download the project files to your local machine.
   
   ```bash
   git clone <repository-url>
