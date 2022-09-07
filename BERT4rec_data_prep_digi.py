from os import listdir
from os.path import join



if __name__ == '__main__':

    input_dir = "/home/mdev/session-rec-empirical/data/digi/slices/"
    # output_dataset_dir = "/home/mdev/session-rec-empirical/data/rsc15/BERT4REC_prepared"
    output_dataset_dir = "/home/mdev/BERT4rec_py3_tf2/BERT4rec/data/digi/input/"

    all_datasets_filenames = ["train-item-views_train_full.txt", "train-item-views_test.txt"]


    unique_session_count = 0
    current_session_id = ""
    unique_item_count = 0
    item_map = {}  # key is real item id, value is transformed id (current unique item id)
    for dataset_filename in all_datasets_filenames:

        input_dataset_path = join(input_dir, dataset_filename)
        output_dataset_path = join(output_dataset_dir, dataset_filename)

        with open(input_dataset_path) as input, open(output_dataset_path, "a") as output:
            input.readline()  # first line is header; not neccessary for BERT4REC

            for line in input:
                line_all_columns = line.split("\t")
                session_id, item_id = (line_all_columns[0], line_all_columns[2])

                if session_id != current_session_id:
                    unique_session_count += 1
                    current_session_id = session_id
                transformed_session_id = str(unique_session_count)

                transformed_item_id = ""
                if item_id in item_map:
                    transformed_item_id = item_map.get(item_id)
                else:
                    unique_item_count += 1
                    transformed_item_id = str(unique_item_count)
                    item_map[item_id] = transformed_item_id

                output.write(transformed_session_id + " " + transformed_item_id + "\n")



