UPI QR Code Generator

A simple Python project that generates UPI payment QR codes using a UPI ID. It creates a scannable QR code and displays the UPI ID below it in a clean, professional design.

 About the Project

The UPI QR Code Generator makes it easy to create and share payment QR codes. Users enter their UPI ID, and the program generates a QR code containing the corresponding UPI payment information.

The generated image displays a **SCAN & PAY** heading, the QR code, and the UPI ID below it.

 Features

*  Generate QR codes using a UPI ID.
*  Display the UPI ID below the QR code.
*  Create a clean and professional QR code design.
*  Save the generated QR code as a PNG image.
*  Automatically display the generated image.
*  Simple and beginner-friendly Python implementation.

 Technologies Used

* **Python** — Core programming language.
* **qrcode** — For generating QR codes.
* **Pillow (PIL)** — For image creation and customization.

 Installation

### 1. Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/upi-qr-code-generator.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 3. Navigate to the Project Directory

```bash
cd upi-qr-code-generator
```

### 4. Install the Required Library

```bash
python -m pip install "qrcode[pil]"
```

 How to Run

Run the following command in your terminal:

```bash
python qrcodegen.py
```

Enter your UPI ID when prompted.

For example:

```text
Enter your UPI ID: yourname@upi
```

The program will generate a QR code image named `upi_qr.png` and display it.

**Note:** `yourname@upi` is an example, not a real payment address.

 Example Output

The generated QR code image contains:

* **SCAN & PAY** heading
* UPI payment QR code
* UPI ID displayed below the QR code

 
This project generates QR codes containing UPI payment information. It does not process payments, verify payment completion, or guarantee that a UPI ID is valid.

Always test the generated QR code using a trusted UPI application before sharing it for actual payments.

⭐ If you find this project useful, consider giving the repository a star!
