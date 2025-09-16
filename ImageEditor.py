from PIL import Image, ImageEnhance, ImageFilter
import os

path = "/home/yourName/Pictures/Images"           # folder for unedited images
pathOut = "/home/yourName/Pictures/EditedImages"  # folder for edited images

os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    file_path = os.path.join(path, filename)

    try:
        img = Image.open(file_path)

        # sharpening, BW
        edit = img.filter(ImageFilter.SHARPEN).convert('L')

        # contrast
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # save
        clean_name = os.path.splitext(filename)[0]
        out_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")
        edit.save(out_path)
        print(f"Saved {out_path}")

    except Exception as e:
        print(f"Skipping {filename}: {e}")
