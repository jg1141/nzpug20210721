#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Key:
; # Windows key
; ^ Control key
; + Shift key
; ! Alt key

; CONTROL SHIFT 1: Send string
^+1::Send {Raw}`%run "C:\\setup.py"

; CONTROL SHIFT 3: Send string
^+3::Send .copy`(`)!{enter}

; CONTROL SHIFT 5: Send string
^+5::Send pd.read_feather(){left}

; CONTROL SHIFT 7: Send string
^+7::Send `, sort_cols=True

; CONTROL SHIFT 8: Send string
^+8::Send .reset_index`(inplace=True, drop=True`)

; CONTROL SHIFT F8: Send string
^+F8::Send {left}{Backspace}{Backspace}{Backspace}{Backspace}{Backspace}{Backspace}{Backspace}{Backspace}{Backspace}{Backspace}{Backspace}!{Enter}

; CONTROL SHIFT 9: Send string
^+9::Send _ = [print`(item`) for item in sorted`(list`(df.columns`)`)]{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}

; CONTROL SHIFT [: Send string
^+[::Send [:2]!{enter}

; CONTROL SHIFT ]: Send string
^+]::Send .stb.freq`(`[''`]`){left}{left}{left}

; CONTROL SHIFT \: Send string
^+\::Send `[''`]{left}{left}

; CONTROL SHIFT .: Send string
^+.::Send {home}+{right}+{right}+{right}^c{end}{enter}^v

; CONTROL SHIFT /: Send string
^+/::Send {home}+{right}+{right}+{right}+{right}^c{end}{enter}^v

; CONTROL SHIFT A: Send string (rename AS)
^+a::Send .rename`(columns={{}'count':'_count'{}}`){left}{left}{left}{left}{left}{left}{left}{left}{left}
return

; CONTROL SHIFT D: Send string
^+d::Send {escape}b{enter}d(dir())!{enter}{up}^adf = {left}{left}{left}

; CONTROL SHIFT F: Add path/filename formula to Excel
^+f::
Send {Raw}=cell("filename")
Send {F9}
return

; CONTROL SHIFT g: Send string
^+g::Send fig{space}={space}px.bar`(df`,{space}x=df.columns[0]`,{space}y='count'`){enter}fig.update_layout`(title=title`,{enter}xaxis_title=''`,{enter}yaxis_title=''`){enter}fig.show`(`){escape}a{enter}title = t(""){left}{left}

; CONTROL SHIFT I: inplace=True
^+i::
Send {Raw}inplace=True
return

; CONTROL SHIFT k: Pivot (crosstab x)
^+k::Send .pivot`(index='' `, columns='' `, values=''`){left}{left}
return

; CONTROL SHIFT L: Send string
^+l::
Send .apply`(lambda row: row.`, axis=1){left}{left}{left}{left}{left}{left}{left}{left}{left}
return

; CONTROL SHIFT N: "NOW" types date as YYYYMMDD HHMM
^+n::
FormatTime, TimeString, Time, yyyyMMdd HHmm ''
Send %TimeString%
return

; CONTROL SHIFT Q: query
^+q::Send {end}query(){left}"""{enter}{left}SELECT * FROM{space} 
return

; CONTROL SHIFT R: "NOW" types date as YYYYMMDD HHMM - replacing existing
^+r::
FormatTime, TimeString, Time, yyyyMMdd HHmm ''
Send {Home}{Right}{Right}{Right}{Right}{Right}{Right}{Right}{Right}{Right}{Right}{Right}{Right}{Right}{Right}+{Home}^+n
return

; CONTROL SHIFT T: "TODAY" types date as YYYYMMDD
^+t::
FormatTime, TimeString, Time, yyyyMMdd
Send %TimeString%
return

; CONTROL SHIFT X: Output to_csv (for eXcel)
^+x::
Send .to_csv`("
FormatTime, TimeString, Time, yyyyMMdd
Send %TimeString%
Send {space}.csv"`, index=False`){left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}{left}
return

; CONTROL SHIFT z: Send string
^+z::Send e(start_time)^{Enter}
return