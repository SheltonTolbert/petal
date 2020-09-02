import React from "react";
import "./twittercontent.css";

class TwitterContent extends React.Component {
  render() {
    return (
      <div className="twittercontent">
        <div className="topbar">
          <img
            className="profile_image"
            src={this.props.profile_image}
            alt="profile"
          ></img>
          <div className="username">{this.props.username}</div>
        </div>
        <div className="body">
          <a className="content" href={this.props.link}>
            {this.props.content}
          </a>
          <div className="info"></div>
        </div>
      </div>
    );
  }
}

export default TwitterContent;
