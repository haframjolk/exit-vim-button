set esc to 53 -- Key code of esc key
tell application "Terminal"
    activate
    delay 0.25
    tell application "System Events"
        keystroke (key code esc)
        keystroke ":q!"
        keystroke return
    end tell
end tell
