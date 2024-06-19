import tkinter as tk
from tkinter import messagebox
import pyautogui
import cv2
import numpy as np
from threading import Thread, Event

class ScreenRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen Recorder")
        
        # Start button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_recording)
        self.start_button.pack()
        
        # Pause button
        self.pause_button = tk.Button(self.root, text="Pause", state=tk.DISABLED, command=self.pause_recording)
        self.pause_button.pack()
        
        # Resume button
        self.resume_button = tk.Button(self.root, text="Resume", state=tk.DISABLED, command=self.resume_recording)
        self.resume_button.pack()
        
        # Stop button
        self.stop_button = tk.Button(self.root, text="Stop", state=tk.DISABLED, command=self.stop_recording)
        self.stop_button.pack()
        
        self.is_recording = Event()
        self.is_paused = Event()
        self.is_paused.set()  # Start in paused state
        
        self.thread = None
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def start_recording(self):
        if self.thread is None:
            self.is_recording.set()
            self.is_paused.set()
            self.thread = Thread(target=self.record_screen)
            self.thread.start()
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
    
    def pause_recording(self):
        self.is_paused.clear()
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.NORMAL)
    
    def resume_recording(self):
        self.is_paused.set()
        self.pause_button.config(state=tk.NORMAL)
        self.resume_button.config(state=tk.DISABLED)
    
    def stop_recording(self):
        self.is_recording.clear()
        self.is_paused.set()
        self.thread.join()
        self.thread = None
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def record_screen(self):
        resolution = (1920, 1080)
        codec = cv2.VideoWriter_fourcc(*"XVID")
        filename = "Recording.avi"
        fps = 20.0
        out = cv2.VideoWriter(filename, codec, fps, resolution)
        
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Live", 480, 270)
        
        while self.is_recording.is_set():
            self.is_paused.wait()
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            cv2.imshow('Live', frame)
            
            if cv2.waitKey(1) == ord('q'):
                break

        out.release()
        cv2.destroyAllWindows()

    def on_closing(self):
        if self.is_recording.is_set():
            if messagebox.askokcancel("Quit", "Do you want to stop the recording and quit?"):
                self.stop_recording()
                self.root.destroy()
        else:
            self.root.destroy()

if __name__ == "__main__":
    ScreenRecorder()
