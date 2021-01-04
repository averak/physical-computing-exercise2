#!/usr/bin/env python
import argparse
import logging

import nnet

from key.repository import KeyRepository
from key.event_viewer import EventViewer
from key import DEFAULT_DIM


# オプション引数
parser = argparse.ArgumentParser()
parser.add_argument('--record', help='create dataset',
                    action='store_true')
parser.add_argument('--train', help='execute training',
                    action='store_true')
parser.add_argument('--infer', help='infer the entered chars',
                    action='store_true')
parser.add_argument('--dim', help='key vector dim', type=int)
args = parser.parse_args()

# ロギング
formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(level=logging.DEBUG, format=formatter)

key_repository = KeyRepository()
key_event_viewer = EventViewer()

dim = args.dim or DEFAULT_DIM
tags = key_repository.tags
n_class = len(tags)

# データセットを作成
if args.record:
    print()
    tag = input('char: ')

    while True:
        try:
            logging.info('Please enter <%s> char!' % tag)
            vector = key_event_viewer.record()
            key_repository.store(vector, tag)
            logging.info('recorded')

        except KeyboardInterrupt:
            break

# トレーニング
if args.train:
    x = []
    y = []

    for label, tag in enumerate(tags):
        for vector in key_repository.find(tag):

            vector.preprocessing()
            vector.dim = dim

            x.append(vector.vector)
            y.append(label)

    logging.info('found %d classes, start training with %d data'
                 % (n_class, len(x)))

    model = nnet.Model(
        vec_dim=dim,
        n_class=n_class,
        model_file='model.h5',
    )
    model.train(x, y, save_weights=True)

# 推論
if args.infer:
    model = nnet.Model(
        vec_dim=dim,
        n_class=n_class,
        load_weights=True,
        model_file='model.h5',
    )

    while True:
        try:
            logging.info('Please enter some char...')
            vector = key_event_viewer.record()
            vector.preprocessing()
            vector.dim = dim
            label = model.predict(vector.vector)
            logging.info('You entered <%s>, right?' % tags[label])

        except KeyboardInterrupt:
            break

exit(0)
