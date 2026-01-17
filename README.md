# RIME-Config-Quick5

A RIME configuration for typing Quick5 (速成) efficiently.

## Overview

This configuration enables **continuous Quick5 typing** (“速成連打”), allowing you to type words and phrases fluidly without selecting individual characters after each code. It also supports both **English (US)** and **German (DE)** keyboard layouts and extends Quick5 typing to cover **Japanese Kokuji**, **Korean Gukja**, and **Vietnamese Chữ Nôm** characters.

## Installation

To use this configuration:

1. Install a [RIME](https://github.com/rime) version that fits your operating system.

2. Clone or download this repository.

3. Copy the contents of the [`./config`](config) directory into RIME’s user configuration folder:
    - On macOS: `~/Library/Rime/`
    - On Windows: `C:\Users\<your-username>\AppData\Roaming\Rime`

4. Launch RIME’s settings menu and select “Deploy” to apply the configuration.

## Features

- **Continuous Typing (“速成連打”)**
  Unlike traditional Quick5 setups where you must confirm each character individually, this configuration supports uninterrupted typing—words and phrases are automatically composed as you type.

    <img width="50%" src="./assets/screenshot_1.png">

- **Multi-Language Keyboard Support**
  Supports **English (US)** and **German** layouts (affecting punctuation only, not the Quick5 arrangement). Switch via `F4`: select `英鍵速成` for US or `德鍵速成` for German keyboards.

    <img width="50%" src="./assets/screenshot_2.png">

- **Extended Character Support**
  Most Chinese characters are supported, as well as many Japanese Kokuji, Korean Gukja, and Vietnamese Chữ Nôm can be typed out using Quick5.

    <img width="50%" src="./assets/screenshot_3.png">

- **Additional Scripts**
  Japanese Kana, Korean Hangul, Bopomofo, and Greek letters can be typed using the symbol hotkey `符`.

    <img width="50%" src="./assets/screenshot_4.png">

- **Emoji Suggestions**
  Type emojis easily using Chinese keywords. Powered by [rime-emoji](https://github.com/drsmile1001/rime-emoji).

    <img width="50%" src="./assets/screenshot_5.png">

- **Character Conversion**
  Easily toggle conversion to Simplified Chinese or Japanese Shinjitai via the `F4` menu.

    <img width="50%" src="./assets/screenshot_6.png">
