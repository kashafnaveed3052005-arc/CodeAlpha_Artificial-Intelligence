# AI Music Generation Using Markov Chains

An algorithmic music generation system built in Python using the **Music21** toolkit. This project parses standard Musical Instrument Digital Interface (MIDI) data, models melodic and harmonic structures using a probabilistic **Markov Chain architecture**, and synthesizes entirely new musical sequences into playable MIDI files.

---

## 🚀 Key Features

* **Automated Audio Parsing:** Leverages `music21` to extract single notes and chord arrays from multi-instrument MIDI tracks.
* **Algorithmic Modeling:** Uses a statistical Markov Chain approach to capture transitional frequencies between notes, guaranteeing stylistically coherent outputs without the extensive overhead of neural networks.
* **Robust Error Handling:** Features a dynamic file validator that filters out corrupted data or mislabeled zip archives (e.g., `b'PK\x03\x04'` structural mismatches).
* **Automatic Workspace Detection:** Programmatically resolves filesystem pathways (`os.path`) to eliminate execution directory crashes between standard shells and text editor runners like VS Code's Code Runner.

---

## 🛠️ System Architecture & Logic

The system operates across four primary pipeline stages:

1. **Preprocessing (Tokenization):** Quantizes and converts raw MIDI note arrays and chord streams into string representations.
2. **State Estimation (Learning):** Populates an adjacency dictionary representing statistical probabilities:
   
   $$P(X_{n+1} = x | X_n = x_n)$$

3. **Stochastic Synthesis (Generation):** Selects a randomized initialization seed from the source token set and walks 100 iterations forward based on state weight balances.
4. **Serialization (Output):** Re-encodes string mappings back into physical `music21.note.Note` and `music21.chord.Chord` objects at fixed step offsets, serializing the stream to disk.

---

## 📋 Prerequisites & Dependency Setup

Ensure you are utilizing Python 3.x (Fully optimized for Python 3.12+ environments). 

Install the required core NLP/Audio parsing dependency:
```bash
pip install music21