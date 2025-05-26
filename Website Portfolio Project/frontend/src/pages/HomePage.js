import React from "react";

function HomePage() {
  return (
    <div>
      <h2>Welcome</h2>
      <p>This website was created with MangoDB, Express, React, and Node.js (MERN). Several other web technologies contributed like HTML for webpage-creation and CSS for design. Both have employed JavaScript for more dynamic elements, and React provides a better user interface while optimizing performance.</p>
      <p>The Node.js runtime environment lets developers run JavaScript for higher-performance web apps from the backend (i.e., asynchronous programming is one instance). The Express framework for Node.js streamlined HTTP requests and responses, routing, and middleware. The MongoDB database system stores this site's data as JSON objects.</p>
      <p>Ancillary technologies also helped. The scalable vector icons used come from the React Icons library. Mongoose, an ODM library for MangoDB and Node.js, helped create a schema for one page.</p>
    </div>
  );
}

export default HomePage;
