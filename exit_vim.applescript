set esc to 53 -- Key code of esc key

-- Get all terminal windows
tell application "System Events"
    set term_windows to name of windows of (application "Terminal")
end tell

-- Find vim window
set i to 1
repeat with window_name in term_windows
    if window_name contains " vim " then
        set vim_window to i
    end if
    set i to i + 1
end repeat

try
    tell application "System Events"
        -- Make vim window the frontmost window
        tell process "Terminal"
            perform action "AXRaise" of window vim_window
            set frontmost to true
        end tell

        -- Exit vim
        keystroke (key code esc)
        keystroke ":q!"
        keystroke return
    end tell
on error
    display dialog "No vim windows currently open."
end try
