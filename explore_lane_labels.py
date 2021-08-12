import json

path = "/media/urw7rs/Data/bdd100k/labels/lane/polygons/lane_train.json"
with open(path) as f:
    train_labels = json.load(f)

label_cat = {}
for image in train_labels:
    if "labels" in image.keys():
        labels = image["labels"]
        for single_label in labels:
            for category in single_label.keys():
                label_category = single_label[category]
                if category not in label_cat.keys():
                    label_cat[category] = []
                if label_category not in label_cat[category]:
                    label_cat[category].append(label_category)

print(label_cat)
