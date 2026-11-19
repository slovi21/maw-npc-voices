# MAW NPC Voices EN

Spoken NPC dialogs for **Might and Magic 8 with MMMerge and the MAW mod**, for all three worlds
**MM6, MM7 and MM8** and the additions of MAW.
About 8,500 recordings: greetings, topic answers, street news and the sayings of guards.
Male and female NPCs speak with different voices.

> A German edition with German texts and German voices is available as a separate mod:
> [MAW NPC Voices DE](https://github.com/slovi21/maw-npc-voices-de).

## Download

Get `MAW-NPC-Voices-EN-<version>.zip` (about 670 MB) from the [Releases](../../releases) page.
`SHA256SUMS.txt` next to it lets you check the download.

## Requirements

Might and Magic 8 (GOG) with MMMerge, the patch, Multiplayer and [MAW](https://github.com/Malekitsu/Maw-Mod-MMMerge),
installed as the MAW README describes. The game must start and work. Nothing else is needed.

## 1. What is in the package

Everything is in the download, ready to use:

* **8,502 recordings** in `Data\Voices\NPC`: 4,251 dialog texts from MM6, MM7, MM8 and MAW, each spoken by a
  male and by a female voice. Almost every NPC dialog of the game has a recording.
  They were generated with [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (voices af_heart and am_michael).
* **Three small lists** in `Data\Voices`: `names.tsv` and `pics.tsv` tell whether an NPC is a man or a woman
  (by name and by portrait), `templates.tsv` matches texts that contain a changing name or number.
* **One script**, `Scripts\General\zzzMaw_NPCVoices.lua`, which the game loads at start and which plays the voices.
* `MAW-NPC-Voices-EN-INSTALL.txt` and `MAW-NPC-Voices-EN-LICENSE.txt` (instructions and terms of use).

## 2. What happens when you install

There is no installer. Unzipping only adds the files above to your game folder. Nothing is generated,
nothing is downloaded, and no file of the game or of MAW is changed (not even `MAWSettings.lua`).

When you talk to an NPC, the script looks up the recording for the text on the screen and plays it with the voice
that fits the NPC (male or female). A text that a newer MAW version changed has no recording and stays silent,
so you never hear a line that does not match the text.

## Which files are changed

| Part | Changed? |
|---|---|
| **Original game** (Might and Magic 8) | No. |
| **MMMerge** (patch, Multiplayer, `mmmerge.T.lod`, tables, scripts) | No. |
| **MAW** (scripts, data, `MAWSettings.lua`) | No. `MAWSettings.lua` changes only if you add one of the lines under "Advanced" yourself. |

Everything the mod brings is **new files** that did not exist before:

* `Scripts\General\zzzMaw_NPCVoices.lua`
* `Data\Voices\NPC\` (the recordings) and `names.tsv`, `pics.tsv`, `templates.tsv` in `Data\Voices`
* `MAW-NPC-Voices-EN-INSTALL.txt`, `MAW-NPC-Voices-EN-LICENSE.txt`
* while playing: `NPCVoicesLog.txt` in the game folder

If MAW NPC Voices DE is installed too, both mods share `zzzMaw_NPCVoices.lua`, `names.tsv` and `pics.tsv`.
The files are the same in both packages, so overwriting does no harm.
We checked this: after installing both mods, the only changed file in the whole game folder was `MAWSettings.lua`,
and the German edition's installer made that change.

## Install

1. Close the game.
2. Unzip the download into the game folder (the folder with `MM8.exe`). Allow merging folders.
3. Start the game and talk to an NPC.

Details and uninstall: [INSTALL.txt](INSTALL.txt).

## Settings in the game

**Volume:** the voices follow the game's voice volume slider in the game options.

**Keys:**

| Key | Action |
|---|---|
| F9 | repeat the last voice (press again within 2 s for the ones before, up to three times) |
| F10 | stop the voice |

**On / off:** this mod has no settings page of its own. If MAW NPC Voices DE is installed too, its page
"Sprache / Language" (in the game options, page through MAW's extra pages with the arrows) has a line
"Voice output: on / off" that works at once.

**Advanced:** add any of these lines inside `return { ... }` in `MAWSettings.lua` in the game folder:

| Line | Effect |
|---|---|
| `npcVoices = false,` | switches the voices off (default: on) |
| `npcVoiceVolume = 0.8,` | 0.0 to 1.0, relative to the voice slider (default: 1.0) |
| `repeatVoiceKey = 120,` | key code for "repeat" (default 120 = F9; the codes are listed in `MAWSettings.lua`) |
| `stopVoiceKey = 121,` | key code for "stop" (default 121 = F10) |

Restart the game after changing `MAWSettings.lua`.

## How it works (technical)

`Scripts/General/zzzMaw_NPCVoices.lua` computes a key (CRC32) from each dialog text the game is about to show
and plays `Data/Voices/NPC/<key>.ogg` with the game's own audio library (SoLoud).
The tools that extract the texts and generate, check and pack the audio are in [Tools/Voice](Tools/Voice/README.md).

## License

See [LICENSE.txt](LICENSE.txt). Non-commercial fan project, not made or approved by the owners of Might and Magic.
MAW is made by Malekitsu; this add-on is not part of MAW.
