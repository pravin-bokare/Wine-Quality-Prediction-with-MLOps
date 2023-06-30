import os
import argparse

import pandas as pd
import yaml
import logging
from from_root import from_root


def read_params(config_path):
    config_path = os.path.join(from_root(), config_path)
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config_path = os.path.join(from_root(), config_path)
    config = read_params(config_path)
    #print(config)
    data_path = os.path.join(from_root(), config['data_source']['s3_source'])
    df = pd.read_csv(data_path, sep=',', encoding='utf-8')
    return df


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join(from_root(), "params.yaml")
    args.add_argument("--config", default=default_config_path)

    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)