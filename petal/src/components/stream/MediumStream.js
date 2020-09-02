import React from "react";
import "./Stream.css";
import MediumContent from "../mediumcontent/MediumContent.js";
import data from "../../data.json";

class MediumStream extends React.Component {
  render() {
    var arr = [];
    var table = [];
    var medium_data = data["medium"];
    Object.keys(medium_data).forEach(function (key) {
      arr.push(medium_data[key]);
    });

    arr.map((post) =>
      table.push(
        <MediumContent
          key={post["link"]}
          medium_logo="https://cdn4.iconfinder.com/data/icons/social-media-2210/24/Medium-512.png"
          category={post["category"]}
          content_image="https://miro.medium.com/max/700/1*yTB0AML2PhCGh6iK5eDgbg.jpeg"
          title={post["title"]}
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

export default MediumStream;
