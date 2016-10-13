-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                K-Shoot MANIA                
                                             
                          Author: masaka     
                     Translation: hakui      
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

●About●
  A music game for Windows that involves hitting keys in tandem with the music in order to add sound effects.

●Environment●
  This software requires a graphics card that supports DirectX8 or later.
  To use VSync, a graphics card that supports DirectX9 or later is required.
  (VSync is optional and can be configured in the options.)
  The DirectX runtime can be downloaded from the Microsoft Corporation website.

●Operation Guide● (During default settings)

  ◇Title Screen
       ↑,↓    … Choose menu item
       Enter    … Confirm selection

  ◇Song Selection (With default key config)
       ↑,↓    … Choose song
       ←,→    … Choose difficulty
       Enter    … Open folder/Play song
    Hold Enter … Add/remove song from Favorites
        F11     … Autoplay song
     Shift+F11  … Autoplay the folder starting from the current song
      S,D,K,L   … Show various options (Change options using arrow keys)
    D+K+無変換  … Change player（To make a new player record, make a new
      (or 変換)    folder in the "score" folder.）
        Esc     … Close folder/Return to title screen

  ◇During Play（With default key config）
      S,D,K,L   … Hit BT (white) objects （H,J,F,G are also mapped to the BT objects）
    無変換,変換 … Hit FX (orange) objects (If you're reading this, your keyboard
                   probably doesn't have the 無変換 and 変換 keys. Go change it.)
       Space    … Hit both FX objects
        Q,W     … Match LEFT LASER (blue) objects
        O,P     … Match RIGHT LASER (red) objects
       ↑,↓    … Adjust hi-speed value
       ←,→    … Adjust hi-speed type
    Ctrl+Enter  … Pause
      Ctrl+→   … Fast forward
        Esc     … Quit song

  ◇Results
    Enter or Esc … Return to song selection

  ◇Option Menu
    ↑,↓,←,→ … Select/change option
       Enter    … Confirm
        Esc     … Back

  ◇INPUT GATE
    ↑,↓,←,→ … Select song
      S,D,K,L   … Check current song
       Enter    … Download all checked songs
    無変換+変換 … Options/Filter song list
        Esc     … Return to title screen
                  (If pressed while songs are still downloading, download will be stopped. All songs
                    that have finished downloading will be inputted.)


●About Hi-speed●
  Hi-speed allows you to adjust the speed of the notes to your liking.
  The different types of hi-speed are as follows:

  ・x0.5 ～ x9.9 … Speed is a multiple of the BPM.
  ・  25 ～ 2000 … Set the mode BPM to this speed (mode based on number of measures).
  ---The following types are not available by default (Enable them in the options)---
  ・ C25 ～ C2000 … Constant speed (even in songs with changing BPMs).
  ・ m25 ～ m2000 … Sets the max BPM to this speed.
  ・ a25 ～ a2000 … Sets the mean BPM to this speed (mean based on duration).

  ※C-speeds will ignore pauses in the chart as well.


●Key Configuration●
  By going to OPTION→Key Configuration, you can change the key bindings for the game.

  To map a button to more than one key, please go to KEYBOARD2 at the bottom of the menu.
  Keys mapped to the same button in KEYBOARD1/KEYBOARD2 will trigger that button when either is pressed.
  For example、when BT-A is mapped to S in KEYBOARD1 and H in KEYBOARD2、pressing either key during play
  will trigger BT-A.
  (Same with GAMEPAD1 and GAMEPAD2.)

  Pressing Space when a button is selected (without pressing Enter) will clear the mapping for that key.

  When changing key mappings, please make sure there aren't any conflicts. (Conflicts will show up in red.)


●Terms of Use●
  - Redistribution or appropriation of the software and its files (including the program, texts, sounds, images)
    are forbidden.
  - The included songs (including those available in the INPUT GATE) and its associated media (eg. jacket illustrations)
    are the property of the content creators. Using them outside of this software without prior permission is forbidden.
  - Distribution of chart data/packs for use with this software that infringes on third-party rights are forbidden. Also, the
    software author does not accept any responsibility for user-uploaded content.
  - Screenshots or video (including streams) showing use of this software that infringes on third-party rights
    are forbidden.
  - Using this software to create content that uses illegally obtained sound or other forms of data, or the playback
    of such content, is forbidden.
  - The software author is not responsible and is not liable for any damages, direct or indirect, that might arise from
    using this software.
  - With regards to these points in this section across different languages of the readme file, the Japanese version takes
    precedence.


●FAQ for K-Shoot MANIA●

  Q: How do you read "けーしゅーまにあ"?
  A: "K-Shoot MANIA".

  Q: Can you hit cross-handed BT objects with the default key config?
  A: Yes.
     For example the BT object in lane 3 is mapped to F, and lane 4 is mapped to G. You can hit all 4 BT objects
    just with your left hand.
     (H and J for lanes 1 and 2, for the right hand.)
     By configuring KEYBOARD2 in the key configuration, it's possible to do cross-handed play.

  Q: After changing my key configuration, pressing one key triggers more than one button.
  A: There might be a conflict in KEYBOARD2. Please check it under Key Configuration, at the bottom. (Conflicting
    mappings will show up in red.)

  Q: I want to autoplay just the LASERs.
  A: In the song selection screen, press S (or BT-A) to bring up the options for each object (on/off/auto/hide).
     You can change it with the arrow keys.

  Q: Pressing multiple keys doesn't register.
  A: It's a keyboard issue, especially with USB keyboards.
     Changing the key configuration to one that doesn't jam should solve the problem.
    (For example, in my case my USB keyboard has the following: BT:D,F,L,; [KEYBOARD2:J,K,G,H]  
     FX:Space,変換  LASER:W,E P,@. This configuration doesn't jam.)
     The only way to completely solve this problem is to use a gaming keyboard or a controller.

  Q: Can I use a gamepad or a controller?
  A: Yes. Under OPTION → Key Configuration, there are mappings for GAMEPAD 1 and GAMEPAD2 that you can set.
     There are two different ways to map LASER input, listed below.

  Q: Can I map LASER input using PowerMate (a type of USB knob)?
  A: Yes. Firstly, please set the key bindings on the PowerMate software itself. (Map it to the key listed in KEYBOARD1.)
     Under OPTION→Input/Judgement Settings, change INPUT TYPE OF LASER OBJECT to Repeat key (for PowerMate).
    ※ Using this method is not recommended due to the poor latency.
       Also, a high spec PC is needed for PowerMate to run smoothly.

  Q: Can I map LASER input using analog sticks?
  A: Yes. Under OPTION→Input/Judgement Settings,  change INPUT TYPE OF LASER OBJECT to Analog stick.

  Q: I'm using a controller. The LASER cursor moves too fast/slow.
  A: Under OPTION→Input/Judgement Settings, change the value of SLIDER/MOUSE SIGNAL SENSITIVITY.
     Please note that there is no way to change the sensitivity for keyboard/PowerMate/analog stick input.

  Q: My LASER keys are being mapped to the LASER on the opposite side.
  A: Under OPTION→Input/Judgement Settings, you can toggle SWITCHING L/R LASER.

  Q: The judgement timing's off for all the songs.
  A: Under OPTION→Input/Judgement Settings, you can change the value for TIMING ADJUST.

  Q: What's Auto Sync?
  A: It fixes the timing for BT/FX short objects for a song, usually used during chart creation. Please note that the
    adjustments are saved according to each difficulty level. If the timing for all the songs are off, please use 
    TIMING ADJUST under OPTION→Input/Judgement Settings instead.

  Q: How do I play song packs released on the internet?
  A: Make a new folder in the songs folder (name doesn't matter). Unzip the contents into that folder. The folder will
     appear in the song selection screen.
    (You can put them in the K-Shoot MANIA folder if you want, but having a large number of songs increases loading
     time and also the chance of song names clashing, so making a new folder is still recommended.)

  Q: Is it okay to upload screenshots to the Internet?
  A: If it's a screenshot, it's okay. However, the game's image data uploaded as-is is forbidden as it is 
    considered a redistribution of the game files, listed under "Terms of Use".


●FAQ for chart creation●

  Q: How do I add the effects to the song?
  A: The procedures are listed in the link below.
     -> http://kshoot.client.jp/tutorial.html (Japanese)

  Q: How do I add BPM changes?
  A: With the pencil tool in position mode, click on the position that you want to add a change to.
     To remove the change, right click the change in that mode, or click with the eraser tool in position mode.

  Q: How do I add a time signature change?
  A: With the pencil tool in position mode, Ctrl+click on the position that you want to add a change to.
     You can only change the time signature at the start of a measure. Also, the denominator is capped at 192.
     To remove the change, right click the change in that mode, or Ctrl+click with the eraser tool in position mode.

  Q: I can't delete some of the notes.
  A: This has to do with the quantization of the notes eg. you can only remove 1/16th notes while in 1/16th mode.
     However, if you Shift+right click using the pencil tool, you can clear notes over a range ie. in the 1/4th mode, Shift+
    right clicking will remove all the notes in that 1/4th range. If you find yourself unable to delete some notes, you can
    try that option.

  Q: I added long FX notes, but they still aren't effected.
  A: There are many different types of FX effects, so each note's effect has to be specified. With the pencil tool in
    long FX mode, Ctrl-clicking the FX object lets you specify the note's effect.

  Q: How do I use the Retrigger effect for long FX notes?
  A: Retrigger basically repeats the selection with a 2 beat delay. For that reason, Retrigger is usually placed starting at
    the halfway mark. For example, if a effect like "te-te-tetetete" is desired, you'd put a Re8 at the halfway mark, then
    a Re16 three quarters of the way through.

  Q: How do I make the LASERs go out of the lane?
  A: LASER objects come in normal and wide range types. Holding down Ctrl+Shift while inserting a LASER object will
    cause a wide range LASER to be inserted. In wide range mode, the LASER object has twice the width of a normal
    one and can go out of the lane. In the editor, wide range LASERs start with a white marker.
     The sound effects for wide range LASERs are calculated based on its normal counterpart's position.

  Q: Can I make a normal LASER object a wide-range one midway through the note?
  A: No. Each LASER can only have one type, so it cannot be changed midway.

  Q: How do I change the volume of the LASER slam sound effects?
  A: With the pencil tool in LASER slam sound volume/sample mode, click on the slam you want to adjust the volume for.
     Accepted values are between 0 and 100.
     The effect sounds tend to be more on the loud side, so putting lower values is recommended.
     To remove the change, right click the change in that mode, or click with the eraser tool in position mode.

  Q: Please tell me more about the different slam sound samples.
  A: To change the sample used for a slam, with the pencil tool in LASER slam sound volume/sample mode, Ctrl+click
    the slam you want to change. Slams without a sample specified will use the Default sound.
    The five types of sound samples are as follows:
      ○Default … A plosive sound effect.
      ○ Down   … A descending sound effect. Intended for use after a fast moving LASER.
      ○  Up    … An ascending sound effect. Intended for use after a fast moving LASER.
      ○ Swing  … A sound similar to swinging a bat.
      ○ Mute   … No sound.
    Default is suitable for most cases. For the other samples, it's recommended to use them when appropriate.

  Q: Please tell me more about the different types of filters.
  A: To change the sound filter, with the pencil tool in LASER sound effects gain/type mode, Ctrl+click the laser.
    The three types of sound filters are as follows:
      ○Peaking filter(PEAK)    … Normal filter. Increases specific frequencies.
      ○High-pass filter(HPF)   … Removes sound below a certain frequency.
      ○Low-pass filter(LPF)    … Removes sound above a certain frequency.
                                   (ie. isolates certain sounds.)
      ○BitCrusher(BITC)        … Roughens the bits of the sound, making it sound like an old radio.
    Peaking filter is suitable for most cases. For the other filters, it's recommended to use them when appropriate.
    To produce a more natural effect、the cutoff frequency is increased when Peaking filter is used along with the
    High-pass filter or Low-pass filter. Like the Peaking filter, this amplification can be changed via the LASER sound
   effects gain mode.
    The Peaking filter delay option can only be used when a Peaking filter is selected.

  Q: LASER sound effects are not being applied on both sides of the lane where they usually enter.
  A: LASER sound effects are calculated based on the maximum displacement of both lasers. Hence, for example, if the
    left (blue) LASER is touching the right side of the lane, there will be no change in sound effects regardless of the
    movement of the right (red) LASER. This is a feature, not a bug. Currently there are no plans to change this.

  Q: Please tell me more about the different lane tilt effects.
  A: Via different lane tilt effects, you can change the tilt angle caused by a LASER object.
    The six types of lane tilt effects are as follows:
      ○NORMAL        … Normal tilt angle.
      ○BIGGER        … More tilt than normal.
      ○BIGGEST       … Way more tilt than normal.
      ○KEEP(NORMAL)  … Set the tilt at that position to be the minimum angle (with NORMAL tilt).
      ○KEEP(BIGGER)  … Set the tilt at that position to be the minimum angle (with BIGGER tilt).
      ○KEEP(BIGGEST) … Set the tilt at that position to be the minimum angle (with BIGGEST tilt).
      ○ZERO          … No tilt.

  Q: How do I keep a part of the chart from tilting?
  A: By setting the lane tilt effect to ZERO, you can keep the lane from tilting.
     Using the pencil tool in the Lane tilt effect type mode, click on the start of the part which you want to prevent
    tilting, and select ZERO. Then, click on the end of the part and select NORMAL. The part between those two
    settings will have no tilt.

  Q: Lane spin effects are not showing up.
  A: Lane spins must be placed at the same position as a LASER slam. Please note that if the spin direction is different
    from the slam direction, the spin will not happen either. When inserting a spin, clicking on the left or right side of the
    lane will affect the spin direction. For spins that are already inserted, you can change the direction by selecting it
    and pressing Ctrl+← or Ctrl+→. For example, for a slam that goes from left to right, the spin that goes with it is
    shown with an arrow going from bottom left to top right (and a counterclockwise mark).

  Q: Please tell me more about the lane swing effect.
  A: The swing effect swings the lane sideways. Like the spin effect, it must be paired with a LASER slam. To add a
    swing effect, use the pencil tool in the Lane spin effect mode. Click to add a lane spin, then Ctrl+click the spin twice
    to change it into a swing effect. Like the spin effect, it must match the position and direction of the LASER slam.
     To change the settings for the swing effect, Ctrl+Shift+click the swing in that mode. You can change the amplitude,
    frequency, and the decay of the swing.

  Q: Pauses in the chart are not showing up.
  A: Your hi-speed might be set to a C-speed (C25～C2000). C-speeds always show the notes at a constant speed, so
    chart pauses would be ignored. Try choosing a different hi-speed option.

  Q: I want to know how off the chart timing is compared to the song.
  A: Pressing FX-L in the results screen will show the average timing difference between your play and the chart
    (timing based off the short objects only). Play the song again, and adjust the timing with Ctrl+Alt+←/→ (5ms jump)
    or Ctrl+Alt+Shift+←/→ (1ms jump). After adjusting the timing to match the difference, press Esc to save the timing
    adjustment into the chart.
     For higher precision, after processing the song through REAPER, compare the waveforms with the measures. If
    differences exist, drag to align them. This is the recommended method. (For details please check the tutorial on the
    website.)
    AUTO SYNC is also a viable option for solving this problem.

  Q: I want to know the weightage for the gauge (EFFECTIVE RATE).
  A: Pressing FX-R in the results screen will show the TOTAL value (the total gauge percentage increase if all notes had
    CRITICAL timing). You can change the TOTAL value manually under Edit→Chart metadata - Detail. Values between
    0 and 100 noninclusive will be ignored. Also, if the TOTAL value is set to 0 (Auto), it tends to assign a large value for
    very easy or very difficult charts.
     The HARD gauge is not affected by the TOTAL value.

  Q: I accidentally overwrote a file. Can I get it back?
  A: The last overwritten file is saved as backup.bak, in the same folder as the editor.
     Changing the file extension back to .ksh will let you read it in the editor.
    (Sometimes the file extensions aren't visible. In that case, go to Control Panel→Folder Options and uncheck "Hide
    extensions for known file types" under the View tab.)

  Q: Is it okay to post self-created charts?
  A: It's okay if it does not contain anything that infringes on property rights. Charts that contain data that infringes
    third-party rights are forbidden under "Terms of Use".

  Q: Is it okay to upload videos of self-created charts onto video hosting sites?
  A: It's okay if it does not contain anything that infringes on property rights. Videos of this software that contains
    media that infringes third-party rights are forbidden under "Terms of Use".

  Q: Is it okay to post videos of this software onto video sharing sites?
  A: It's okay if it does not contain anything that infringes on property rights. Videos (including streams) of this software
    that contains media that infringes third-party rights are forbidden under "Terms of Use".


●Licenses●
　libvorbis  Copyright (c) 2002-2008 Xiph.org Foundation
　libogg  Copyright (c) 2002, Xiph.org Foundation
　mpglib  Copyright (c) 2004  Michael Hipp
　BASS  Copyright (c) 2003-2013 un4seen developments

  OpenHSP Copyright (c) 1997-2012, Onion Software/onitama.
  NKF Copyright (C) 1987, FUJITSU LTD. (I.Ichikawa).
  NKF Copyright (C) 1996-2009, The nkf Project.
  cJSON Copyright (c) 2009 Dave Gamble

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.