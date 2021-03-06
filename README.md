# [CVPRW 2021] CLIP-Art

[CLIP-Art: Contrastive Pre-Training for Fine-Grained Art Classification](https://openaccess.thecvf.com/content/CVPR2021W/CVFAD/html/Conde_CLIP-Art_Contrastive_Pre-Training_for_Fine-Grained_Art_Classification_CVPRW_2021_paper.html) paper for CVPR FGVC8 & CVFAD Workshops 2021.

### [Code](https://github.com/KeremTurgutlu/self_supervised)

**Reference repo: https://github.com/KeremTurgutlu/self_supervised (245 ⭐ stars) includes:**

Here are the list of implemented self_supervised.vision algorithms:
- SimCLR v1 & SimCLR v2
- MoCo v1 & MoCo v2
- SwAV, Barlow Twins
- DINO
- CLIP

For vision algorithms all models from timm and fastai can be used as encoders.
For multimodal training currently CLIP supports ViT-B/32 and ViT-L/14, following best architectures from the paper.


If you use our code or ideas do not forget to cite our work:

```
@InProceedings{Conde_2021_CVPR,
    author    = {Conde, Marcos V. and Turgutlu, Kerem},
    title     = {CLIP-Art: Contrastive Pre-Training for Fine-Grained Art Classification},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    month     = {June},
    year      = {2021},
    pages     = {3956-3960}
}
```

> Existing computer vision research in artwork struggles with artwork's fine-grained attributes recognition and lack of curated annotated datasets due to their costly creation. In this work, we use CLIP (Contrastive Language-Image Pre-Training) for training a neural network on a variety of art images and text pairs, being able to learn directly from raw descriptions about images, or if available, curated labels. Model's zero-shot capability allows predicting the most relevant natural language description for a given image, without directly optimizing for the task. Our approach aims to solve 2 challenges: instance retrieval and fine-grained artwork attribute recognition. We use the iMet Dataset, which we consider the largest annotated artwork dataset. 

<img src="https://i.ibb.co/pnHrz1d/poster.png" alt="poster" border="0">
