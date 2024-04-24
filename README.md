# Dr-NEAR-GHack-2024

The project aims to create a Medical Assistant application that helps users find appropriate healthcare providers based on their symptoms. This system utilizes a database that includes doctor profiles with details like name, location, experience, specialty, and user ratings and reviews. Another database lists common symptoms and the corresponding medical specialties required for treatment. The application employs a LinearSVC machine learning model from scikit-learn library to recommend doctors by matching their specialties, experience, and proximity to the user's location.

## Live Features:

- Recommendations based on symptoms, doctor experience, and user ratings.
- Users can select doctors based on their availability according to their schedule.

## Upcoming Features:

- Implementation of NLP techniques to assess the authenticity of user reviews and calculate a "genuine score" for each doctor, enhancing recommendation reliability.
- Integration of a WhatsApp chatbot for seamless communication, offering users an easy and accessible way to interact with the system.
- Development of a voice-activated AI assistant to accommodate users who prefer voice input, improving accessibility and user experience.
- Creation of a dedicated section for blogs authored by renowned doctors, covering various health topics such as emergency procedures and nutritional advice.

## Getting Started

Follow the instruction given to set up environment and run this project on your local machine.

### Prerequisites

Before installing the project, ensure you have the following software installed on your local machine:

- Python (Recommended version 3.9)
- Pip (Python Package Installer)

#### Installing Prerequisites on Windows

1. **Python:**
   - Download the Python 3.9 installer from the official [Python website](https://www.python.org/downloads/release/python-390/).
   - Run the installer. Make sure to check the box that says "Add Python 3.9 to PATH" at the beginning of the installation process.
   - Complete the installation and verify the installation by opening Command Prompt and running:
     ```bash
     python --version
     ```
   - Python should report back with "Python 3.9.x".

2. **Pip:**
   - Pip is included by default when you install Python 3.4 or later, so it should already be installed. You can check by running:
     ```bash
     pip --version
     ```

#### Installing Prerequisites on Linux

1. **Python:**
   - Most Linux distributions come with Python pre-installed. To check if Python is installed and its version, open a terminal and run:
     ```bash
     python3 --version
     ```
   - If you don't have Python 3.9, you can install it using the package manager of your Linux distribution. For example, on Ubuntu:
     ```bash
     sudo apt update
     sudo apt install python3.9
     ```

2. **Pip:**
   - To install pip on Linux, if it isn't already installed, run:
     ```bash
     sudo apt install python3-pip
     ```
   - Verify pip installation with:
     ```bash
     pip3 --version
     ```
 
### Installation

#### Step 1: Configure Your Local Environment

Set up your local development environment. This involves ensuring that all the necessary tools and software mentioned in the Prerequisites section are installed.

#### Step 2: Clone the Repository

To get started with the project, clone the repository to your local machine:

```bash
git clone https://github.com/siriarelli/Dr-NEAR-GHack-2024.git
cd Dr-NEAR-GHack-2024
```
### Step 3: Install Required Libraries
Navigate to the project directory where the requirements.txt file is located and install the required libraries:

```bash
pip install -r requirements.txt
```
### Step 4: Run the Application
To start the application, use the following command:

```bash
streamlit run app.py
```
## Conclusion

This README provides you with all the necessary steps to set up and run the Medical Assistant application on your local machine. If you follow these instructions carefully, you should be able to start the application without any issues. The application is designed to help you find suitable healthcare providers based on your symptoms. If you encounter any difficulties during the installation or operation of the application, please do not hesitate to reach out for support by emailing siriarelli1@gmail.com. Your feedback and queries are always welcome, as they help improve the project and assist you better.