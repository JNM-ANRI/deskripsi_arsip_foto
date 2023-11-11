# Periksa kebutuhan Sistem 
Deskripsi arsip membutuhkan CUDA, periksa apakah driver cuda sudah terinstall pada sistem    
cara 1
```
nvcc --version
```
cara 2
```
nvidia-smi
```
cara 3
```
whereis cuda
```
> Jika sudah diketahui lokasi CUDA
```
export CUDA_HOME=/path/to/your/cuda
```
contoh: 
```
export PATH=/usr/lib/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/lib/cuda/lib64:$LD_LIBRARY_PATH
```
membuat permanen 
```
nano ~/.bashrc
export PATH=/usr/lib/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/lib/cuda/lib64:$LD_LIBRARY_PATH
source ~/.bashrc
```
# Install Cuda di ubuntu
```
sudo apt install nvidia-cuda-toolkit
```

# Persiapan Sistem  
```
conda create --name i2p python=3.8 -y  
conda activate i2p   
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html  

git clone https://github.com/facebookresearch/detectron2.git  
cd detectron2  
cd ..
pip install -r requirements.txt  
pip install -U transformers  
pip install openai  
pip install --upgrade diffusers[torch]  

pip install setuptools==59.5.0
atau
pip install setuptools==60.2.0

pip install git+https://github.com/facebookresearch/segment-anything.git  
pip install -U openmim  
mim install mmcv  
pip install spacy  
python -m spacy download en_core_web_sm  
```

# 1. Instalasi

### 1.1 Unduh Model yang Sudah Dilatih
Pertama, navigasikan ke direktori proyek, kemudian unduh model yang sudah dilatih dari Segment Anything dan grit.

```bash
cd [PATH_KE_PROYEK_INI]
mkdir pretrained_models
cd pretrained_models
wget -c https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth
wget -c https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
wget -c https://datarelease.blob.core.windows.net/grit/models/grit_b_densecap_objectdet.pth
cd ..
```
