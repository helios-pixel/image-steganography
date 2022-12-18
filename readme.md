# Image Steganography Using LSB method

LSB-Steganography is a steganography technique in which we hide messages inside an image by replacing Least significant bit of image with the bits of message to be hidden. By modifying only the first most right bit of an image we can insert our secret message and it also make the picture unnoticeable, but if our message is too large it will start modifying the second right most bit and so on. Image Steganography is mostly implemented in data transfer encryptions.


# How to run the program

1. Make sure you have all the required modules installed along with python 3.8+. All the modules are listed in "requirements.txt" file in the repo simply navigate to the directory on your local machine through command line and run the following command.

							`pip install -r requirements.txt`

2. On successful installation of the modules, run the python file "app.py" which will open up the following GUI window.
![Application GUI](https://i.imgur.com/YIhLpdx.png) 
3. Click on "Open Image" option to select an image to be processed (.png files only).
4. Navigate and select the desired image through the windows explorer dialog box
5. On selecting the image will appear in the black box of the application GUI.

![Image selected GUI](https://i.imgur.com/YTtDHKf.png)

6. Enter message to be embedded in the image in the right hand side textbox of the application gui and press "Hide Data"
7. To save the image press "Save Image", this will save the stego image (image embedded with message) in the program folder as "Stegano_image.png"
8. This image can be shared through a non pixelating channel to maintain its bits and can be decoded using the same application.
9. Use the "Show Data" button to decode the embedded text.
 
