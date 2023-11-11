import os
import shutil
source_folder = "/content/drive/MyDrive/NLP DATASETS- Meme Datasest/my_data_images"
destination_folder = "/content/drive/MyDrive/NLP DATASETS- Meme Datasest"
batch_size = 2000
num_batches = len(os.listdir(source_folder)) // batch_size + 1

for i in range(num_batches):
    batch_folder = os.path.join(destination_folder, f"batch{i + 1}")
    os.makedirs(batch_folder, exist_ok=True)

image_files = os.listdir(source_folder)

for i, image_file in enumerate(image_files):
    source_path = os.path.join(source_folder, image_file)
    batch_index = i // batch_size
    batch_folder = os.path.join(destination_folder, f"batch{batch_index + 1}")
    destination_path = os.path.join(batch_folder, image_file)

    shutil.move(source_path, destination_path)

    if (i + 1) % batch_size == 0:
        print(f"Moved {i + 1} images to {batch_folder}")
