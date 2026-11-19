# MAW NPC Voices EN

The people of **Might and Magic 8 with the fan mod MAW** speak their lines out loud: greetings, answers, street
news and guards, in all three worlds (MM6, MM7, MM8) and in the additions of MAW. Male and female NPCs have
different voices.

> Want the game in German, with German voices? Use [MAW NPC Voices DE](https://github.com/slovi21/maw-npc-voices-de).

## Quick start

1. [Go to the download](https://github.com/slovi21/maw-npc-voices-en/releases/latest) and click
   `MAW-NPC-Voices-EN-…zip` under "Assets" (about 675 MB).
2. Close the game.
3. Unzip the file into your game folder (the folder with `MM8.exe`). Answer "Yes" if Windows asks to merge folders
   or replace files.
4. Start the game and talk to someone.

The mod only adds files. It changes no file of the game, of MMMerge or of MAW, and it does not touch your saved games.

## Which mod do I need?

| You want … | Use … |
|---|---|
| English texts with English voices | **this mod (EN)** |
| the game in German, with German voices | [MAW NPC Voices DE](https://github.com/slovi21/maw-npc-voices-de) |
| to switch between German and English in the game, both with voices | both mods; they work together |

**How the two mods differ:**

| | EN mod (this one) | DE mod |
|---|---|---|
| Who made the voices? | we did, with the free AI speech program Kokoro | NPC voices: we did, with the AI ElevenLabs; hero voices: the original German game |
| What does the installer create? | nothing, there is none | the parts taken from your German MM8 (original texts and hero voices), because we may not share them |
| Download | about 675 MB | about 430 MB |

## Requirements

* **Might and Magic 8 with MMMerge and MAW**, installed as the [MAW guide](https://github.com/Malekitsu/Maw-Mod-MMMerge)
  describes. The game must start and work. Nothing else is needed.
* **Your game folder** is the folder that holds `MM8.exe`. To find it: right-click the game's shortcut and choose
  "Open file location".

## What is in the package

Everything is ready to use, there is no installer:

* **8,502 recordings** in `Data\Voices\NPC`. They cover 3,803 of the 3,881 different dialog texts of the game,
  most of them in a male and a female voice. They were made with the free speech generator Kokoro-82M.
* **Three small lists** in `Data\Voices`: `names.tsv` and `pics.tsv` tell whether an NPC is a man or a woman
  (by name and portrait), `templates.tsv` handles texts with changing names or numbers.
* **One script**, `Scripts\General\zzzMaw_NPCVoices.lua`, which the game loads at start and which plays the voices.
* `MAW-NPC-Voices-EN-INSTALL.txt` (the guide) and `MAW-NPC-Voices-EN-LICENSE.txt` (terms of use).

When you talk to someone, the script finds the recording for the text on the screen and plays it with the voice that
fits the person. A text that a newer MAW version changed has no recording and stays silent, so you never hear a line
that does not match the text.

## Settings in the game

**Volume:** the voices follow the voice volume slider in the game's options.

**Keys:**

| Key | Action |
|---|---|
| F9 | plays the last line again. Press F9 again within 2 seconds for the line before it, and once more for the one before that. |
| F10 | stops the voice. Otherwise a long text keeps playing even after you have closed the conversation. |

**On / off:** this mod has no settings page of its own. If MAW NPC Voices DE is installed too, its page
"Sprache / Language" in the game options (page through MAW's extra pages with the arrows) has a line
"Voice output: on / off" that works at once. Without it, use `npcVoices = false` below.

**Advanced** (open `MAWSettings.lua` in the game folder with Notepad, add the line inside `return { … }`, then restart
the game):

| Line | Effect |
|---|---|
| `npcVoices = false,` | switches the voices off (default: on) |
| `npcVoiceVolume = 0.8,` | volume from 0.0 to 1.0, relative to the voice slider (default 1.0) |
| `repeatVoiceKey = 120,` | another key instead of F9 (the key codes are listed in `MAWSettings.lua`) |
| `stopVoiceKey = 121,` | another key instead of F10 |

If MAW's key settings page has two free places, the two keys appear there as "VOICE AGAIN" and "VOICE STOP" and are
set there instead. With MAW 4.5 there is no free place.

## What the mod changes in your game

| Part | Changed? |
|---|---|
| Original game | no |
| MMMerge | no |
| MAW, including `MAWSettings.lua` | no (only if you add one of the lines above yourself) |
| Saved games | no |

Everything else is new files (list under [Uninstall](#uninstall)). If MAW NPC Voices DE is installed too, the two mods
share three files; they are the same in both packages, so overwriting them does no harm. The German mod changes
`MAWSettings.lua`; this one does not.

## Uninstall

1. Delete `Data\Voices\NPC` and, in `Data\Voices`, the file `templates.tsv`.
2. Delete `MAW-NPC-Voices-EN-INSTALL.txt` and `MAW-NPC-Voices-EN-LICENSE.txt` in the game folder.
3. **Only if MAW NPC Voices DE is not installed:** also delete `Scripts\General\zzzMaw_NPCVoices.lua`,
   `Data\Voices\names.tsv`, `Data\Voices\pics.tsv` and `NPCVoicesLog.txt` in the game folder.

Nothing else was changed.

## If something does not work

* **No voice:** is the voice volume slider in the game options above zero? Did you add `npcVoices = false`?
  Does the folder `Data\Voices\NPC` exist in the game folder?
* **Some lines are silent:** texts that a newer MAW version changed, and a few texts with changing names or numbers,
  have no recording.
* **MAW's "Check game files" lists `zzzMaw_NPCVoices.lua` as "unknown":** that is expected, the voices are an add-on
  and not part of MAW. Do not delete the file.
* **Report a problem** on the [Issues](../../issues) page. Please attach `NPCVoicesLog.txt` from the game folder: it
  lists every dialog text as played or missing.

## Technical details

`Scripts/General/zzzMaw_NPCVoices.lua` computes a key (CRC32) from each dialog text the game is about to show and
plays `Data/Voices/NPC/<key>.ogg` with the game's own audio library (SoLoud). The recordings were generated with
[Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (voices af_heart and am_michael). The tools that extract the
texts and generate, check and pack the audio are in [Tools/Voice](Tools/Voice/README.md).
`SHA256SUMS.txt` on the download page lets you check that the zip arrived undamaged.

## License

See [LICENSE.txt](LICENSE.txt). Non-commercial fan project, not made or approved by the owners of Might and Magic.
MAW is made by Malekitsu; this add-on is not part of MAW.
