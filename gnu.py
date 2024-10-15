from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk  # For the styled progress bar
import os
from urllib.request import urlopen, HTTPError, URLError
import threading

fln = ''
filesize = 0


def startDownload():
    global fln
    # Ask the user where to save the file
    fln = filedialog.asksaveasfilename(
        initialdir=os.getcwd(),
        title="Save File",
        filetypes=(("JPG Image File", "*.jpg"), ("PNG Image File", "*.png"), ("All Files", "*.*"))
    )

    # If the user cancels the dialog, return
    if not fln:
        return

    filename.set(os.path.basename(fln))  # Set the filename in the UI
    progress_bar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')  # Show progress bar on download start
    threading.Thread(target=initDownload).start()  # Start download in a new thread


def initDownload():
    global filesize
    furl = url.get()

    try:
        target = urlopen(furl)
    except (HTTPError, URLError) as e:
        messagebox.showerror("Error", f"Failed to download file: {e}")
        return

    meta = target.info()
    filesize = float(meta['Content-Length'])  # Get file size in bytes

    downloaded = 0
    chunks = 1024 * 5  # Read 5KB chunks
    progress_bar['maximum'] = filesize  # Set maximum size for progress bar

    with open(fln, "wb") as f:
        while True:
            parts = target.read(chunks)
            if not parts:
                messagebox.showinfo("Download Complete", "Your Download Has Been Completed Successfully")
                break

            downloaded += len(parts)
            f.write(parts)

            # Update download progress (show in KB/MB depending on size)
            if downloaded < 1024 * 1024:  # Show in KB until 1 MB
                download_progress.set(f"{round(downloaded / 1024, 2)} KB / {round(filesize / 1024, 2)} KB")
            else:  # Show in MB after 1 MB
                download_progress.set(f"{round(downloaded / 1024 / 1024, 2)} MB / {round(filesize / 1024 / 1024, 2)} MB")

            # Calculate and update percentage
            download_percentage.set(f"{round((downloaded / filesize) * 100, 2)}%")
            
            # Update progress bar
            progress_bar['value'] = downloaded

    f.close()

    # Hide progress bar after download completes
    progress_bar.grid_remove()


def exitProg():
    if messagebox.askyesno("Exit Program?", "Are you sure you want to exit the program?") == False:
        return
    root.quit()


# Initialize the main window
root = Tk()

# Tkinter variables
url = StringVar()
filename = StringVar()
download_progress = StringVar()
download_percentage = StringVar()

# Default values for progress and percentage
download_progress.set("N/A")
download_percentage.set("N/A")

# URL input frame
wrapper = LabelFrame(root, text="File URL")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

# Download information frame
wrapper2 = LabelFrame(root, text="Download Information")
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

# URL entry and download button
lbl = Label(wrapper, text="Download URL: ")
lbl.grid(row=0, column=0, padx=10, pady=10)

ent = Entry(wrapper, textvariable=url)
ent.grid(row=0, column=1, padx=5, pady=10)

btn = Button(wrapper, text="Download", command=startDownload)
btn.grid(row=0, column=2, padx=5, pady=10)

# Download info labels
lbl2 = Label(wrapper2, text="File: ")
lbl2.grid(row=0, column=0, padx=10, pady=10)

lbl3 = Label(wrapper2, textvariable=filename)
lbl3.grid(row=0, column=1, padx=10, pady=10)

lbl4 = Label(wrapper2, text="Download Progress")
lbl4.grid(row=1, column=0, padx=10, pady=10)

lbl5 = Label(wrapper2, textvariable=download_progress)
lbl5.grid(row=1, column=1, padx=10, pady=10)

lbl6 = Label(wrapper2, text="Download Percentage")
lbl6.grid(row=2, column=0, padx=10, pady=10)

lbl7 = Label(wrapper2, textvariable=download_percentage)
lbl7.grid(row=2, column=1, padx=10, pady=10)

# Style the progress bar to make it smoother with curved edges
style = ttk.Style()
style.theme_use('clam')  # Use 'clam' theme which allows more customization
style.configure("TProgressbar",
                thickness=15,
                troughcolor='#DDDDDD',
                background='#4CAF50',
                troughrelief='flat',
                borderwidth=0)
style.layout("TProgressbar",
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'})])

# Progress bar for download (hidden initially, expands to full width)
progress_bar = ttk.Progressbar(wrapper2, orient=HORIZONTAL, mode='determinate', style="TProgressbar")
progress_bar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')  # Span full width
progress_bar.grid_remove()  # Hide the progress bar initially

# Exit button
Button(wrapper2, text="Exit Downloader", command=exitProg).grid(row=4, column=0, padx=10, pady=10)

# Main window settings
root.geometry("450x400")
root.title("File Downloader")
root.resizable(False, False)

root.mainloop()
