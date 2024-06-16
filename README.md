# Batch Watermark GUI README

The Batch Watermark GUI is a Python-based graphical user interface (GUI) application designed for batch watermarking of images. Utilizing the `tkinter` library, this tool offers a straightforward method for applying watermarks to multiple images at once, with adjustable transparency levels for each watermark.

## Introduction

- **Purpose**: To facilitate the mass addition of watermarks to images, enhancing copyright protection and ownership claims.
- **Features**: Customizable watermark placement, transparency adjustment, and support for various image formats.

## Getting Started

### Prerequisites

- Python installed on your system.
- Install the `Pillow` library for image processing:
pip install pillow

- Install `tkinter ` library for the gui:
pip install tkinter



### Installation

1. Clone the repository:
git clone https://github.com/VincentNeemie/BatchWatermark.git

2. Navigate to the cloned directory.

### Running the Application

Execute the script:
python BatchWatermark.py


## Usage

Upon launching the application, you will interact with the following components:

- **Select Directory**: Choose the folder containing images to be watermarked.
- **Select Image**: Upload the watermark image.
- **Transparency**: Adjust the watermark's transparency level using the slider.
- **Add Watermark**: Apply the watermark to all selected images.
- **Save Images**: Specify a new directory to save the watermarked images.

## Contributing

Contributions to enhance the functionality or fix bugs are welcomed. Please create an issue on the GitHub repository for discussions or submit a pull request for code changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file in the repository for detailed terms.
