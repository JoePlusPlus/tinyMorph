import tensorflow as tf
import numpy as np
import os

def load_img(path_to_img, target_size = 512, crop=False):
    max_dim = target_size
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    if crop:
        shape = tf.cast(tf.shape(img)[:-1], tf.float32)
        long_dim = min(shape[:2])
        scale = max_dim / long_dim

        new_shape = tf.cast(shape * scale, tf.int32)

        img = tf.image.resize(img, new_shape)
        img = img[tf.newaxis, :]

        height = img.shape[0]
        width = img.shape[1]
        h_off = np.max([height//2 - max_dim//2, 0])
        w_off = np.max([width//2 - max_dim//2, 0])
        img = tf.image.crop_to_bounding_box(img, h_off, w_off, max_dim, max_dim)

    else:
        shape = tf.cast(tf.shape(img)[:-1], tf.float32)
        long_dim = max(shape)
        scale = max_dim / long_dim

        new_shape = tf.cast(shape * scale, tf.int32)

        img = tf.image.resize(img, new_shape)
        img = img[tf.newaxis, :]
    return img

def main():
    files = os.listdir('data/input_img')
    for i, f in enumerate(files):
        size = 256
        in_path = os.path.join('data/input_img', f)
        out_img = load_img(in_path, size, True).numpy()[0]
        out_path = os.path.join('data/output_img', f)
        tf.keras.utils.save_img(out_path, out_img)
        print(f'Resized image number {i + 1} out of {len(files)}')

if __name__ == '__main__':
    main()
