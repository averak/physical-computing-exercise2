import numpy as np
import datetime
import glob

DATA_DIR = 'data'
VEC_SIZE = 30


class KeyVector:
    def __init__(self, length):
        self._length = length
        self._vector = []

        self.reset()

    def reset(self):
        self._vector = [0] * self.length

    @property
    def length(self):
        return self._length

    @property
    def vector(self):
        return self._vector


def extract_class_name(file_name):
    return file_name.split('/')[-2]


def extract_classes():
    result = []
    for file in glob.glob(DATA_DIR + '/*/*.npy'):
        class_name = extract_class_name(file)

        if class_name not in result:
            result.append(class_name)

    return result


def load_vectors():
    result = []

    files = glob.glob(DATA_DIR + '/*/*.npy')
    for file in files:
        result.append(np.load(file))

    return result


def save_vector(class_name, np_vector):
    # FIXME: ディレクトリが存在しない場合は作成する
    file = '%s/%s/%s' % (
        DATA_DIR,
        class_name,
        datetime.datetime.now().strftime('%Y%m%d:%H%M%S:%f.npy'),
    )

    np.save(file, np_vector)


def preprocessing(np_vectors):
    result = []

    for vec in np_vectors:
        # ベクトルを固定長に変換
        vec = vec[:VEC_SIZE]
        vec = np.append(vec, [0] * (VEC_SIZE - len(vec)))

        # 正規化
        vec = np.vectorize(lambda k: k / 226)(vec)

        result.append(vec)

    return result


# クラス一覧を取得
CLASSES = extract_classes()
