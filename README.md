# MiDiff: MIDI-Conditioned Diffusion Models for Drum Audio Enhancement

This repository contains the research page for our study on the efficacy of diffusion models for audio denoising, comparing a baseline diffusion model with an enhanced model incorporating Connectionist Temporal Classification (CTC) loss.

## 🔗 Live Demo

Visit the live research page: [https://eladaspis.github.io/paper_page](https://eladaspis.github.io/paper_page)

## 📋 Abstract

This study presents a novel approach to drum audio enhancement using MIDI-conditioned diffusion models. We leverage symbolic musical information from MIDI data to guide the denoising process, enabling the model to make musically informed decisions about which audio components to preserve, enhance, or suppress. The conditioning mechanism uses Feature-wise Linear Modulation (FiLM) to incorporate MIDI embeddings throughout the diffusion U-Net architecture.

## ✨ Features

- **Interactive Audio Samples**: Compare clean, noisy, and denoised audio across different training epochs
- **Real-time MIDI Piano Roll Visualization**: Canvas-based interactive MIDI visualization with drum labels
  - 9 drum classes with color-coded notes
  - Velocity-based brightness and transparency
  - Synchronized playback with audio samples
  - Real-time cursor tracking
- **Static Spectrogram Visualizations**: High-quality spectrograms for clean and noisy audio
  - Generated using librosa with 480×360px resolution
  - Magma colormap for clear frequency representation
  - 2.5s middle section for optimal comparison
- **Interactive Charts**: Dynamic Frechet VGGish Score comparison using Chart.js
- **Responsive Design**: Mobile-friendly layout using Bulma CSS framework
- **Mathematical Notation**: MathJax integration for displaying equations (FiLM formulas)

## 📊 Results

The quantitative results show that the CTC Loss-Improved model achieves a consistently lower Frechet VGGish Score, indicating closer statistical similarity to clean audio. The MIDI-conditioned model with CTC loss demonstrates superior preservation of rhythmic structure and drum timbre compared to baseline models.

## 🎵 Audio Samples

The page includes:
- **Reference Audio**: Clean original and noisy input samples with static spectrograms
- **MIDI Reference**: Interactive piano roll visualization with playback controls
  - Drum labels for 9 drum classes (Bass, Snare, Hi-hats, Toms, Cymbals)
  - Color-coded notes with velocity dynamics
  - Synchronized scrolling with playback
- **Model Outputs**: Baseline and CTC-enhanced model outputs at epochs 0, 10, and 20
- **Interactive Controls**: Synchronized audio playback with spectrogram visualization

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3 (Bulma), JavaScript
- **MIDI Visualization**: 
  - Tone.js (@tonejs/midi) for MIDI parsing
  - html-midi-player for playback controls
  - Custom canvas rendering for piano roll
- **Audio Spectrograms**: 
  - Python (librosa, matplotlib) for static spectrogram generation
  - PIL for image processing
- **Charts**: Chart.js for interactive data visualization
- **Math Rendering**: MathJax for LaTeX equation display
- **Hosting**: GitHub Pages

## 🚀 Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/eladaspis/paper_page.git
   cd paper_page
   ```

2. Serve the files using a local HTTP server:
   ```bash
   # Using Python 3
   python3 -m http.server 8000
   
   # Using Node.js (if you have http-server installed)
   npx http-server
   ```

3. Open your browser and navigate to `http://localhost:8000`

## 📁 Project Structure

```
├── index.html                     # Main research page
├── generate_spectrograms.py       # Python script for generating spectrograms
├── static/
│   ├── css/                      # Stylesheets (Bulma + custom)
│   ├── js/                       # JavaScript libraries
│   ├── images/                   # Images, figures, and spectrograms
│   │   ├── spec_clean.png       # Clean audio spectrogram
│   │   ├── spec_noisy.png       # Noisy audio spectrogram
│   │   └── overview.PNG         # Architecture overview
│   ├── figures/                  # Architecture diagrams
│   │   ├── MidiConditioned.png
│   ├── baseline_model/           # Baseline model audio outputs
│   ├── ctc_loss/                # CTC model audio outputs
│   ├── 1_funk-groove1_138_beat_4-4.mid  # MIDI reference file
│   └── clean_10_soul-groove10_102_4-4_bluebird.wav  # Clean audio reference
└── README.md
```

## 📄 Citation

If you use this work in your research, please cite:

```bibtex
@misc{aspis2025diffusion,
  title={MiDiff: MIDI-Conditioned Diffusion Models for Drum Audio Enhancement},
  author={Elad Aspis},
  year={2025},
  institution={Bar Ilan University},
  url={https://eladaspis.github.io/paper_page}
}
```

## 📧 Contact

**Elad Aspis**  
Bar Ilan University  
[Your Email]

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
