import os


class Model:
    def __init__(self, vec_dim=30, n_class=10, load_weights=False, model_file='nnet.h5'):
        self.__model_path = '%s/ckpt/%s' % (
            os.path.dirname(__file__), model_file)

        from .make import make_nnet

        self.__nnet = make_nnet((vec_dim,), n_class,
                                load_weights, self.model_path)

    def train(self, x, y, save_weights=False):
        from .compile import compile_nnet
        from .train import train_nnet

        self.__nnet = compile_nnet(self.__nnet)
        self.__nnet = train_nnet(
            self.__nnet, x, y, save_weights, self.model_path)

    def predict(self, x):
        from .predict import predict

        return predict(self.__nnet, x)

    @property
    def model_path(self):
        return self.__model_path
