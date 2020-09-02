import React from "react";
import "./Redditcontent.css";

class Redditcontent extends React.Component {
  render() {
    return (
      <div className="redditcontent">
        <div className="topbar">
          <img
            className="subreddit_image"
            src={this.props.subreddit_image}
            alt="subreddit"
          ></img>

          <div className="subreddit_name">{this.props.subreddit_name}</div>
        </div>
        <div className="reddit_body">
          <div
            className="content_image"
            img={this.props.content_image}
            alt="content"
          ></div>
          <a className="reddit_title" href={this.props.link}>
            {this.props.title}
          </a>
          <div className="info"></div>
        </div>
      </div>
    );
  }
}

export default Redditcontent;
