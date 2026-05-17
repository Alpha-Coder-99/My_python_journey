# 🚀  System Health Monitor 
import psutil
import tkinter as tk
from tkinter import ttk
from plyer import notification


class SystemHealthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("💻 Advanced System Health Monitor")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#0a0a2a")

        # Notification Spam Fix
        self.alert_sent = False

        # ================= TITLE =================
        title = tk.Label(
            self.root,
            text="⚡ Advanced System Health Monitor ⚡",
            font=("Poppins", 22, "bold"),
            fg="#00FFCC",
            bg="#0a0a2a"
        )
        title.pack(pady=20)

        # ================= CPU =================
        self.cpu_label = tk.Label(
            self.root,
            text="CPU Usage: 0%",
            font=("Poppins", 14, "bold"),
            fg="white",
            bg="#0a0a2a"
        )
        self.cpu_label.pack(pady=5)

        self.cpu_bar = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.cpu_bar.pack(pady=5)

        # ================= RAM =================
        self.ram_label = tk.Label(
            self.root,
            text="RAM Usage: 0%",
            font=("Poppins", 14, "bold"),
            fg="white",
            bg="#0a0a2a"
        )
        self.ram_label.pack(pady=5)

        self.ram_bar = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.ram_bar.pack(pady=5)

        # ================= BATTERY =================
        self.battery_label = tk.Label(
            self.root,
            text="Battery: Fetching...",
            font=("Poppins", 14, "bold"),
            fg="white",
            bg="#0a0a2a"
        )
        self.battery_label.pack(pady=10)

        # ================= DISK =================
        self.disk_label = tk.Label(
            self.root,
            text="Disk Usage: Fetching...",
            font=("Poppins", 14, "bold"),
            fg="white",
            bg="#0a0a2a"
        )
        self.disk_label.pack(pady=10)

        # ================= TOP PROCESSES =================
        process_title = tk.Label(
            self.root,
            text="🔥 Running Processes",
            font=("Poppins", 16, "bold"),
            fg="#00FFCC",
            bg="#0a0a2a"
        )
        process_title.pack(pady=10)

        self.process_box = tk.Listbox(
            self.root,
            width=70,
            height=10,
            bg="#111133",
            fg="white",
            font=("Consolas", 10)
        )
        self.process_box.pack(pady=10)

        # ================= REFRESH BUTTON =================
        refresh_btn = tk.Button(
            self.root,
            text="🔄 Refresh Now",
            font=("Poppins", 12, "bold"),
            bg="#00FFCC",
            fg="black",
            activebackground="#00ccaa",
            command=self.update_stats
        )
        refresh_btn.pack(pady=10)

        # Start updating
        self.update_stats()

    # ====================================================
    # COLOR CHANGER FUNCTION
    # ====================================================
    def usage_color(self, value):
        if value < 50:
            return "lightgreen"
        elif value < 80:
            return "yellow"
        else:
            return "red"

    # ====================================================
    # MAIN UPDATE FUNCTION
    # ====================================================
    def update_stats(self):

        # ================= CPU =================
        cpu = psutil.cpu_percent()

        self.cpu_label.config(
            text=f"⚙️ CPU Usage: {cpu}%",
            fg=self.usage_color(cpu)
        )

        self.cpu_bar["value"] = cpu

        # ================= RAM =================
        ram = psutil.virtual_memory().percent

        self.ram_label.config(
            text=f"🧠 RAM Usage: {ram}%",
            fg=self.usage_color(ram)
        )

        self.ram_bar["value"] = ram

        # ================= BATTERY =================
        battery = psutil.sensors_battery()

        if battery:
            plugged = "⚡ Charging" if battery.power_plugged else "🔋 Discharging"

            self.battery_label.config(
                text=f"🔋 Battery: {battery.percent}% | {plugged}",
                fg=self.usage_color(100 - battery.percent)
            )

        else:
            self.battery_label.config(
                text="No Battery Detected",
                fg="orange"
            )

        # ================= DISK =================
        disk = psutil.disk_usage('/').percent

        self.disk_label.config(
            text=f"💾 Disk Usage: {disk}%",
            fg=self.usage_color(disk)
        )

        # ================= RUNNING PROCESSES =================
        self.process_box.delete(0, tk.END)

        count = 0

        for process in psutil.process_iter(['name']):
            try:
                process_name = process.info['name']

                if process_name:
                    self.process_box.insert(tk.END, process_name)
                    count += 1

                if count >= 10:
                    break

            except:
                pass

        # ================= NOTIFICATIONS =================
        if (cpu > 80 or ram > 80) and not self.alert_sent:

            notification.notify(
                title="⚠️ System Warning!",
                message=f"High Usage Detected!\nCPU: {cpu}%\nRAM: {ram}%",
                timeout=5
            )

            self.alert_sent = True

        elif cpu < 70 and ram < 70:
            self.alert_sent = False

        # ================= AUTO UPDATE =================
        self.root.after(2000, self.update_stats)


# ====================================================
# MAIN APP
# ====================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = SystemHealthChecker(root)
    root.mainloop()

