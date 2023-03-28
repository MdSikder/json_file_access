import os, json

path_to_json_files = '../json/B_6/photo1/ann/'
# get all JSON file names as a list
json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

for json_file_name in json_file_names:
    with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
        json_text = json.load(json_file)

        # ##################print all file name and values  #################
        print(json_file_name, json_text)

        # print all file name
        # print(json_file_name)
