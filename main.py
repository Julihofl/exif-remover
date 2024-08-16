import os

from PIL import Image
from typing import List
from tkinter import filedialog

def remove_exif(input_path: str, output_path: str) -> None:
    input_image: Image = Image.open(input_path)
    
    output_image: Image = Image.new(input_image.mode, input_image.size)
    output_image.putdata(list(input_image.getdata()))
    
    output_image.save(output_path)
    print(f"Removed EXIF-Data: {output_path}")

def get_output_path(input_path: str) -> str:
    base, ext = os.path.splitext(input_path)
    return f"{base}_2{ext}"

def main() -> None:
    images_paths: List[str] = filedialog.askopenfilenames(
        title='Select images to remove EXIF data',
        filetypes=[("Bilddateien", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),
               ("PNG Dateien", "*.png"),
               ("JPEG Dateien", "*.jpg;*.jpeg"),
               ("BMP Dateien", "*.bmp"),
               ("GIF Dateien", "*.gif")]
        )

    for path in images_paths:
        remove_exif(path, get_output_path(path))

if __name__ == "__main__":
    main()
