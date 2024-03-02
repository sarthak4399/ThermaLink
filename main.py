import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import datetime  # For timestamping logs

class TemperatureRegulationApp:
    def __init__(self, master):
        self.master = master
        master.title("Temperature Regulation HMI")

        # Initialize temperature variable and setpoint control variables
        self.temperature = tk.DoubleVar()
        self.setpoint = tk.DoubleVar(value=25.0)  # Default setpoint temperature
        self.runtime = tk.StringVar()

        # Create frames for layout
        self.temperature_frame = ttk.Frame(master)
        self.temperature_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.controls_frame = ttk.Frame(master)
        self.controls_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Create temperature label and display
        self.temperature_label = ttk.Label(self.temperature_frame, text="Temperature:", font=("Arial", 12))
        self.temperature_label.grid(row=0, column=0, padx=5, pady=5)
        self.temperature_display = ttk.Label(self.temperature_frame, textvariable=self.temperature, font=("Arial", 12))
        self.temperature_display.grid(row=0, column=1, padx=5, pady=5)

        # Create setpoint label, entry, and update button
        self.setpoint_label = ttk.Label(self.controls_frame, text="Setpoint:", font=("Arial", 12))
        self.setpoint_label.grid(row=0, column=0, padx=5, pady=5)
        self.setpoint_entry = ttk.Entry(self.controls_frame, textvariable=self.setpoint, font=("Arial", 12))
        self.setpoint_entry.grid(row=0, column=1, padx=5, pady=5)
        self.update_setpoint_button = ttk.Button(self.controls_frame, text="Update Setpoint", command=self.update_setpoint)
        self.update_setpoint_button.grid(row=0, column=2, padx=5, pady=5)

        # Create process runtime label
        self.runtime_label = ttk.Label(self.controls_frame, text="Process Runtime:", font=("Arial", 12))
        self.runtime_label.grid(row=1, column=0, padx=5, pady=5)
        self.runtime_display = ttk.Label(self.controls_frame, textvariable=self.runtime, font=("Arial", 12))
        self.runtime_display.grid(row=1, column=1, padx=5, pady=5)

        # Create temperature slider
        self.temperature_slider = tk.Scale(self.controls_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                                           variable=self.temperature, command=self.update_temperature)
        self.temperature_slider.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        # Create get logs button
        self.get_logs_button = ttk.Button(self.controls_frame, text="Get Logs", command=self.get_logs)
        self.get_logs_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # Start process runtime
        self.start_time = datetime.datetime.now()
        self.update_runtime()

    def update_temperature(self, value):
        # Update temperature label when slider value changes
        self.temperature.set(float(value))

    def update_setpoint(self):
        # Update setpoint temperature
        try:
            new_setpoint = float(self.setpoint.get())
            self.setpoint.set(new_setpoint)
            messagebox.showinfo("Success", "Setpoint updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid setpoint value. Please enter a valid number.")

    def update_runtime(self):
        # Update process runtime label
        elapsed_time = datetime.datetime.now() - self.start_time
        self.runtime.set(str(elapsed_time))

        # Update runtime label every second
        self.master.after(1000, self.update_runtime)

    def get_logs(self):
        # Function to get logs (placeholder)
        logs = "Sample logs:\n"
        logs += "Timestamp: {}\n".format(datetime.datetime.now())
        logs += "Temperature: {}\n".format(self.temperature.get())
        logs += "Setpoint: {}\n".format(self.setpoint.get())
        logs += "Process Runtime: {}\n".format(self.runtime.get())
        messagebox.showinfo("Logs", logs)


def main():
    root = tk.Tk()
    app = TemperatureRegulationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
