import openai


class ImageToText:
    # def __init__(self, api_key, gpt_version="gpt-3.5-turbo"):
    #     self.template = self.initialize_template()
    #     openai.api_key = api_key
    #     self.gpt_version = gpt_version

    def __init__(self, api_key, gpt_version="gpt-4"):
        self.template = self.initialize_template()
        openai.api_key = api_key
        self.gpt_version = gpt_version

    # def initialize_template(self):
    #     prompt_prefix_1 = """buat paragraf yang informatif dan deskripsi yang alami untuk konten photo berdasarkan pada
    #     informasi yang diberikan berikut:\n"""

    # ##---------------------indonesian version---------------------###
    def initialize_template(self):
        prompt_prefix_1 = """Buatlah deskripsi informatif dan alamiah untuk konten foto berdasarkan informasi yang
        diberikan :\n"""
        # prompt_prefix_2 = """\n a. Resolusi Gambar:  """
        prompt_prefix_3 = """\n b. Keterangan Gambar: """
        prompt_prefix_4 = """\n c. Keterangan Padat: """
        prompt_prefix_5 = """\n d. Semantik Wilayah: """
        prompt_suffix = """\n Ada beberapa aturan: Buatlah paragraf informatif dan ringkas yang mendeskripsikan
        konten foto, berdasarkan aturan-aturan berikut ini: 1. Berikan deskripsi yang informatif tentang konten foto,
        termasuk apa yang terjadi (What), kapan terjadi (When), di mana terjadi (Where), siapa yang terlibat (Who),
        mengapa terjadi (Why), dan bagaimana keadaan sekitar (How), tidak perlu menyertakan kata what, when, where,
        who, why, how. 4. Batasi deskripsi menjadi tidak lebih dari 7 kalimat. 5. Sajikan deskripsi konten dalam satu
        paragraf 7. Hindari penggunaan angka atau koordinat dalam deskripsi konten. Fokus pada peristiwa sejarah yang
        terjadi pada foto. 8. Jika diketahui tokoh sejarah atau peristiwa penting, sebutkan dalam deskripsi 9. susun
        deskripsi konten foto dengan gaya naratif yang alamiah dan mudah dibaca. 10. berikan hashtag dengan bahasa
        indonesia untuk kata kunci yang relevan, subjek, objek penting dan fitur kunci atau hal menonjol lainnya,
        tampilkan pada bagian bawah paragraf secara terpisah"""

    # -----------------english version-----------------#
    # def initialize_template(self):
    #     prompt_prefix_1 = """Create an informative and natural description for the content of the photo based on the
    #     information provided :\n"""
    #     # prompt_prefix_2 = """\n a. Image Resolution:  """
    #     prompt_prefix_3 = """\n b. Image Caption: """
    #     prompt_prefix_4 = """\n c. Dense Caption: """
    #     prompt_prefix_5 = """\n d. Semantic Region: """
    #     prompt_suffix = """\n There are a few rules: Craft an informative and concise paragraph that describes
    #     the content of the photo, based on the following rules: 1. Provide an informative description of the
    #     photo content, including what is happening (What), when it happened (When), where it happened (Where),
    #     who is involved (Who), why it happened (Why), and how the surrounding situation is (How). 4. Limit the
    #     description to no more than 7 sentences. 5. Present the content description in one paragraph 7. Avoid the
    #     use of numbers or coordinates in the content description. Focus on the historical event happening in the
    #     photo. 8. If a historical figure or significant event is known, mention it in the description 9. compose
    #     the photo content description in a naturally narrative and readable style. 10. provide hashtags in
    #     for relevant keywords, subjects, important objects and key features or other standout things,
    #     display at the bottom of the paragraph separately"""
    #
        # template = f"{prompt_prefix_1}{prompt_prefix_2}{{width}}X{{height}}{prompt_prefix_3}{{caption}}{prompt_prefix_4}{{dense_caption}}{prompt_prefix_5}{{region_semantic}}{prompt_suffix}"
        template = f"{prompt_prefix_1}{prompt_prefix_3}{{caption}}{prompt_prefix_4}{{dense_caption}}{prompt_prefix_5}{{region_semantic}}{prompt_suffix}"
        return template



    def paragraph_summary_with_gpt(self, caption, dense_caption, region_semantic, width, height):
        question = self.template.format(width=width, height=height, caption=caption, dense_caption=dense_caption,
                                        region_semantic=region_semantic)
        print('\033[1;35m' + '*' * 100 + '\033[0m')
        print('\nStep4, Paragraph Summary with GPT-3:')
        print('\033[1;34m' + "Question:".ljust(10) + '\033[1;36m' + question + '\033[0m')
        completion = openai.ChatCompletion.create(
            model=self.gpt_version,
            messages=[
                {"role": "user", "content": question}]
        )

        print('\033[1;34m' + "ChatGPT Response:".ljust(18) + '\033[1;32m' + completion['choices'][0]['message'][
            'content'] + '\033[0m')
        print('\033[1;35m' + '*' * 100 + '\033[0m')
        return completion['choices'][0]['message']['content']

    def paragraph_summary_with_gpt_debug(self, caption, dense_caption, width, height):
        question = self.template.format(width=width, height=height, caption=caption, dense_caption=dense_caption)
        print("paragraph_summary_with_gpt_debug:")
        return question
