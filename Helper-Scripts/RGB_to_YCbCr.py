from PIL import Image


def main():
        img = Image.open('Input_Image.jpg')
        ycbcr_image = Image.new('RGB', img.size, 'black')
        ycbcr = convert_to_ycbcr(img)
        pix = ycbcr_image.load()

        for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    pix[i, j] = tuple(map(int, ycbcr[i * img.size[1] + j]))

        ycbcr_image.save('Output_Image.jpg')
      

#function to Convert rgb image to ycbcr 
def convert_to_ycbcr(img):
        dummy=[]
        x = img.size[0]
        y = img.size[1]

        for i in range(x):
                for j in range(y):
                        r, g, b = img.getpixel((i,j))
                        dummy.append(  (
            16 + (65.738 * r + 129.057 * g + 25.064 * b) / 256,
            128 + (-37.945 * r - 74.494 * g + 112.439 * b) / 256,
            128 + (112.439 * r - 94.154 * g - 18.285 * b) / 256
            ))
        
        return dummy


if __name__=='__main__':
        print 'Processing...'
        main()
        print 'Done !'
