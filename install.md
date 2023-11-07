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

### 1.2 Pemasangan Lingkungan

Jalankan perintah berikut

```
pip install -r requirements.txt
```
