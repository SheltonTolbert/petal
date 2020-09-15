import React from "react";
import "./mediumContent.css";

class MediumContent extends React.Component {
  render() {
    return (
      <div className="medium_content">
        <div className="medium_topbar">
          <img
            className="medium_logo"
            src={this.props.medium_logo}
            alt="subreddit"
          ></img>
          <div className="medium_category">{this.props.category}</div>
        </div>
        <div className="medium_article_body">
          <img
            className="medium_content_image"
            src={this.props.content_image}
            alt="medium_content"
          ></img>
          <a className="medium_title" href={this.props.link}>
            {this.props.title}
          </a>
          <div className="medium_info"></div>
        </div>
      </div>
    );
  }
}

export default MediumContent;
