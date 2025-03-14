# **TV Shows Organizer**  

This Python script automatically organizes downloaded TV show episodes by moving them into properly named **season folders** within a target directory.  

## **Features**  

✅ **Automatic Episode Detection** – Identifies TV show episodes in your `Downloads` folder based on user input.  
✅ **Organized Folder Structure** – Moves episodes into a **series folder**, categorized by **seasons** (e.g., `S01`, `S02`).  
✅ **Dynamic Filename Handling** – Works with filenames containing **dots, underscores, or dashes** by normalizing them.  
✅ **Auto-Creation of Folders** – If the **series or season folder** doesn’t exist, the script **creates them automatically**.  
✅ **Logging Support** – Provides **detailed logs** to track moved files.  

---

## **How It Works**  

1️⃣ The script **prompts you to enter the TV series name**.  
2️⃣ It scans your `~/Downloads` folder for files that match the **normalized** series name (ignoring dots, dashes, and underscores).  
3️⃣ It detects the **season number** using patterns like `S01`, `s01`, etc., in filenames.  
4️⃣ It moves the files to the structured target folder:  
   ```
   ~/videos/{SeriesName}/SXX/ (e.g., ~/videos/Breaking Bad/S01/)
   ```  
5️⃣ If the **series or season folder doesn’t exist**, it **automatically creates it**.  

---

## **Requirements**  

- **Python 3.x**  
- **Standard Python Libraries Used:**  
  - `os` – For file handling  
  - `shutil` – For moving files  
  - `logging` – For tracking operations  
  - `re` – For pattern matching in filenames  

---

## **Installation & Usage**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/hafiz-yss/automation-scripts.git
cd automation-scripts/tv-shows-organizer
```

### **2️⃣ Run the Script**  
```bash
python tv-shows-organizer.py
```

### **3️⃣ Enter the Series Name**  
When prompted, enter the **TV series name** (punctuation and capitalization do not matter).  

**Example:**  
If your downloaded files look like this:  
```
Breaking.Bad.S01E01.720p.mkv  
Breaking-Bad_S01E02_1080p.mp4  
```
You can simply enter:  
```
Breaking Bad
```
The script will then move them to:  
```
~/videos/Breaking Bad/S01/
```

---

## **Folder Structure Example**  

### **Before Running the Script**  
```
~/Downloads/  
│── Breaking.Bad.S01E01.720p.mkv  
│── Breaking-Bad_S01E02_1080p.mp4  
│── Random.Movie.2023.mkv  
```

### **After Running the Script**  
```
~/videos/  
└── Breaking Bad/  
    ├── S01/  
    │   ├── Breaking.Bad.S01E01.720p.mkv  
    │   ├── Breaking-Bad_S01E02_1080p.mp4  
```

---

## **⚠️ Notes**  

- **Case-Insensitive Matching** – The script **normalizes filenames**, so dots, dashes, and underscores do not matter.  
- **Season Detection** – Works with `SXX` patterns (e.g., `S01`, `s02`).  
- **Files Without a Season Number Are Skipped** – If a file does **not** contain `SXX`, it **will not be moved**.  
- **Creates Missing Folders** – No need to manually create directories.  
- **Only Moves Matching Files** – Other files in `Downloads` (such as movies or unrelated videos) **are left untouched**.  

---

## **License**  

This project is **open-source** under the **MIT License**.  

---

## **Contributing**  

🔹 Found a bug? Have an idea? Feel free to **fork the repo** and submit a **pull request**!  

