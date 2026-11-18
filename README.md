# MAW NPC Voices

Spoken NPC dialogs for **Might and Magic 8 with MMMerge and the MAW mod**.
About 8,500 recordings: greetings, topic answers, street news and the sayings of guards, for MM6, MM7, MM8 and MAW.
Male and female NPCs speak with different voices.

> A German edition with German texts and German voices is available as a separate mod:
> [MAW NPC Voices Deutsch](https://github.com/slovi21/maw-npc-voices-deutsch).

## Download

Get `MAW-NPC-Voices-<version>.zip` (about 670 MB) from the [Releases](../../releases) page.
`SHA256SUMS.txt` next to it lets you check the download.

## Requirements

Might and Magic 8 (GOG) with MMMerge, the patch, Multiplayer and [MAW](https://github.com/Malekitsu/Maw-Mod-MMMerge),
installed as the MAW README describes. The game must start and work.

## Install

1. Close the game.
2. Unzip the download into the game folder (the folder with `MM8.exe`). Allow merging folders.
3. Start the game and talk to an NPC.

The mod changes no MAW file. Details, settings and uninstall: [INSTALL.txt](INSTALL.txt).

| Key | Action |
|---|---|
| F9 | repeat the last voice (press again within 2 s for the ones before) |
| F10 | stop the voice |

## How it works

`Scripts/General/zzzMaw_NPCVoices.lua` computes a key (CRC32) from each dialog text the game is about to show
and plays `Data/Voices/NPC/<key>.ogg` with the game's own audio library (SoLoud). A text that a newer MAW
version changed has no recording and stays silent instead of playing a wrong line.

The recordings were generated locally with [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M).
The tools that extract the texts and generate, check and pack the audio are in [Tools/Voice](Tools/Voice/README.md).

## License

See [LICENSE.txt](LICENSE.txt). Non-commercial fan project, not made or approved by the owners of Might and Magic.
MAW is made by Malekitsu; this add-on is not part of MAW.
