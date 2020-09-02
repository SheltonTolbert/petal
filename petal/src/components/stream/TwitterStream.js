import React from "react";
import "./Stream.css";
import TwitterContent from "../twittercontent/TwitterContent";
import data from "../../data.json";

class TwitterStream extends React.Component {
  render() {
    var arr = [];
    var table = [];
    var twitter_data = data["twitter"];
    Object.keys(twitter_data).forEach(function (key) {
      arr.push(twitter_data[key]);
    });

    arr.map((post) =>
      table.push(
        <TwitterContent
          key={post["score"]}
          profile_image={post["profile_img"]}
          username={post["username"]}
          content={post["text"]}
          link={post["link"]}
        />
      )
    );

    return (
      <div className="stream">
        {table.map((element) => (
          <div>{element}</div>
        ))}
      </div>
    );
  }
}

export default TwitterStream;
