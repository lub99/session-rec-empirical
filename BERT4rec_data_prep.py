from os import listdir
from os.path import join


def transform_line(line):
    line_without_timestamp = line.rsplit("\t", 1)[0]
    output.write(line_without_timestamp + "\n")


if __name__ == '__main__':

    all_datasets_txts_dir_path = "/home/mdev/session-rec-empirical/data/rsc15/prepared"
    # output_dataset_dir = "/home/mdev/session-rec-empirical/data/rsc15/BERT4REC_prepared"
    output_dataset_dir = "/home/mdev/BERT4rec_py3_tf2/BERT4rec/data"

    all_datasets_filenames = ["yoochoose-clicks-100k_train_full.txt", "yoochoose-clicks-100k_test.txt"]

    unique_session_count = 0
    current_session_id = ""
    unique_item_count = 0
    item_map = {}  # key is real item id, value is transformed id (current unique item id)
    for input_dataset_filename in all_datasets_filenames:
        output_dataset_filename = "BERT4REC_" + input_dataset_filename

        input_dataset_path = join(all_datasets_txts_dir_path, input_dataset_filename)
        output_dataset_path = join(output_dataset_dir, output_dataset_filename)

        with open(input_dataset_path) as input, open(output_dataset_path, "a") as output:
            input.readline()  # first line not neccessary for BERT4REC

            for line in input:
                line_without_timestamp = line.rsplit("\t", 1)[0]
                session_id, item_id = line_without_timestamp.split("\t")

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
