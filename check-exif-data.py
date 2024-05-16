import sys
import os
import platform

try:
    from PIL import Image
except ModuleNotFoundError:
    print("Pillow is required to run this script.")

    print()
    
    operational_system = platform.system()

    if (operational_system == "Linux"):
        if ("arch" in platform.platform()):
            os.system("sudo pacman -Syu python-pillow --noconfirm --ask=4")
        elif ("Ubuntu" in platform.version()):
            os.system("sudo apt install python3-pillow -y")
        print()
        input("Press Enter to exit...")
        sys.exit()
    elif (operational_system == "Windows"):
        os.system("pip install pillow")
        print()
        input("Press Enter to exit...")
        sys.exit()

def print_exif_data(image_path):
    try:
        img = Image.open(image_path)

        # Get EXIF data
        exif_data = img.getexif()

        # Print EXIF data
        if exif_data:
            print(f"EXIF Data for {os.path.basename(image_path)}:")
            for tag, value in exif_data.items():
                print(f"Tag: {tag}, Value: {value}")
        else:
            print(f"No EXIF data found for {os.path.basename(image_path)}.")

        print()
    except Exception as e:
        print("Error:", e)

if len(sys.argv) < 2:
    print("Usage: python script.py <image_path1> [<image_path2> ...]")
    sys.exit(1)

for image_path in sys.argv[1:]:
    print_exif_data(image_path)

input("Press Enter to exit...")