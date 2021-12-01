import os
from PIL import Image

def main(main_images_folder,new_width=200):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe') #para ver se a pasta existe

    for root, dirs, files in os.walk(main_images_folder): #nova largura
        for file in files:
            file_full_path = os.path.join(root,file)#caminho
            file_name, extension = os.path.splitext(file) # para não subresecsvrer retornar arquivo e extensão
            convert_tag=   'converted'

            new_file =file_name+convert_tag+ extension # criar nova imagem
            new_file_full_path = os.path.join(root, new_file)

            if convert_tag in file_full_path:
               continue
               #volta o laço e não converter se tiver o msm nome

            img_pillow= Image.open(file_full_path)
            width,height= img_pillow.size #tamanho da imagem, largura e tamanho
            new_height = round((new_width) * height)/width
            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS
            )

            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70,
            )

            new_image.close()
            img_pillow.close()


if __name__ == '__main__':
    main_images_folder = 'Redim'
    main(main_images_folder, new_width=200)

