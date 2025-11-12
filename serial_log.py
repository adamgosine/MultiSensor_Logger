import serial, csv, matplotlib.pyplot as plt, time
from datetime import datetime

PORT = "COM3"          # adjust if needed
BAUD = 115200
DURATION = 30          # seconds to log

# Timestamped filename
filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

ser = serial.Serial(PORT, BAUD, timeout=1)
print(f"Logging to {filename} ...")

# Wait for header
while True:
    line = ser.readline().decode(errors="ignore").strip()
    if line.startswith("millis,"):
        header = line.split(',')
        break

# Prepare writer
with open(filename, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    i_ldr = header.index("ldr_ema")
    i_mic = header.index("mic_ema")
    i_joyx = header.index("joyx_ema")
    i_joyy = header.index("joyy_ema")

    xs, ldr, mic, joyx, joyy = [], [], [], [], []
    plt.ion()
    fig, ax = plt.subplots()

    start = time.time()
    while (time.time() - start) < DURATION:
        line = ser.readline().decode(errors="ignore").strip()
        if not line or line.startswith("millis,"): continue
        parts = line.split(',')
        if len(parts) != len(header): continue

        w.writerow(parts)
        xs.append(len(xs))
        ldr.append(float(parts[i_ldr]))
        mic.append(float(parts[i_mic]))
        joyx.append(float(parts[i_joyx]))
        joyy.append(float(parts[i_joyy]))

        ax.clear()
        ax.plot(xs, ldr, label="LDR")
        ax.plot(xs, mic, label="Mic")
        ax.plot(xs, joyx, label="Joy X")
        ax.plot(xs, joyy, label="Joy Y")
        ax.legend()
        ax.set_title(f"Live Sensor Logger – {int(time.time() - start)} s")
        plt.pause(0.01)

ser.close()
print("Logging complete.")
