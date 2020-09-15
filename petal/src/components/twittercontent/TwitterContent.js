import React from "react";
import "./twittercontent.css";

class TwitterContent extends React.Component {
  render() {
    return (
      <div className="twitter_content">
        <div className="twitter_topbar">
          <img
            className="twitter_profile_image"
            src={this.props.profile_image}
            alt="profile"
          ></img>
          <div className="twitter_username">{this.props.username}</div>
        </div>
        <div className="twitter_body">
          <a className="twitter_content" href={this.props.link}>
            {this.props.content}
          </a>
          <div className="twitter_info"></div>
        </div>
      </div>
    );
  }
}

export default TwitterContent;
