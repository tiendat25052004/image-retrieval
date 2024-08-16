import matplotlib.pyplot as plt
import os
from PIL import Image
from source.data_loader import read_image_from_path
import source.config as config


def plot_results(query_path, ls_path_score, reverse=False, save=False, filename=''):
    fig = plt.figure(figsize=(15, 9))
    fig.add_subplot(2, 3, 1)

    # Display query image
    query_image = read_image_from_path(query_path, config.IMAGE_SIZE)
    plt.imshow(query_image)
    query_path = query_path.replace('\\', str('/'))
    plt.title(f"Query Image: {query_path.split('/')[2]}", fontsize=16)
    plt.axis("off")

    # Display top 5 results
    ls_path_score = sorted(
        ls_path_score, key=lambda x: x[1], reverse=reverse)[:5]
    for i, (image_path, score) in enumerate(ls_path_score, start=2):
        fig.add_subplot(2, 3, i)
        result_image = read_image_from_path(image_path, size=config.IMAGE_SIZE)
        plt.imshow(result_image)
        image_path = image_path.replace('\\', str('/'))
        plt.title(f"Top {i-1}: {image_path.split('/')[2]}", fontsize=16)
        plt.axis("off")

    # Save plot
    if save:
        output_dir = 'assets/demo_images'
        os.makedirs(output_dir, exist_ok=True)
        output_path = f"{query_path.split('/')[2]}_{filename}_result.png"
        plt.savefig(os.path.join(output_dir, output_path))

    plt.show()
