import subprocess
import sys

# Compile the GUI script to executable
subprocess.call(['pyinstaller', '--onefile', 'gui.py'])

# Move the executable to the current directory
subprocess.call(['mv', 'dist/gui', 'YTDownloader'])

# Clean up the temporary files
subprocess.call(['rm', '-rf', 'build'])
subprocess.call(['rm', '-rf', 'dist'])
subprocess.call(['rm', 'gui.spec'])

print("Injector script completed successfully.")
