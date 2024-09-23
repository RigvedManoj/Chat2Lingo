# Chat2Lingo

This application is used to convert conversation logs into audio with distinct voices for each individual.

## Requirements

- **Python 3**: Make sure Python 3 is installed on your system.
- **Required Libraries**: The following libraries are needed: (You can install these dependencies using the `requirements.txt` file.)
    - `pyttsx3`
    - `pydub`
    - `flask_ml`

## Setup Instructions

1. **Clone the Repository**:  
   Clone this repository to your local machine.
   ```bash
   git clone https://github.com/RigvedManoj/Chat2Lingo.git
   cd Chat2Lingo
   ```

2. **Create a Virtual Environment**:  
   Create a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   ```

3. **Activate a Virtual Environment**:

    On Windows:
    ```bash
   venv\Scripts\activate
   ```
   On MacOS/Linux:
   ```bash
   source venv/bin/activate 
   ```

4. **Install Dependencies**:  
    Install the required Python libraries.
   ```bash
   pip install -r requirements.txt
   ```

5. **Download FFMPEG**:

   This project also requires FFmpeg for audio processing. 
   You can install it by following the instructions found [here](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/).
   
6. **Run the Project**:

    Execute the provided shell script to start the server and run the client.

    _Note: Please execute this in git bash if running on Windows._
   ```bash
   cd src
   ./runSample.sh
   ```
7. **Run Project with CLI**:
   
   The project can also be run via command line. 
   Run the server.py file in a terminal and then run client.py with arguments in another terminal.
   ```bash
   python server.py &
   python client.py "Inputs/text1.txt" "Inputs/text2.txt"
   ```

## Additional Setup (Optional):
The pyttsx3 packages uses voices available in the operating system. Usually the number of voices available for english is 2.
Additional voices can be downloaded and installed via the below steps:
1. **Windows**:
    - Download Additional Voices: Visit Microsoft Speech Platform to download the Speech Platform and additional voice packs.
    - Install the Voice Pack: Run the downloaded installer(s) and follow the prompts to install.
    - Check out [here](https://puneet166.medium.com/how-to-added-more-speakers-and-voices-in-pyttsx3-offline-text-to-speech-812c83d14c13) for more detailed instructions.
2. **MACOS**:
    - Open System Preferences: Go to System Preferences > Accessibility > Speech.
    - Add Additional Voices: Click on the System Voice dropdown and select Manage Voices. 
    - Choose your desired voice(s) and click Download.
3. **LINUX**:
    - Open a terminal and run:
    ```bash
    sudo apt-get install espeak festival festvox-kallpc16k
   ```
    - Configure pyttsx3: Ensure you have the espeak engine available in pyttsx3.

**Verify Installation**:
```bash
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"ID: {voice.id}, Name: {voice.name}")
```

## Code Structure:

- text2audio.py : Contains the core function that parses text and converts to audio file.
- client.py : Contains client function to request server for text to audio conversion.
- server.py : Contains server function to get client requests, call text2audio and return results.
- runSample.sh : Runs server.py and runs client.py with an argument.
- Inputs : Directory containing input text files.
- Outputs : Directory containing output audio files corresponding to each text file.
