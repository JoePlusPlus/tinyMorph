# Welcome to TinyMorph! 

TinyMorph is a little project about image processing using GAN's
and other fancy architectures. We will provide a simple base model to be tinkered with
and will ultimately include a "research report" on all the variations we tested
during the process. There might be a front-end to play with images.

We will be using tensorflows pretrained models (like VGG-19) and make use
of ImageNet for data of different sizes & categories.

After that, we will move on to more experimental configs which have yet to be
specified.

---> User-Input: potentially use pix2pix + cycleGAN to turn drawings into images

    https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
    
    AS A FIRST MILESTONE

---> make use of several pretrained models: 

    https://huggingface.co/models
 
# Workflow

 1. get a generic pipeline going, using a pretrained VGG-19 (tensorflow)
    
    --> EXAMPLES: 
    
    https://towardsdatascience.com/generate-novel-artistic-artworks-with-deep-learning-f2f61da69e6e

    ( How to quickly implement a pretrained VGG-19 ) 

    https://www.tensorflow.org/tutorials/generative/cyclegan

    ( How to set up a generative network )

    https://www.tensorflow.org/tutorials/generative/style_transfer#build_the_model 

    ( How to set up a basic model )
