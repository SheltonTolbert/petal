import React from "react";
import "./Stream.css";
import Redditcontent from "../redditcontent/Redditcontent";
import data from "../../data.json";

class RedditStream extends React.Component {
  render() {
    var arr = [];
    var table = [];
    var reddit_data = data["reddit"];
    Object.keys(reddit_data).forEach(function (key) {
      arr.push(reddit_data[key]);
    });

    arr.map((post) =>
      table.push(
        <Redditcontent
          key={post["score"]}
          subreddit_image="https://banner2.cleanpng.com/20180615/ro/kisspng-reddit-logo-computer-icons-reddit-5b234a1c1cd1f0.3657774515290393881181.jpg"
          title={post["title"]}
          link={post["link"]}
          subreddit_name="r/thisisatest"
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

export default RedditStream;
