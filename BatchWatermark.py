from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageEnhance
import os
class WatermarkGUI:
    def __init__(self, master):
        self.master = master
        master.title("Batch Watermark GUI")
        self.watermark_image = None
        self.transparency = 50
        self.images = []
        self.watermarked_images = []
        self.directory_label = Label(master, text="Directory:")
        self.directory_label.pack(side=TOP)
        self.directory_button = Button(master, text="Select Directory", command=self.select_directory)
        self.directory_button.pack(side=TOP)
        self.watermark_image_label = Label(master, text="Watermark Image:")
        self.watermark_image_label.pack(side=TOP)
        self.watermark_image_button = Button(master, text="Select Image", command=self.select_watermark_image)
        self.watermark_image_button.pack(side=TOP)
        self.transparency_label = Label(master, text="Transparency:")
        self.transparency_label.pack(side=TOP)
        self.transparency_scale = Scale(master, from_=0, to=255, orient=HORIZONTAL, command=self.set_transparency)
        self.transparency_scale.pack(side=TOP)
        self.add_watermark_button = Button(master, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_button.pack(side=TOP)
        self.save_images_button = Button(master, text="Save Images", command=self.save_images)
        self.save_images_button.pack(side=TOP)
    def select_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.images = [os.path.join(directory_path, file_name) for file_name in os.listdir(directory_path) if file_name.endswith((".jpg", ".jpeg", ".png"))]
    def select_watermark_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.watermark_image = Image.open(file_path)
    def set_transparency(self, value):
        self.transparency = int(value)
    def add_watermark(self):
        if self.watermark_image and self.images:
            self.watermarked_images = [(image_path, self.watermark_image_on_original(image_path)) for image_path in self.images]
    def watermark_image_on_original(self, image_path):
        original_image = Image.open(image_path)
        watermark_resized = self.watermark_image.resize(original_image.size)
        watermark_with_transparency = watermark_resized.copy().convert("RGBA")
        alpha = watermark_with_transparency.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(self.transparency/255)
        watermark_with_transparency.putalpha(alpha)
        watermarked_image = original_image.copy()
        watermarked_image.paste(watermark_with_transparency, (0, 0), watermark_with_transparency)
        return watermarked_image
    def save_images(self):
        if self.watermarked_images:
            destination_folder = filedialog.askdirectory()
            if destination_folder:
                for image_path, watermarked_image in self.watermarked_images:
                    file_name = os.path.basename(image_path)
                    save_path = os.path.join(destination_folder, "watermarked_" + file_name)
                    watermarked_image.save(save_path)
root = Tk()
my_gui = WatermarkGUI(root)
root.mainloop()