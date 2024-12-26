# Image Captioning Project

This repository contains an implementation of an image captioning model using deep learning techniques. The model generates descriptive captions for images, leveraging state-of-the-art neural network architectures.

## Features
- Downloads and processes the **Flickr8k Dataset**.
- Utilizes **EfficientNet** for image feature extraction.
- Incorporates **TextVectorization** for caption preprocessing.
- Implements an encoder-decoder architecture with attention mechanisms.

## Dataset
The project uses the **Flickr8k Dataset**, which consists of:
- 8,000 images.
- 40,000 captions (5 captions per image).

To download the dataset separately, run the provided script:
```bash
python download_dataset.py
```

## Dependencies
Ensure you have the required Python libraries installed. Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
### Step 1: Clone the Repository
```bash
git clone https://github.com/n7kadda/image_caption.git
cd image-caption
```

### Step 2: Install Dependencies
Install the required libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Download the Dataset
Run the dataset download script:
```bash
python download_dataset.py
```

### Step 4: Run the Jupyter Notebook
Ensure you have Jupyter Notebook installed. Open the notebook and execute the cells sequentially.
```bash
jupyter notebook final_img_captioning.ipynb
```

### Step 5: View Results
The model will output captions for test images, demonstrating its capabilities.

## Model Architecture
- **Encoder**: Uses EfficientNet to extract image features.
- **Decoder**: A sequence-to-sequence model with LSTM layers and attention mechanisms.

## Results
After training, the model generates captions that describe the content of images accurately. Examples are provided in the notebook.

## Customization
To use your own dataset, replace the Flickr8k dataset with your images and captions. Modify the data preprocessing steps accordingly.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- [Flickr8k Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k)
- TensorFlow and Keras Documentation


