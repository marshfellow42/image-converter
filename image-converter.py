from tqdm import tqdm
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

print("""1) JPG
2) PNG
3) TIFF
4) AVIF""")
filetype = int(input("What file type do you want to convert to? "))

file_extension = ""
file_save = ""

match filetype:
    case 1:
        file_extension = ".jpeg"
        file_save = "JPEG"
    case 2:
        file_extension = ".png"
        file_save = "PNG"
    case 3:
        file_extension = ".tiff"
        file_save = "TIFF"
    case 4:
        file_extension = ".avif"
        file_save = "AVIF"


if len(sys.argv) < 2:
    print("Usage: python script.py <image_path1> <image_path2> ...")
    sys.exit(1)

image_paths = sys.argv[1:]

try:
    for image_path in image_paths:
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        output_dir = os.path.join(os.path.dirname(image_path), "converted_images")
        os.makedirs(output_dir, exist_ok=True)

        img = Image.open(image_path)

         # Convert and save image
        save_dir = os.path.join(output_dir, file_save)
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, f"{image_name}{file_extension}")
        
        with tqdm(desc="Converting", total=100) as pbar:
            if (file_extension == ".jpeg"):
                img = img.convert("RGB")
            img.save(save_path, file_save, progress_callback=lambda i, n: pbar.update(100/n))
        
        print("Image saved as:", save_path)
        print()
except Exception as e:
    print("Error:", e)

input("Press Enter to exit...")