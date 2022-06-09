# Welcome to TinyMorph! 

Our project uses "generative networks" to turn sketches into images. 
Using pre-trained models (fastCUT & pix2pix - see below for refs)
we are able to convert user-generated portrait doodles or pre-computed
edge-sketches into something akin to photographs. The models
were specifically and narrowly trained on clean portraits.

# How to do it yourself

Clone this repo, install the requirements and simply run "run.py" in 
the root directory. 

This will launch a local page in your webbrowser
where you can upload example images or try to sketch your own faces
in our canvas.

Due to the size of the model, we only include fastCUT in this repo by default.
As of now we have to provide pix2pix ourselves or possibly as a download later.

# How the magic is done

Before any model could be trained, we had to pre-process the images. A photo was
turned into a sketch by using edge-detection-algorithms. In our case, we made
use of "canny-edge-detection" (ref below) to generate our own sketches.

The training was specialized on portraits. We took a slice from a 
Kaggle-database of 10.000 Flickr-faces (ref below).

We then lovingly trained two image-processing-networks to our
set of generated sketches (called fastCUT & pix2pix). Due to limited
hardware, we trained the models on 5000 and 500 images respectively.
To achieve anything close to SOTA, at least 200 epochs are required for
the used models. We managed around 80 for fastCUT and 150 for pix2pix.

Once training was done, the models could be integrated into our front-end
and generate novel images from new pre-computed sketches or user-made doodles.

# Repos and Databases

All training faces are provided by this Kaggle-Database:

https://www.kaggle.com/datasets/arnaud58/flickrfaceshq-dataset-ffhq

The following repos were "mission-critical":

fastCUT: https://github.com/taesungp/contrastive-unpaired-translation

pix2pix: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

Edge-Detection: https://github.com/FienSoP/canny_edge_detector

Photosketch: https://github.com/mtli/PhotoSketch
