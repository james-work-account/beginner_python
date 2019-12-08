# Python Projects for beginners
# https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs

import matplotlib.ticker as tck
import matplotlib.pyplot as plot
import numpy as np

print(""" \\ \\        / / | |                          | |
  \\ \\  /\\  / /__| | ___ ___  _ __ ___   ___  | |
   \\ \\/  \\/ / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | |
    \\  /\\  /  __/ | (_| (_) | | | | | |  __/ |_|
     \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___| (_)
                                                
                                                """)
print("Sine / Cosine graph generator")


time = np.arange(0, 2 * np.pi, 0.1)
amplitude_sin = np.sin(time)
amplitude_cos = np.cos(time)

plot.suptitle("Graphs!")

line_sin, = plot.plot(time, amplitude_sin, 'tab:blue', label="sine")
line_cos, = plot.plot(time, amplitude_cos, 'tab:orange', label="cosine")

plot.legend(handles=[line_sin, line_cos])
plot.xlabel("degrees (radians)")
plot.ylabel("value")
plot.xticks(np.arange(min(time), max(time)+1, np.pi))
ax = plot.gca()
ax.grid(True)
ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)
ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
ax.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))


plot.show()
