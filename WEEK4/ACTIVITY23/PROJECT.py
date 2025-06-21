import csv
import pandas as pd
from PIL import Image

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process(self):
        raise NotImplementedError("Subclasses must implement this method")


class CSVProcessor(FileProcessor):
    def process(self):
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
                print(f"\nCSV File: {self.file_path}")
                print(f"Total rows: {len(rows)}")
                if rows:
                    print("Header:", rows[0])
                    print("First row:", rows[1] if len(rows) > 1 else "N/A")
        except Exception as e:
            print(f"Error reading CSV: {e}")


class TextProcessor(FileProcessor):
    def process(self):
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                lines = file.readlines()
                print(f"\nText File: {self.file_path}")
                print(f"Total lines: {len(lines)}")
                if lines:
                    print("First line:", lines[0].strip())
                    print("Last line:", lines[-1].strip())
        except Exception as e:
            print(f"Error reading TXT: {e}")


class ParquetProcessor(FileProcessor):
    def process(self):
        try:
            df = pd.read_parquet(self.file_path)
            print(f"\nParquet File: {self.file_path}")
            print(f"Total records: {len(df)}")
            print("Columns:", list(df.columns))
            print("First row:\n", df.iloc[0] if not df.empty else "N/A")
        except Exception as e:
            print(f"Error reading Parquet: {e}")


class ImageProcessor(FileProcessor):
    def process(self):
        try:
            import tensorflow as tf
            import numpy as np
            import matplotlib.pyplot as plt

            img = Image.open(self.file_path).convert('RGB')  # Ensure it's RGB
            print(f"\nImage File: {self.file_path}")
            print(f"Format: {img.format}")
            print(f"Size: {img.size}")
            print(f"Mode: {img.mode}")

            # Display the image
            plt.imshow(img)
            plt.title("Loaded Image")
            plt.axis('off')
            plt.show()

            img = img.resize((32, 32))  
            img_array = np.array(img) / 255.0 
            img_array = np.expand_dims(img_array, axis=0) 

            label = np.array([0])

            model = tf.keras.Sequential([
                tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(32, 32, 3)),
                tf.keras.layers.MaxPooling2D((2, 2)),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(32, activation='relu'),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])

            model.compile(optimizer='adam',
                        loss='binary_crossentropy',
                        metrics=['accuracy'])

            print("\nTraining the model on the single loaded image (dummy label)...")
            model.fit(img_array, label, epochs=3, verbose=2)

            print("Training complete.")

        except Exception as e:
            print(f"Error reading or processing image: {e}")


def main():
    print("Welcome to the File Processor Tool!")
    while True:
        print("\nChoose an option:")
        print("1. Process CSV file")
        print("2. Process TXT file")
        print("3. Process Parquet file")
        print("4. Process Image file")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            file_path = input("Enter path to CSV file: ").strip()
            processor = CSVProcessor(file_path)
            processor.process()
        elif choice == '2':
            file_path = input("Enter path to TXT file: ").strip()
            processor = TextProcessor(file_path)
            processor.process()
        elif choice == '3':
            file_path = input("Enter path to Parquet file: ").strip()
            processor = ParquetProcessor(file_path)
            processor.process()
        elif choice == '4':
            file_path = show.input("Enter path to Image file: ").strip()
            processor = ImageProcessor(file_path)
            processor.process()
        elif choice == '5':
            print("See ya Later, Alligator!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()