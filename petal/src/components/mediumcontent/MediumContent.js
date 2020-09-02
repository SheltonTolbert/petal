import React from "react";
import "./mediumContent.css";

class MediumContent extends React.Component {
  render() {
    return (
      <div className="mediumcontent">
        <div className="topbar">
          <img
            className="medium_logo"
            src={this.props.medium_logo}
            alt="subreddit"
          ></img>
          <div className="medium_category">{this.props.category}</div>
        </div>
        <div className="article_body">
          <img
            className="content_image"
            src={this.props.content_image}
            alt="content"
          ></img>
          <a className="title" href={this.props.link}>
            {this.props.title}
          </a>
          <div className="info"></div>
        </div>
      </div>
    );
  }
}

export default MediumContent;
