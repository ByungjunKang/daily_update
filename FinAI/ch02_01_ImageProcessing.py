import requests
from PIL import Image

url = 'https://moneycoding.kr/wp-content/uploads/2023/01/home-1.png'
r = requests.get(url, stream=True).raw

img = Image.open(r)
#img.show()
#img.save('src.png')

#print(img.get_format_mimetype)

BUF_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)

import hashlib

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())

#print('src.png\'s hash : {}'.format(sha_src.hexdigest()))
#print('dst.png\'s hash : {}'.format(sha_dst.hexdigest()))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122)
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img[:,:,0]
plt.imshow(pseudo_img)
plt.show()
