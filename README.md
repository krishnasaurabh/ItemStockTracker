# Item Stock Tracker
[![Build Status](https://github.com/ramyasaimullapudi/ItemStockTracker/workflows/Build%20Status/badge.svg)](https://github.com/ramyasaimullapudi/ItemStockTracker/actions)
[![codecov](https://codecov.io/gh/ramyasaimullapudi/ItemStockTracker/branch/main/graph/badge.svg?token=EHYPNZ5ACP)](https://codecov.io/gh/ramyasaimullapudi/ItemStockTracker)

![GitHub](https://img.shields.io/badge/language-python-blue.svg)
<a href="https://zenodo.org/badge/latestdoi/416888118"><img src="https://zenodo.org/badge/416888118.svg" alt="DOI"></a>
![GitHub](https://img.shields.io/github/license/ramyasaimullapudi/ItemStockTracker)


![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ramyasaimullapudi/ItemStockTracker)
![GitHub open issues](https://img.shields.io/github/issues/ramyasaimullapudi/ItemStockTracker)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/ramyasaimullapudi/ItemStockTracker)
![GitHub all downloads](https://img.shields.io/github/downloads/ramyasaimullapudi/ItemStockTracker/total)


# "Item Stock Tracker" is a program designed to alert users when specific items from an online retailer are back in stock.



https://user-images.githubusercontent.com/34405372/135356983-439e7808-8268-41aa-ad82-38615d4a773e.mp4



### Prerequisites
Make sure you have installed and followed all of the following prerequisites on your development machine:

* Python-- [Download & Install Python 3.9](https://www.python.org/downloads/release/python-390/)
* Email-- Fill out the email address(gmail_user) and password(gmail_password) in SendEmail.py as the sender email
* pillow-- [Download & Install Pillow for python with version>=8.3.0](https://pillow.readthedocs.io/en/stable/)
* requests-- [Download & Install Requests for python with version~=2.26.0](https://docs.python-requests.org/en/latest/)
* beautifulsoup4-- [Download & Install Beautifulsoup4 for python with version~=4.10.0](https://pypi.org/project/beautifulsoup4/)
* lxml-- [Download & Install lxml for Python with version~=4.6.3](https://lxml.de)
* setuptools-- [Download & Install setuptools for Python with version~=57.0.0](https://pypi.org/project/setuptools/)
* sphinx-- [Download & Install setuptools for Python with sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
* sphinx-rtd-theme-- [Download & Install setuptools for Python with sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/)

### Documentation
[Item Stock Tracker’s documentation](https://itemstocktracker1.readthedocs.io/en/latest/)

### Installation

1. Download the project from GitHub or clone the repository.

`git clone https://github.com/ramyasaimullapudi/ItemStockTracker.git`



<img width="714" alt="Screen Shot 2021-10-06 at 3 30 28 AM" src="https://user-images.githubusercontent.com/34405372/136159116-5de09c46-95ac-4531-ada6-d14933d41478.png">

2. Change the current directory to the project folder, install the required packages.

`cd ItemStockTracker`

`pip install -r requirements.txt`

3. Change the current directory to `code`, then run the `GUI.py`.

`cd code`

`python3 GUI.py`

### Build executable 

To build the executable, you need to have pyinstaller installed which can be done using `pip install pyinstaller`. 
Navigate to `ItemStockTracker` folder and run the below commands based on the operating system you are running.

For Windows 

`pyinstaller --distpath ./build/dist --workpath ./build/build --noconfirm ./ItemStockTracker.spec`

For Mac

`pyinstaller  --distpath ./build/dist --workpath ./build/build --noconfirm ./ItemStockTrackerMac.spec`

The executable will be found in the folder</br>
`ItemStockTracker/build/dist/ItemStockTracker/ItemStockTracker.exe` for windows</br>
`ItemStockTracker/build/dist/ItemStockTrackerMac/ItemStockTrackerMac.exe` for windows



### USAGE
---


![image](https://user-images.githubusercontent.com/19464321/140402539-b528fbaa-b352-454d-96ae-a9af6b01f623.png)

By default, the GUI will already contain some data, which is loaded from `data/tracker.txt`. To add your own items, click the plus button in the upper right. You will be prompted to enter a name for the item you are tracking, along with a URL for a specific product page. Currently, `amazon.com`, `bestbuy.com` and `walmart.com` product pages are supported.
  
![7](https://user-images.githubusercontent.com/51504486/140412693-de447000-4c6e-47c8-88da-f31ffc6b1c6d.PNG)

You can also edit, add, or delete items by right-clicking on a selected item,
  
![8](https://user-images.githubusercontent.com/51504486/140413151-fa73f2fc-adde-4f8a-ae91-1e95f06a6dce.PNG)

When an item is restocked, a popup will appear. Aditionally, a system notification will also be generated 
  
  ![image](https://user-images.githubusercontent.com/30803969/134995936-a4088c47-229a-43cf-b01d-a9ae6e787b7b.png) ![5](https://user-images.githubusercontent.com/51504486/140413777-9632cd0b-9a50-48f6-874b-6cf8fb40c0a4.PNG)
  
Lastly, in the "Settings" tab you can adjust the refresh interval (how often the program will poll the website to check the stock status of your items), and configure your email alert settings.

  ![image](https://user-images.githubusercontent.com/30803969/134995891-10801bc1-8d94-44be-8e01-1f4bd80fb68d.png)

Edited the Settings tab with two new features, "Minimize to system tray" (tick/untick) and "Launch tracker at startup" (ticl/untick) along with Save button.

![image](https://user-images.githubusercontent.com/19464321/140394652-f033a3b3-21a7-41d0-976e-2b20531f277f.png)

When the minimize to system tray option is selected, the black coloured plus sign gets added as below,

![image](https://user-images.githubusercontent.com/19464321/140403479-a9b362f3-a8cf-431c-b099-5f3d8b74df3f.png)

All the info about our application can be found out in newly added INFO tab.
  ![image](https://user-images.githubusercontent.com/19464321/139944383-42c2d554-dc54-4c80-84a8-58cb60fc2c68.png)



### Future Goals
- Collect the in-stock drop data and predict the next drop time.
- More supported retailers.
- [Other enhancements](https://github.com/ramyasaimullapudi/ItemStockTracker/issues)



### Questions?
If you encountered any questions and seeking for helps, please reach out to us at
<br/>[SEGroup16.2021@gmail.com](mailto:SEGroup16.2021@gmail.com)
<br/>Alternatively, you can contact any of the team members listed below.

### Team Members

[Arjun Madhusudan](mailto:amadhus2@ncsu.edu)</br>
[Ramya Sai Mullapudi](mailto:rmullap@ncsu.edu)</br>
[Lakshmi Swetha Gavini](mailto:lgavini@ncsu.edu)</br>
[Rohan Prabhune](mailto:rjprabhu@ncsu.edu)</br>
[Saurabh Krishna](mailto:kvankad@ncsu.edu)</br>

