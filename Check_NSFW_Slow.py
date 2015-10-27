from PIL import Image

THRESHOLD = 0.5

def main():
        im=Image.open('Input_Image.jpg')
        ycbcr_image = Image.new('RGB', im.size, 'black')
        ycbcr=convert_to_ycbcr(im)
        #function accept image pixel tuple
        def detect(sample):
                y, cb, cr = sample
                return 80 <= cb <= 120 and 133 <= cr <= 173

        output = map(detect, ycbcr)
        print "Total Number of Pixel Checked " + str(len(output))
        rating = float(output.count(True)) / len(output)
        print rating > THRESHOLD
        print "NSFW Rating Percentage : "+str(rating*100)+" %" 

#function to Convert rgb image to ycbcr 
def convert_to_ycbcr(im):
        dummy=[]
        x = im.size[0]
        y = im.size[1]
        for i in range(x):
                for j in range(y):
                        r, g, b = im.getpixel((i,j))
                        dummy.append(  (
            16 + (65.738 * r + 129.057 * g + 25.064 * b) / 256,
            128 + (-37.945 * r - 74.494 * g + 112.439 * b) / 256,
            128 + (112.439 * r - 94.154 * g - 18.285 * b) / 256
            ))
        
        return dummy


if __name__=='__main__':
        main()
