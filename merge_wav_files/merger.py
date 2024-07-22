import soundfile as sf
import numpy as np
import os

def read_wave_file(file_path):
    data, samplerate = sf.read(file_path)
    return data, samplerate

def write_wave_file(file_path, data, samplerate):
    sf.write(file_path, data, samplerate)

def merge_audio_files(input_directory, output_file):
    audio_files = [f for f in os.listdir(input_directory) if f.endswith('.wav')]
    audio_files.sort() 

    combined_frames = []
    samplerate = None

    for file_name in audio_files:
        file_path = os.path.join(input_directory, file_name)
        data, current_samplerate = read_wave_file(file_path)
        if samplerate is None:
            samplerate = current_samplerate
        elif samplerate != current_samplerate:
            raise ValueError("All WAV files must have the same sample rate.")
        
        combined_frames.append(data)

    combined_frames = np.concatenate(combined_frames)
    write_wave_file(output_file, combined_frames, samplerate)
    print(f'Merged {len(audio_files)} files into {output_file}')

if __name__ == '__main__':
    input_directory = 'path_to_your_wav_files_directory' 
    output_file = 'merged_audio.wav'
    merge_audio_files(input_directory, output_file)
