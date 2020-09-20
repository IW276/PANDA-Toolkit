import os
import argparse
from ResultMerge import DetResMerge


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Merge results created on crops.')
    parser.add_argument('--result_path', type=str, required=True,
                        help='Path to result file in COCO result format.')
    parser.add_argument('--split_anno_path', type=str, required=True,
                        help='Path to annotation file of splitted dataset.')
    parser.add_argument('--person_anno_path', type=str, required=True,
                        help='Path to person annotation file of original dataset.')
    parser.add_argument('--output_result_path', type=str, required=True,
                        help='Path to write merged result file.', default='person')
    args = parser.parse_args()

merge = DetResMerge(args.result_path, args.split_anno_path, args.person_anno_path,
                    args.output_result_path)
merge.mergeResults()

