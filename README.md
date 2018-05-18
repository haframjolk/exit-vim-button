## Summary
You know the saying: Once you start using Vim, it's hard to quit. Well, that's exactly what this project aims to address. It's a button whose sole purpose is to exit Vim running in the native macOS Terminal app. This project does not require an Arduino board with keyboard command support.

## Requirements
* Arduino board (I used an Arduino Uno R3)
* A pushbutton connected to the Arduino
* A Mac

## Installation
### Dependencies
The Exit Vim Button's input handler requires Python 3 and the pySerial module.

If you have Homebrew, install them with the following commands:
```bash
brew install python
pip install pyserial
```

In order to upload the Arduino sketch to your board you need the Arduino IDE.

It can be installed with the following command:
```bash
brew cask install arduino
```

### Setup
Clone the repository to your computer with the following command:
```bash
git clone https://github.com/reyniraron/exit-vim-button.git
```

Connect your Arduino to your Mac and start up the Arduino IDE. You may have to configure your board type and serial port. Open the *exit_vim_button.ino* sketch inside the *Arduino/exit_vim_button* directory. Change the **BUTTON** and **ACTIVE** constants to match your setup. **BUTTON** is the number of the pin your button is attached to, and **ACTIVE** is either *HIGH* or *LOW* depending on how your button is wired. After you've done this, upload the sketch to your board.

Open *input_handler.py* in your favorite text editor and change the **serial_port** variable to match the serial port of your Arduino. You can find it in the Arduino IDE by opening the *Tools* menu and hovering over *Port*. If your board is connected via USB, it will most likely start with */dev/cu.usbmodem*.

### Granting assistive access
In order for the Exit Vim Button to work, you need to grant your Terminal application access to control your computer. Open *System Preferences*, click on the *Security & Privacy* pane and select the *Privacy* tab. Select *Accessibility* in the left sidebar and click the padlock on the bottom if it is locked. Authenticate with your username and password. Now, click the plus (+) icon and navigate to */Applications/Utilities/* and select Terminal. Hit *Open*. Now you should be good to go.

## Usage
Open a command line and `cd` into the repository you cloned. Run the input handler by typing the following:
```bash
./input_handler.py
```

If you followed this guide properly your Exit Vim Button should be working. Try opening Vim in a Terminal window and hitting the button. It should automatically activate the window and type the keystroke to quit. Note that the button quits without saving your work. It can be changed by modifying the keystroke in *exit_vim.applescript* and compiling that file to *exit_vim.scpt*.

In order to stop the input handler, simply press <kbd>CTRL</kbd>+<kbd>C</kbd> inside the Terminal window.

## License
This project is licensed under the MIT License. See repository LICENSE file for more details.
