import os
import source.config as config
from source.plot_results import plot_results
from source.retrieval import get_l1_score, get_l2_score, get_cosine_similarity_score, get_correlation_coefficient_score


def query_images(query_path, get_similarity, method_name, reverse=False):
    query_path = os.path.join(config.TEST_DIR, query_path)
    _, ls_path_score = get_similarity(
        config.TRAIN_DIR, query_path, config.IMAGE_SIZE)
    plot_results(query_path, ls_path_score, reverse=reverse,
                 save=True, filename=method_name)


def run_retrieval():
    query_path = 'Orange_easy/0_100.jpg'
    query_images(query_path, get_l1_score, 'l1')
    query_images(query_path, get_l2_score, 'l2')
    query_images(query_path, get_cosine_similarity_score,
                 'cosine_similarity', True)
    query_images(query_path, get_correlation_coefficient_score,
                 'correlation_coefficient', True)


if __name__ == "__main__":
    run_retrieval()
