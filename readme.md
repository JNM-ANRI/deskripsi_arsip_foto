```
git clean -fd
git checkout -b prompt-indo origin/prompt-indo
```



#### Doing
- [ ] Merekognisi dan mendeteksi tokoh sejarah, misalnya(tokoh pada kabinet kerja).
- [ ] Menerima input data foto secara masal.
- [ ] Output dapat berupa daftar arsip / katalog arsip foto beserta deskripsinya.
- [ ] Tersedia API yang memungkinkan model dapat diintegrasikan dengan sistem lain 


##  Installation

Cara instalasi dapat dilihat di [install.md](install.md).


### Persiapkan OpenAI API key
```
echo 'export OPENAI_KEY=yourkeyhere' >> ~/.bashrc
source ~/.bashrc


```


## 2. Start

## Use gradio directly

```bash
python main_gradio.py
```

