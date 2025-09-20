
---

# Photo Editing Framework with Python

Welcome to the **Photo Editing Framework**, an end-to-end solution for enhancing and transforming your images using Python. This framework leverages the powerful **Pillow (PIL)** library to provide a range of editing functionalities, allowing you to effortlessly enhance and modify your photo collection.

## Features

* **Sharpening & Black & White Conversion:**
  Applies sharpening effects and converts images to grayscale using the `'L'` mode. Includes optional rotation for creative adjustments.

* **Contrast Enhancement:**
  Adjust the contrast of your images with customizable factors. The example script uses a factor of `1.5` for a vibrant, dynamic look.

* **Extendable & Customizable:**
  Designed to be easily extendable. Explore and add additional edits using Pillow’s rich functionality. Full documentation: [Pillow Documentation](https://pillow.readthedocs.io/en/stable/).

## Usage

1. **Prepare Images:**
   Place your unedited images in the input folder:

   ```
   /home/your_name/Pictures/Images
   ```

2. **Run the Script:**
   Execute the Python script to process all images in the input folder, applying the defined edits:

   ```bash
   python photo_editor.py
   ```

3. **Output:**
   Enhanced images will be saved in the output folder:

   ```
   /home/your_name/Pictures/EditedImages
   ```

   Original filenames are retained with the `_edited` suffix.


1. **Prepare Images:**
   Place your unedited images in the `imgs` folder.

2. **Run the Script:**
   Execute the Python script to process all images in the input folder, applying the defined edits.

3. **Output:**
   Enhanced images will be saved in the `editedImgs` folder, keeping original filenames with the `_edited` suffix.

## Getting Started

Follow these steps to set up and run the framework:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Image-Editor.git
   cd photo-editing-framework
   ```

2. **Install dependencies:**

   ```bash
   pip install pillow
   ```

3. **Run the script:**

   ```bash
   python photo_editor.py
   ```

4. **Customize:**
   Modify the script to add more edits or adjust parameters based on your creative needs.

## License

MIT License © \ Vasilis Kokotakis

---


