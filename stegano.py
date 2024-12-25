import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Function to encode text in the image
def hide_text(image_path, text):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGB")
        
        # Convert the text to binary
        binary_text = ''.join(format(ord(i), '08b') for i in text)
        
        # Ensure the text fits in the image
        max_capacity = img.width * img.height * 3  # 3 values (RGB) per pixel
        if len(binary_text) > max_capacity:
            messagebox.showerror("Error", "Text is too long to hide in this image.")
            return None
        
        pixels = img.load()
        text_index = 0
        
        # Hide the binary text in the least significant bits of the image
        for y in range(img.height):
            for x in range(img.width):
                if text_index < len(binary_text):
                    r, g, b = img.getpixel((x, y))
                    
                    # Modify the least significant bit (LSB) for each color channel
                    new_r = r & 0xFE | int(binary_text[text_index])  # Modify the LSB of red
                    text_index += 1
                    new_g = g & 0xFE | int(binary_text[text_index])  # Modify the LSB of green
                    text_index += 1
                    new_b = b & 0xFE | int(binary_text[text_index])  # Modify the LSB of blue
                    text_index += 1
                    
                    pixels[x, y] = (new_r, new_g, new_b)
                else:
                    break
            if text_index >= len(binary_text):
                break
        
        # Save the image with hidden text
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if output_path:
            img.save(output_path)
            messagebox.showinfo("Success", f"Text hidden successfully. Image saved to {output_path}")
        return output_path
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to decode text from the image
def reveal_text(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        pixels = img.load()
        
        binary_text = ""
        
        # Extract the least significant bits
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                binary_text += str(r & 1)  # Extract the LSB of red
                binary_text += str(g & 1)  # Extract the LSB of green
                binary_text += str(b & 1)  # Extract the LSB of blue
        
        # Convert the binary text back to characters, stopping at null character
        text = ""
        for i in range(0, len(binary_text), 8):
            byte = binary_text[i:i+8]
            if len(byte) < 8:
                break
            char = chr(int(byte, 2))
            if char == '\x00':  # Stop at null character (end of hidden message)
                break
            text += char
        
        return text
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Code
class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography - Text in Image")
        self.root.geometry("400x400")
        
        # Hide text functionality
        self.hide_button = tk.Button(root, text="Hide Text in Image", command=self.hide_text)
        self.hide_button.pack(pady=20)
        
        # Reveal text functionality
        self.reveal_button = tk.Button(root, text="Reveal Hidden Text", command=self.reveal_text)
        self.reveal_button.pack(pady=20)
        
        # Text Entry for hiding
        self.text_entry_label = tk.Label(root, text="Enter text to hide:")
        self.text_entry_label.pack()
        
        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=10)
        
    def hide_text(self):
        text = self.text_entry.get()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to hide.")
            return
        
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if image_path:
            hide_text(image_path, text)
    
    def reveal_text(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if image_path:
            hidden_text = reveal_text(image_path)
            messagebox.showinfo("Revealed Text", f"Hidden Text: {hidden_text}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root) 
    root.mainloop()
