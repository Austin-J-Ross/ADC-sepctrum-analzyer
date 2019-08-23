import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import h5py
import pickle
# ctrl+shift+i for information


class AnalogToDigital:
    def __init__(self):
        self.data = ""


class SignalSampler:
    def __init__(self):
        self.signal = []
        self.sin_param = {"amp": 1, "freq": 1, "phi": 1}

    def generate(self, sample_freq: float, number_of_samples: int, signal_type="simple"):
        """
        generates a list of samples from a signal
        :param sample_freq:
        :param number_of_samples:
        :param signal_type:
        :return:
        """
        if signal_type == "simple":
            self.signal = np.array(
                [self.simple_sin((i/sample_freq)) for i in range(number_of_samples)]
            )
        return self.signal

    def simple_sin(self, time):
        amplitude = self.sin_param["amp"]
        frequency = self.sin_param["freq"]
        phi = self.sin_param["phi"]
        return amplitude*np.sin(time*(2*np.pi*frequency) + phi)


if __name__ == "__main__":
    df = pd.DataFrame()
    signal = SignalSampler()

    print(signal.generate(800, 100))

    df["test1"] = signal.generate(30, 100)
    df["test2"] = signal.generate(100, 100)



    x = [i for i in range(100)]
    path = "./output.csv"
    df.to_clipboard()

    plt.plot(x, df["test1"], "x")
    plt.show()



