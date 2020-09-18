import os
import argparse
from ImgSplit import ImgSplit
from panda_utils import generate_coco_anno_only_person_2


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate Split Data.')
    parser.add_argument('--image_root', type=str, help='Path to input folder with images.')
    parser.add_argument('--person_anno_file', type=str, help='Name of annotation file.')
    parser.add_argument('--outpath', type=str, help='Path to store output dataset.')
    parser.add_argument('--annomode', type=str, help='Annotation mode.', nargs='?', default='person')
    parser.add_argument('--outannofile', type=str, help='Name of output annotation file.',
                        nargs='?', default='train.json')
    parser.add_argument('--scale', type=int, help='Resize rate before cut.', nargs='?', default=0.25)
    parser.add_argument('--subwidth', type=int, help='Resize width.', nargs='?', default=1920)
    parser.add_argument('--subheight', type=int, help='Resize height.', nargs='?', default=1080)
    parser.add_argument('--image_subdir', type=str, help='Subfolder for output images.',
                        nargs='?', default='image_train')
    parser.add_argument('--annotype', type=str, help='Type of annotation.', nargs='?', default='train')
    args = parser.parse_args()


if args.annotype == 'train':
    split = ImgSplit(args.image_root, args.person_anno_file, args.annomode, args.outpath,
                     args.outannofile, image_subdir=args.image_subdir)
    split.splitdata(args.scale)
    generate_coco_anno_only_person_2(os.path.join(args.outpath, 'image_annos', args.outannofile),
                                     os.path.join(args.outpath, 'image_annos', 'train_coco.json'))
elif args.annotype == 'valid':
    if args.outannofile == 'train.json':
        args.outannofile = 'valid.json'
    if args.image_subdir == 'image_train':
        args.image_subdir = 'image_valid'
    split = ImgSplit(args.image_root, args.person_anno_file, args.annomode, args.outpath,
                     args.outannofile, image_subdir=args.image_subdir)
    split.splitdata(args.scale)
    generate_coco_anno_only_person_2(os.path.join(args.outpath, 'image_annos', args.outannofile),
                                     os.path.join(args.outpath, 'image_annos', 'valid_coco.json'))
else:
    print('\nType of annotation must be train or valid')
