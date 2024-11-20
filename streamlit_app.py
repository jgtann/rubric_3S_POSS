import streamlit as st
import streamlit.components.v1 as components

# Save the HTML content as a string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Phoneme Visualization</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      margin: 0;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .container {
      width: 90%;
      max-width: 800px;
      text-align: left;
      line-height: 1.6;
    }

    h1 {
      color: #333;
      text-align: center;
    }

    p {
      color: #666;
      font-size: 1rem;
      text-align: center;
    }

    .word-block {
      display: inline-block;
      margin-right: 15px;
      margin-bottom: 20px;
      text-align: center;
    }

    .word-title {
      font-size: 1.2rem;
      font-weight: bold;
      color: #333;
    }

    .phonemes {
      display: flex;
      gap: 5px;
      justify-content: center;
      margin-top: 5px;
    }

    .phoneme {
      padding: 5px 10px;
      border-radius: 5px;
      font-size: 1rem;
      font-weight: bold;
      text-align: center;
    }

    .text {
      margin-top: 20px;
      font-size: 1.2rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Phoneme Visualization</h1>
    <p>The 100 most common English words, with their phonemes visualized below in unique colors.</p>
    <div id="text-container"></div>
  </div>
  <script>
    const words = [
      "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
      "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
      "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
      "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
      "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
      "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
      "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
      "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
      "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
      "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
    ];

    const phonemeMap = {
      "a": "#ff5733", "b": "#33ff57", "c": "#3357ff", "d": "#ff33a1",
      "e": "#33fff7", "f": "#ff9e33", "g": "#57ff33", "h": "#5733ff",
      "i": "#ff3333", "j": "#33ff9e", "k": "#3357a1", "l": "#ffa133",
      "m": "#5733a1", "n": "#57a1ff", "o": "#a1ff33", "p": "#a15733",
      "q": "#33a1ff", "r": "#ff3357", "s": "#a1ff57", "t": "#ff5733",
      "u": "#ff33ff", "v": "#57ffaa", "w": "#33aaff", "x": "#ffaa33",
      "y": "#aaff57", "z": "#ffaaff"
    };

    function getPhonemes(word) {
      return word.split("").map(letter => ({
        letter: letter.toLowerCase(),
        color: phonemeMap[letter.toLowerCase()] || "#cccccc"
      }));
    }

    const textContainer = document.getElementById("text-container");
    words.forEach(word => {
      const wordBlock = document.createElement("div");
      wordBlock.className = "word-block";

      const wordTitle = document.createElement("div");
      wordTitle.className = "word-title";
      wordTitle.textContent = word;
      wordBlock.appendChild(wordTitle);

      const phonemesDiv = document.createElement("div");
      phonemesDiv.className = "phonemes";

      const phonemes = getPhonemes(word);
      phonemes.forEach(phoneme => {
        const phonemeElement = document.createElement("div");
        phonemeElement.className = "phoneme";
        phonemeElement.textContent = phoneme.letter;
        phonemeElement.style.backgroundColor = phoneme.color;
        phonemeElement.style.color = "#000"; // Ensure contrast
        phonemesDiv.appendChild(phonemeElement);
      });

      wordBlock.appendChild(phonemesDiv);
      textContainer.appendChild(wordBlock);
    });
  </script>
</body>
</html>
"""

# Embed the HTML in Streamlit
st.title("Phoneme Visualization with Top 100 Words")
components.html(html_content, height=1000, width=900)