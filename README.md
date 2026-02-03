# Student Exam Venue Lookup System
# منظومة الاستعلام عن أماكن الامتحانات - قسم التغذية العلاجية

A professional, mobile-responsive web application for searching student exam venues by Enrollment Number.

## Features
- **Search by Enrollment Number**: Finds Seat Number and Exam Hall.
- **Offline Ready**: Works without a backend server (using `data.js`).
- **Modal Results**: Professional pop-up with details.
- **Print Support**: Clean PDF printing for student cards.
- **Academic Design**: Navy Blue & Gold theme.

## How to Deploy (Important!)

Since this is a **Static Website** (HTML/CSS/JS only), you **DO NOT** need a Python environment to run it, but you need Python to **update the data**.

### 🚀 Option 1: Render.com (Recommended)
This project includes a `render.yaml` file for automatic configuration.

1.  Go to the Render Dashboard.
2.  Click **New +** and select **Static Site**.
3.  Connect this repository.
4.  Render should automatically detect the settings. If not:
    -   **Build Command**: (Leave empty)
    -   **Publish Directory**: `.` (Dot, meaning root directory)
5.  Click **Create Static Site**.

### 📝 How to Update Data
1.  Edit `data.xlsx` with new student information.
2.  Run the build script:
    ```bash
    python build_data.py
    ```
3.  This will update `data.js` automatically.
4.  **Push** the changes to GitHub to update the live site.

### 🛠️ Requirements
If you need to run the update script, install dependencies:
```bash
pip install -r requirements.txt
```
