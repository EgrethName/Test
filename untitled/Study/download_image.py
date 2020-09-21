import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('device_type', type=str)
parser.add_argument('version', type=str)
parser.add_argument('path_to_save', type=str)
args = parser.parse_args()

if args.device_type == "ReachRS":

