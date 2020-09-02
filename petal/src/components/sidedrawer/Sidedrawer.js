import React from "react";
import "./Sidedrawer.css";
import RedditSidebar from "./redditsidebar/RedditSidebar";

class Sidedrawer extends React.Component {
  render() {
    return (
      <div className="sidedrawer">
        <RedditSidebar />
      </div>
    );
  }
}

export default Sidedrawer;
