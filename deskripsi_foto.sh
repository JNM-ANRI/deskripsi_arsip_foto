#!/bin/bash

# Aktifkan conda environment
source /home/lambda_one/anaconda3/etc/profile.d/conda.sh
conda activate i2p

# Jalankan program python Anda
sudo python /home/lambda_one/project/i2p/main_gradio.py
