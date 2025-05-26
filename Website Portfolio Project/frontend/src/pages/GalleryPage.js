import React from "react";

import ImageGallery from "react-image-gallery";

const images = [
  {
    original: "images/gracie-kimura-lock.jpg",
    thumbnail: "images/gracie-kimura-lock.jpg",
    description:
      "Royce Gracie, Brazilian MMA fighter and UFC hall-of-famer, showed us how to perform a kimura lock during a lesson. I wrote a feature story and interviewed him. (2017)",
    originalHeight: "450px",
  },
  {
    original: "images/boston-interview.jpg",
    thumbnail: "images/boston-interview.jpg",
    description:
      "I interviewed Boston for a concert preview story I wrote. The band had changed considerably since the seventies. Their then-drummer, Tommy DeCarlo, they'd found on MySpace performing cover songs. (2017)",
    originalHeight: "450px",
  },
  {
    original: "images/cherry-blossom-ganghwado.jpg",
    thumbnail: "images/cherry-blossom-ganghwado.jpg",
    description:
      "Each spring, cherry blossom season blooms in South Korea. Here, I had first moved to Ganghwa Island, a semi-rural community near North Korea with a sparse westerner presence. (2018)",
    originalHeight: "450px",
  },
  {
    original: "images/yongsan-base-seoul.jpg",
    thumbnail: "images/yongsan-base-seoul.jpg",
    description:
      "In 2018, the US moved its Korea headquarters from Yongsan Garrison in Seoul to Pyeongtaek. The States' significant regional presence has sometimes influenced Korean policy. One example is the THAAD anti-missile system deployed in 2017, which pleased some but upset Korean leftist opposition. (2018)",
    originalHeight: "450px",
  },
  {
    original: "images/akihabara-district-tokyo.jpg",
    thumbnail: "images/akihabara-district-tokyo.jpg",
    description:
      "While visiting my friend in Tokyo, I saw what the Akihabara district does best — consumerism. Many consider it the center of otaku culture, a — sometimes controversial — Japanese word to describe avid media consumers. (2018)",
    originalHeight: "450px",
  },
  {
    original: "images/hanok-village-seoul.jpg",
    thumbnail: "images/hanok-village-seoul.jpg",
    description:
      "Hanok Bukchon Village — Bukchon meaning 'north village' in Korean — is a 600-year-old traditional village preserved in Seoul. Government officials and nobility lived there during the Joseon Dynasty. (2021)",
    originalHeight: "450px",
  },
  {
    original: "images/kazan-cathedral-saint-petersburg.jpg",
    thumbnail: "images/kazan-cathedral-saint-petersburg.jpg",
    description:
      "When I lived in Russia, I passed the Kazan Cathedral every morning while walking to work in St. Petersburg. The Russian Orthodox Church building, constructed in 1801, is also a landmark of resistance during the 1812 French invasion. (2021)",
    originalHeight: "450px",
  },
  {
    original: "images/soviet-chess-set.jpg",
    thumbnail: "images/soviet-chess-set.jpg",
    description:
      "I bought a 1960s Soviet Union-era chess set in Russia that, unfortunately, got left behind. The war began four days later, and many westerners — including me — booked immediate flights with limited luggage space. This is in a khrushchevka, a low-cost, widely produced Soviet apartment analogous to cookie-cutter neighborhoods in America.  (2022)",
    originalHeight: "450px",
  },
  {
    original: "images/lazycase-hackathon-project.jpg",
    thumbnail: "images/lazycase-hackathon-project.jpg",
    description:
      "I registered for the BeaverHacks Fall Hackathon when I first began getting serious about a career change. My teammates and I wrote a Google Doc add-on to auto-format academic titles for APA, Chicago and MLA styles. It sparked some questions on part-of-speech tagging and ideas to expand the project. (2022)",
    originalHeight: "450px",
  },
  {
    original: "images/orthokon-python-project.jpg",
    thumbnail: "images/orthokon-python-project.jpg",
    description:
      "I wrote this game two years ago for a class but rewrote from scratch recently to avoid violating academic policy. It was also for terminal output, and GUI gameplay with keyboard events required completely different logic. I realized I didn't understand OOP as well as I thought, and fixing memory leaks took longer than I want to admit. (2022)",
    originalHeight: "450px",
  },
];

function GalleryPage() {
  return (
    <div>
      <h2>Gallery of Memories</h2>
      <article class="gallery">
        <ImageGallery items={images} />
      </article>
    </div>
  );
}

export default GalleryPage;
