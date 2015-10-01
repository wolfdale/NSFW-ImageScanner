from PIL import Image

THRESHOLD = 0.5

def main():
        im=Image.open('abc.jpg')
        #ycbcr_image = Image.new('RGB', im.size, 'black')
        ycbcr=convert_to_ycbcr(im)
        '''
        pix=ycbcr_image.load()
        for i in range(0, im.size[0]):
                for j in range(0, im.size[1]):
                    pix[i, j] = tuple(map(int, ycbcr[i * im.size[1] + j]))
        
        ycbcr_image.save('nin.jpg')
        '''
        def judge(sample):
                y, cb, cr = sample
                return 80 <= cb <= 120 and 133 <= cr <= 173

        judged = map(judge, ycbcr)
        print judged.count(True)
        print judged.count(False)
        print len(judged)
        rating = float(judged.count(True)) / len(judged)
        print rating > THRESHOLD, rating*100

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
