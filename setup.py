from setuptools import setup, find_packages

setup(
    name='merge_audio_files',
    version='0.1.0',
    description='A simple library for merging WAV audio files',
    author='Baslael Workineh',
    author_email='your.email@example.com',
    url='https://github.com/BaslaelWorkineh/Merge_wav_files',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'soundfile',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
