import React from "react";
import "./Flowsection.css";
import RedditStream from "../stream/RedditStream";
import MediumStream from "../stream/MediumStream";
import TwitterStream from "../stream/TwitterStream";

class Flowsection extends React.Component {
  render() {
    return (
      <div className="flowsection">
        <RedditStream />
        <MediumStream />
        <TwitterStream />
      </div>
    );
  }
}

export default Flowsection;
