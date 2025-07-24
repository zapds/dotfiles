import os
import random
import subprocess
import json
import re
import sys


pic = None
if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        pic = sys.argv[1]

wallpaper_dir = "/home/zapdos/Wallpapers"
if not pic:
    pics = os.listdir(wallpaper_dir)
    pic = random.choice(pics)
print(f"Chose wallpaper {pic}")

pic_path = os.path.join(wallpaper_dir, pic)
subprocess.call(["wal", "-i", pic_path])
subprocess.call(
    ["swww", "img", "--transition-duration", "1", "--transition-step", "10", pic_path]
)
subprocess.call(["pywalfox", "update"])
subprocess.call(["fish", "/home/zapdos/.cache/wal/colors.fish"])
subprocess.call(
    [
        "cp",
        "/home/zapdos/.cache/wal/colors-waybar.css",
        "/home/zapdos/.config/waybar/color.css",
    ]
)
subprocess.call(
    [
        "cp",
        "/home/zapdos/.cache/wal/colors-waybar.css",
        "/home/zapdos/.config/wlogout/colors.css",
    ]
)
subprocess.call(["pkill", "waybar"])
subprocess.call(["hyprctl", "dispatch", "exec", "waybar"])

conf_path = "/home/zapdos/.config/hypr/hyprlock.conf"
with open(conf_path, "r") as file:
    content = file.read()

# Replace the line that starts with 'path ='
# This regex captures any indentation before 'path =', then replaces the full line
content = re.sub(
    r"^(?P<indent>\s*)path\s*=\s*.*$",
    rf"\g<indent>path = {pic_path}",
    content,
    flags=re.MULTILINE,
)

# Write the updated content back to the file
with open(conf_path, "w") as file:
    file.write(content)

# Load pywal colors
with open("/home/zapdos/.cache/wal/colors.json") as f:
    colors = json.load(f)["colors"]

# Read the starship config file
with open("/home/zapdos/.config/starship.toml", "r") as f:
    config = f.read()

for name, hex_value in colors.items():
    # Match lines like: color0 = "#ffffff"
    pattern = rf'({re.escape(name)}\s*=\s*)"(#.*?)"'
    config = re.sub(pattern, rf'\1"{hex_value}"', config)

with open("/home/zapdos/.config/starship.toml", "w") as f:
    f.write(config)
