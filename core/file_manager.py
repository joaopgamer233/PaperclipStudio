from PIL import Image


class FileManager:
    @staticmethod
    def open_image(path):
        """
        Opens an image using Pillow.
        """
        return Image.open(path)

    @staticmethod
    def save_image(image, path):
        """
        Saves a Pillow image.
        """
        image.save(path)

    @staticmethod
    def new_image(width, height, color="white"):
        """
        Creates a new blank image.
        """
        return Image.new("RGBA", (width, height), color)