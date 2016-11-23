# Task [№12](https://devman.org/challenges/12/) from [devman](https://devman.org)
## Requirements
```
Python 3.5.2+
pillow
```
## Setup
```    
git clone https://github.com/ram0973/12_image_resize.git
cd 12_image_resize
pip3 install -r requirements.txt
```
## Description
The user enters the required argument - the path to the original image and
four optional. The script resizes the images and saves as
specified in the task. It works at least with jpg, png, tif, bmp, tga.
Saves to gif, but can't handle the resulting gif.
## Usage
``` 
python3 image_resize.py --i image_path 
```
Example of optional parameters:
``` 
python3 image_resize.py --i original_image.jpg --w 200 --h 100 --s 0.5 --o image_scaled.jpg
```
## License
[MIT](http://opensource.org/licenses/MIT)