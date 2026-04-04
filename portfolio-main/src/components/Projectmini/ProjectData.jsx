import warehouse from "../Images/projectPics/warehouse.png";
import port from "../Images/projectPics/port.png";
import ott from "../Images/projectPics/ott.png";
import soon from "../../assets/soon.webp";

const fullstack = [
  {
    id: "002",
    softUsed: ["react.js", "css", "tailwind css","Html","JS","bootstrap"],
    title: "Portfolio 2.0",
    description: "The portfolio you are viewing right now",
    image: port,
    link: "https://github.com/ibrahim-borio/Final-Project-Portfolio-.git",
  },
  {
    id: "001",
    softUsed: [
      "express.js",
      "node.js",
      "mongodb",
      "html (ejs template)",
      "bootstrap",
      "react.js",
      "css",
    ],
    title: "Furniture Website",
    description: "Users can Order furniture online",
    image: ott,
    link: "https://github.com/ibrahim-borio/Website.git",
  },
  {
    id: "003",
    softUsed: ["bootstrap", "react.js", "css"],
    title: "Appexy ",
    description: "A website to Managing and payment plans",
    image: warehouse,
    link: "https://github.com/ibrahim-borio/U12.git",
  },
  {
    id: "004",
    softUsed: [" techn is loading", " please be patient "],
    title: "Coming soon",
    description: "Yes, I am working on it",
    image: soon,
    link: "#",
  },
];

const frontend = [
  {
    id: "001",
    softUsed: [" techn is loading", " please be patient "],
    title: "Coming soon",
    description: "Yes, I am working on it",
    image: soon,
    link: "#",
  },
];

export { fullstack, frontend };
