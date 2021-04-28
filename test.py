import glob, os
import numpy as np
from PIL import Image

def extract_features(parent_directory, sub_directory, file_ext="*.ogg", bands = 128, frames = 128):
    window_size = 512 * 127
    log_specgrams = []
    labels = []
    ITJ = 0
    for l, sub_directory in enumerate(sub_directory):
        PTJ = 1
        for fn in glob.glob(os.path.join(parent_directory, sub_directory, file_ext)):
            sound_clip, s = librosa.load(fn)
            label = ITJ
            for (start, end) in windows(sound_clip, window_size):
                if(len(sound_clip[start:end]) == window_size):
                    signal = sound_clip[start:end]
                    melspec = librosa.feature.melspectogram(signal, n_mels = bands)
                    logspec = librosa.logamplitude(melspec)
                    logspec = logspecc.T.flatten()[:, np.newaxis].T
                    log_specgrams.append(logspec)
                    labels.append(label)
            print(PTJ*ITJ*270, ITJ)
            PTJ = PTJ + 1
        ITJ = ITJ + 1
    log_specgrams = np.array(log_specgrams)
    print(log_specgrams.shape)
    log_specgrams = np.asarray(log_specgrams).reshape(len(log_specgrams), bands, frames)
    features = log_specgrams
    return np.array(features)

data = extract_features("train_short_audio", "acafly")
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()